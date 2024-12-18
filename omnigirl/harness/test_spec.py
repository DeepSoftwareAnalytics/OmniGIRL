import hashlib
import json
import platform
import re

from dataclasses import dataclass
from typing import Any, Union

from constants import (
    SWEbenchInstance,
    MAP_REPO_TO_INSTALL,
    MAP_VERSION_TO_INSTALL,
    MAP_REPO_TO_TEST_FRAMEWORK,
    USE_X86,
)
from dockerfiles import (
    get_dockerfile_base,
    get_dockerfile_env,
    get_dockerfile_instance,
)
from utils import (
    get_requirements,
    get_environment_yml,
    get_test_directives,
)

DIFF_MODIFIED_FILE_REGEX = r"--- a/(.*)"


@dataclass
class TestSpec:
    """
    A dataclass that represents a test specification for a single instance of SWE-bench.
    """
    instance_id: str
    repo: str
    version: str
    repo_script_list: str
    eval_script_list: str
    env_script_list: str
    arch: str
    FAIL_TO_PASS: list[str]
    PASS_TO_PASS: list[str]

    @property
    def setup_env_script(self):
        return "\n".join(["#!/bin/bash", "set -euxo pipefail"] + self.env_script_list) + "\n"

    @property
    def eval_script(self):
        return "\n".join(["#!/bin/bash", "set -uxo pipefail"] + self.eval_script_list) + "\n"
        # Don't exit early because we need to revert tests at the end

    @property
    def install_repo_script(self):
        return "\n".join(["#!/bin/bash", "set -euxo pipefail"] + self.repo_script_list) + "\n"

    @property
    def base_image_key(self):
        return f"sweb.base.{self.arch}:latest"

    @property
    def env_image_key(self):
        """
        The key for the environment image is based on the hash of the environment script list.
        If the environment script list changes, the image will be rebuilt automatically.

        Note that old images are not automatically deleted, so consider cleaning up old images periodically.
        """
        hash_object = hashlib.sha256()
        hash_object.update(str(self.env_script_list).encode("utf-8"))
        hash_value = hash_object.hexdigest()
        val = hash_value[:22]  # 22 characters is still very likely to be unique
        return f"sweb.env.{self.arch}.{val}:latest"

    @property
    def instance_image_key(self):
        return f"sweb.eval.{self.arch}.{self.instance_id.lower()}:latest"

    def get_instance_container_name(self, run_id=None):
        if not run_id:
            return f"sweb.eval.{self.instance_id}"
        return f"sweb.eval.{self.instance_id}.{run_id}"

    @property
    def base_dockerfile(self):
        return get_dockerfile_base(self.platform, self.arch)

    @property
    def env_dockerfile(self):
        return get_dockerfile_env(self.platform, self.arch)

    @property
    def instance_dockerfile(self):
        return get_dockerfile_instance(self.platform, self.env_image_key)

    @property
    def platform(self):
        if self.arch == "x86_64":
            return "linux/x86_64"
        elif self.arch == "x86_64_js":
            return "linux/x86_64"
        elif self.arch == "x86_64_java" or self.arch == "x86_64_java_gradle":
            return "linux/x86_64"
        elif self.arch == "x86_64_js_ubuntu_20":
            return "linux/x86_64"
        elif self.arch == "x86_64_ubuntu_20":
            return "linux/x86_64"
        elif self.arch == "x86_64_ubuntu_16":
            return "linux/x86_64"
        elif self.arch == "arm64":
            return "linux/arm64/v8"
        else:
            raise ValueError(f"Invalid architecture: {self.arch}")
        

def get_test_specs_from_dataset(dataset: Union[list[SWEbenchInstance], list[TestSpec]]) -> list[TestSpec]:
    """
    Idempotent function that converts a list of SWEbenchInstance objects to a list of TestSpec objects.
    """
    if isinstance(dataset[0], TestSpec):
        return dataset
    test_specs = list(map(make_test_spec, dataset))
    test_specs = [test_spec for test_spec in test_specs if test_spec!=None]
    return test_specs


def make_repo_script_list(install, repo, repo_directory, base_commit, env_name):
    """
    Create a list of bash commands to set up the repository for testing.
    This is the setup script for the instance image.
    """
    if 'python' in install:
        setup_commands = [
            f"git clone -o origin https://github.com/{repo} {repo_directory}",
            f"chmod -R 777 {repo_directory}",  # So nonroot user can run tests
            f"cd {repo_directory}",
            f"git reset --hard {base_commit}",
            # Remove the remote so the agent won't see newer commits.
            f"git remote remove origin",
            # Make sure conda is available for later use
            "source /opt/miniconda3/bin/activate",
            f"conda activate {env_name}",
            f'echo "Current environment: $CONDA_DEFAULT_ENV"',
        ]
        if repo in MAP_REPO_TO_INSTALL:
            setup_commands.append(MAP_REPO_TO_INSTALL[repo])

        # Run pre-install set up if provided
        if "pre_install" in install:
            for pre_install in install["pre_install"]:
                setup_commands.append(pre_install)
        if 'setup_command' in install:
            for setup_command in install["setup_command"]:
                setup_commands.append(setup_command)
        if "install" in install:
            setup_commands.append(install["install"])
    elif 'java' in install:
        setup_commands = [
            f"git clone -o origin https://github.com/{repo} {repo_directory}",
            f"chmod -R 777 {repo_directory}",  # So nonroot user can run tests
            f"cd {repo_directory}",
            f"git reset --hard {base_commit}",
            # Remove the remote so the agent won't see newer commits.
            f"git remote remove origin",
            # Make sure conda is available for later use
     
        ]
        if repo in MAP_REPO_TO_INSTALL:
            setup_commands.append(MAP_REPO_TO_INSTALL[repo])
     
        if "pre_install" in install:
            for pre_install in install["pre_install"]:
                setup_commands.append(pre_install)
        if 'setup_command' in install:
            for setup_command in install["setup_command"]:
                setup_commands.append(setup_command)
        if "install" in install:
            setup_commands.append(install["install"])
    elif 'nodejs' in install:
        if 'null' in repo.lower():
            setup_commands = [
                f"git clone --depth 1 https://github.com/{repo} {repo_directory}",  # Shallow clone to only fetch the latest commit
                f"chmod -R 777 {repo_directory}",  # So nonroot user can run tests
                f"cd {repo_directory}",
                f"git fetch --depth=1 origin {base_commit}",  # Fetch only the specific commit you need
                f"git checkout -f {base_commit}",  # Checkout to the specific commit
                # Remove the remote so the agent won't see newer commits.
                f"git remote remove origin",
                # Make sure conda is available for later use
            ]

        else: 
            setup_commands = [
                f"git clone -o origin https://github.com/{repo} {repo_directory}",
                f"chmod -R 777 {repo_directory}",  # So nonroot user can run tests
                f"cd {repo_directory}",
                f"git reset --hard {base_commit}",
                # Remove the remote so the agent won't see newer commits.
                f"git remote remove origin",
                # Make sure conda is available for later use
        
            ]
        if repo in MAP_REPO_TO_INSTALL:
            setup_commands.append(MAP_REPO_TO_INSTALL[repo])

        # Run pre-install set up if provided
        if "pre_install" in install:
            for pre_install in install["pre_install"]:
                setup_commands.append(pre_install)
        if 'setup_command' in install:
            for setup_command in install["setup_command"]:
                setup_commands.append(setup_command)
        if "install" in install:
            setup_commands.append(install["install"])
    return setup_commands


def make_env_script_list(instance, install, env_name):
    """
    Creates the list of commands to set up the conda environment for testing.
    This is the setup script for the environment image.
    """
    HEREDOC_DELIMITER = "EOF_59812759871"

    if 'python' in install:
        reqs_commands = [
            "source /opt/miniconda3/bin/activate",
        ]
        # Create conda environment according to install instructinos
        pkgs = install.get("packages", "")
        if pkgs == "requirements.txt":
            # Create environment
            cmd = f"conda create -n {env_name} python={install['python']} -y"
            reqs_commands.append(cmd)

            # Install dependencies
            reqs = get_requirements(instance)
            path_to_reqs = "$HOME/requirements.txt"
            reqs_commands.append(
                f"cat <<'{HEREDOC_DELIMITER}' > {path_to_reqs}\n{reqs}\n{HEREDOC_DELIMITER}"
            )
            cmd = f"conda activate {env_name} && python -m pip install -r {path_to_reqs}"
            reqs_commands.append(cmd)
            reqs_commands.append(f"rm {path_to_reqs}")
        elif pkgs == "environment.yml":
            # Create environment from yml
            reqs = get_environment_yml(instance, env_name)
            path_to_reqs = "environment.yml"
            reqs_commands.append(
                f"cat <<'{HEREDOC_DELIMITER}' > {path_to_reqs}\n{reqs}\n{HEREDOC_DELIMITER}"
            )
            if "no_use_env" in install and install["no_use_env"]:
                # `conda create` based installation
                cmd = f"conda create -c conda-forge -n {env_name} python={install['python']} -y"
                reqs_commands.append(cmd)

                # Install dependencies
                cmd = f"conda env update -f {path_to_reqs}"
                reqs_commands.append(cmd)
            else:
                # `conda env create` based installation
                cmd = f"conda env create --file {path_to_reqs}"
                reqs_commands.append(cmd)

                cmd = f"conda activate {env_name} && conda install python={install['python']} -y"
                reqs_commands.append(cmd)

            # Remove environment.yml
            reqs_commands.append(f"rm {path_to_reqs}")
        else:
            # Create environment + install dependencies
            cmd = f"conda create -n {env_name} python={install['python']} {pkgs} -y"
            reqs_commands.append(cmd)

        reqs_commands.append(f"conda activate {env_name}")

        # Install additional packages if specified
        if "pip_packages" in install:
            pip_packages = " ".join(install["pip_packages"])
            cmd = f"python -m pip install {pip_packages}"
            reqs_commands.append(cmd)

        if 'apt' in install: 
            # apt_packages = " ".join(install["apt"])
            # cmd = f"{apt_packages}"
            
            for apt_cmd in install['apt']:
                # print(apt_cmd)
                reqs_commands.append(apt_cmd)
    elif 'nodejs' in install:
        reqs_commands = []
        cmd = f"volta install node@{install['nodejs']}"
        reqs_commands.append(cmd)
        if 'yarn' in install:
            yarn_cmd = f"volta install yarn"
            reqs_commands.append(yarn_cmd)
        if 'apt' in install: 
            # apt_packages = " ".join(install["apt"])
            # cmd = f"{apt_packages}"
            
            for apt_cmd in install['apt']:
                # print(apt_cmd)
                reqs_commands.append(apt_cmd)
    elif 'java' in install:
        reqs_commands = []
        reqs_commands.append('set +u')
        # reqs_commands.append('curl -s "https://get.sdkman.io" | bash')
        reqs_commands.append(install['java'])
        reqs_commands.append('set -u')
        # if 'maven' in install:
        #     reqs_commands.append(install['maven'])
       

    return reqs_commands




def find_first_special_pattern(text):
    """
    Find and return the first substring that matches the pattern 'test/xxxCases' in the provided text.
    """
    pattern = r"test/\w+Cases"
    match = re.search(pattern, text)
    if match:
        return match.group()  # 返回匹配的字符串
    else:
        return None


def get_filter_test_directives(instance):
    test_directives = get_test_directives(instance)
    
    repo = instance['repo']

    if 'typescript' in repo.lower():
        
        test_directives = [t for t in test_directives if t.endswith('.ts')]
    elif 'prettier' in repo.lower():
        
        test_directives = [t.replace('/__snapshots__','').replace('.snap','') for t in test_directives if '__snapshots__' in t]
    elif 'goose' in repo.lower():
        test_directives = [t for t in test_directives if t.endswith('.js')]
    elif 'pack' in repo.lower():
        new_test_directives = []
        for t in test_directives:
            if '__snapshots__' in t:
                new_test_directives.append(t.replace('/__snapshots__','').replace('.snap','') )
            special_pattern = find_first_special_pattern(t)
            if special_pattern:
                
                if 'test/configCases' == special_pattern:
                    # subtest = t.replace(special_pattern+'/','').split('/')[0]
                    new_t = f'ConfigTestCases'
                    new_test_directives.append(new_t)
                    # print('yes')
                    # print(new_t)
                    # input()
                # input()

            if 'ConfigTestCases' in t:
                new_test_directives.append('ConfigTestCases')
            if 'StatsTestCases' in t:
                new_test_directives.append('StatsTestCases')
            # if 'watchCases' in t:
            #     new_test_directives.append('StatsTestCases')
            if t.endswith('.test.js'):
                new_test_directives.append(t)
            if 'test/cases/parsing' in t:
                new_test_directives.append('test/JavascriptParser.unittest.js')
            if 'watchCases' in t:
                new_test_directives.append('test/Watch.test.js')
            if 'hotCases' in t:
                new_test_directives.append("HotTestCases")
            if t.endswith('.unittest.js'):
                new_test_directives.append(t)
            if t.endswith('.longtest.js'):
                new_test_directives.append(t)
        new_test_directives = list(set(new_test_directives))
        #     elif t.endswith('index.js'):
        #         new_test_directives.append(t)
        # # return ['']
        return new_test_directives
    elif 'jest' in repo.lower():
        new_test_directives = []
        for t in test_directives:
            if '__snapshots__' in t:
                new_test_directives.append(t.replace('/__snapshots__','').replace('.snap','') )
            if t.endswith('.test.ts'):
                new_test_directives.append(t)
            # if t.endswith('.test.js'):
            #     new_test_directives.append(t)
        new_test_directives = list(set(new_test_directives))
        # if len(new_test_directives) == 1:
        #     ver = instance['version']
        #     p_number = instance['pull_number']
        #     # print(new_test_directives)
        #     print(f'{p_number}')
        #     elif t.endswith('index.js'):
        #         new_test_directives.append(t)
        # # return ['']
        return new_test_directives
    elif 'babel' in repo.lower():
        new_test_directives = []
        for t in test_directives:
            if 'test/fixtures/' in t:
                # truncated_t = t.split('test/fixtures/', 1)[1]
                # formatted_t = " ".join(part.replace('-', ' ') for part in truncated_t.split('/')[:-1])
                # temp_t = f'-t "{formatted_t}"'
                temp_t = t.split('/')[1]
                new_test_directives.append(temp_t)
        new_test_directives = list(set(new_test_directives))
        return new_test_directives
    elif 'jetty' in repo.lower() or 'assertj' in repo.lower() or 'gson' in repo.lower() or 'netty' in repo.lower():
        new_test_directives = []
        for t in test_directives:
            if '.java' in t:
                temp_t = t.split('/')[-1]
                temp_t = temp_t.split('.')[0]
                new_test_directives.append(temp_t)
        new_test_directives = list(set(new_test_directives))
        return new_test_directives
    elif 'junit' in repo.lower() or 'retrofit' in repo.lower() or 'testng' in repo.lower():
        new_test_directives = []
        for t in test_directives:
            if '.java' in t:
                temp_t = t.split('/')[-1]
                temp_t = temp_t.split('.')[0]
                temp_t = f'--tests "{temp_t.strip()}"'
                new_test_directives.append(temp_t)
        new_test_directives = list(set(new_test_directives))
        return new_test_directives

    
    # elif 'h2' in repo.lower():
    #     new_test_directives = []
    #     for t in test_directives:
    #         if '.java' in t and 'Test' in t:
    #             temp_t = t.split('/')[-1]
    #             temp_t = temp_t.split('.')[0]
    #             new_test_directives.append(temp_t)
    #             # if len(t.split('src/test/'))==2:
    #             #     temp_t = t.split('src/test/')[1]
    #             #     temp_t= temp_t.replace('.java','')
    #             #     temp_t = temp_t.replace('/','.')
    #             #     new_test_directives.append(temp_t)
    #             # else:
    #             #     new_test_directives.append(temp_t)
    #         if t.endswith('.sql'):
    #             if 'scripts' in t:
    #                  new_test_directives.append('TestScript')
    #                 # new_test_directives.append('org.h2.test.scripts.TestScript')
                    

        new_test_directives = list(set(new_test_directives))         
        return new_test_directives

        
    return  test_directives

def make_eval_script_list(instance, install, env_name, repo_directory, base_commit, test_patch):
    """
    Applies the test patch and runs the tests.
    """
    HEREDOC_DELIMITER = "EOF_114329324912"
    test_files = re.findall(DIFF_MODIFIED_FILE_REGEX, test_patch)
    reset_test_files = ['"' + t + '"' for t in test_files]
    # Reset test files to the state they should be in before the patch.
    reset_tests_command = f"git checkout {base_commit} {' '.join(reset_test_files)}"
    apply_test_patch_command = (
        f"git apply -v - <<'{HEREDOC_DELIMITER}'\n{test_patch}\n{HEREDOC_DELIMITER}"
    )
    
    if 'python' in install:
        if 'dateutil' in instance["repo"]:

            
            test_command =MAP_REPO_TO_TEST_FRAMEWORK[instance["repo"]][instance["version"]]


        else:
            test_command = " ".join(
                [
                    MAP_REPO_TO_TEST_FRAMEWORK[instance["repo"]][instance["version"]],
                    *get_test_directives(instance),
                ]
            )
        eval_commands = [
            f"source /opt/miniconda3/bin/activate",
            f"conda activate {env_name}",
            f"cd {repo_directory}",
        ]
        if "eval_commands" in install:
            eval_commands += install["eval_commands"]
        eval_commands += [
            f"git config --global --add safe.directory {repo_directory}",  # for nonroot user
            f"cd {repo_directory}",
            # This is just informational, so we have a record
            f"git status",
            f"git show",
            f"git diff {base_commit}",
            "source /opt/miniconda3/bin/activate",
            f"conda activate {env_name}",
        ]
        if 'extra_command' in install:
            for extra_command in install["extra_command"]:
                eval_commands.append(extra_command)
        if "install" in install:
            eval_commands.append(install["install"])
        eval_commands += [
            reset_tests_command,
            apply_test_patch_command,
            test_command,
            reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
        ]
    elif 'nodejs' in install:
        test_command = " ".join(
                [
                    MAP_REPO_TO_TEST_FRAMEWORK[instance["repo"]][instance["version"]],
                    # *get_test_directives(instance),
                    *get_filter_test_directives(instance)

                ]
            )
        eval_commands = [
            f"cd {repo_directory}",
        ]
        if "eval_commands" in install:
            eval_commands += install["eval_commands"]
        eval_commands += [
            f"git config --global --add safe.directory {repo_directory}",  # for nonroot user
            f"cd {repo_directory}",
            # This is just informational, so we have a record
            f"git status",
            f"git show",
            f"git diff {base_commit}",
        ]
        if 'extra_command' in install:
            for extra_command in install["extra_command"]:
                eval_commands.append(extra_command)
        if "install" in install:
            eval_commands.append(install["install"])
        if 'hereby' in install:
            hereby_command = 'hereby'
            hereby_commands= " ".join(
                [
                    'node ./built/local/tsc.js --watch',
                    *get_test_directives(instance),
                ]
            )
            eval_commands += [
                reset_tests_command,
                apply_test_patch_command,
                hereby_command,
                hereby_commands,
                test_command,
                reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
            ]
        elif 'update_command' in install:
            eval_commands += [
                reset_tests_command,
                apply_test_patch_command,
                install['update_command'],
                test_command,
                reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
            ]
        else:
            if instance['instance_id'] in ['iamkun__dayjs-1003','iamkun__dayjs-1015','iamkun__dayjs-1054','iamkun__dayjs-1160','iamkun__dayjs-1161','iamkun__dayjs-1164','iamkun__dayjs-987','iamkun__dayjs-998','iamkun__dayjs-994']:
                eval_commands += [
                    reset_tests_command,
                    apply_test_patch_command,
                    "sed -i 's/MockDate\.set(new Date())/MockDate.set(\"2024-09-01T00:00:00Z\")/' test/plugin/timezone.test.js",
                    test_command,
                    reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
                ]
            else:
                eval_commands += [
                    reset_tests_command,
                    apply_test_patch_command,
                    test_command,
                    reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
                ]
    elif 'java' in install:
        repo_test_command = MAP_REPO_TO_TEST_FRAMEWORK[instance["repo"]][instance["version"]]
       
        if 'h2' in instance['repo'].lower():
            test_command = repo_test_command

        elif 'mvn' in repo_test_command:
            repo_test_directives = get_filter_test_directives(instance)
            repo_test_directives = [d.strip() for d in repo_test_directives]
            if 'netty' in instance['repo'].lower():
                test_files=f"{' '.join(reset_test_files)}"
                match = re.search(r'([^/]+)/src', test_files)
                if match:
                    module_name = match.group(1).replace('"', '')
                else:
                    module_name = ""
                if module_name:
                    pl_option = f"-pl {module_name}"
                else:
                    pl_option = ""   
                test_command = repo_test_command.replace("{pl_option}", pl_option) + '"' + ','.join(repo_test_directives)+'"'+' -X'
            else:
                test_command = repo_test_command +'"'+ ','.join(repo_test_directives)+'"'+' -X'

        else:
            test_command = " ".join(
                    [
                        MAP_REPO_TO_TEST_FRAMEWORK[instance["repo"]][instance["version"]],
                        # *get_test_directives(instance),
                        *get_filter_test_directives(instance)

                    ]
                )
        eval_commands = [
            f"cd {repo_directory}",
        ]
        # print(test_command)
        if "eval_commands" in install:
            eval_commands += install["eval_commands"]
        eval_commands += [
            f"git config --global --add safe.directory {repo_directory}",  # for nonroot user
            f"cd {repo_directory}",
            # This is just informational, so we have a record
            f"git status",
            f"git show",
            f"git diff {base_commit}",
        ]


        eval_commands += [
             'set +u',
                reset_tests_command,
                apply_test_patch_command,
                test_command,
                reset_tests_command,  # Revert tests after done, leave the repo in the same state as before
                'set -u',
            ]
    return eval_commands




def make_test_spec(instance: SWEbenchInstance,language = 'python') -> TestSpec:
    if isinstance(instance, TestSpec):
        return instance
    instance_id = instance["instance_id"]
    repo = instance["repo"]
    version = instance["version"]
    base_commit = instance["base_commit"]
    problem_statement = instance["problem_statement"]
    hints_text = instance["hints_text"]  # Unused
    test_patch = instance["test_patch"]



    def _from_json_or_obj(key: str) -> Any:
        """If key points to string, load with json"""
        if isinstance(instance[key], str):
            return json.loads(instance[key])
        return instance[key]

    pass_to_pass = _from_json_or_obj("PASS_TO_PASS")
    fail_to_pass = _from_json_or_obj("FAIL_TO_PASS")

    env_name = "testbed"
    repo_directory = f"/{env_name}"
    # install = MAP_VERSION_TO_INSTALL[repo][version]
    install = MAP_VERSION_TO_INSTALL.get(repo, {}).get(version, None)
    # print(MAP_VERSION_TO_INSTALL.get('jestjs/jest', {}))
    # print(repo)
    # print(MAP_VERSION_TO_INSTALL)
    if install is None:
        # print(version)
        # input()
        # Handle the case where the repo or version does not exist in MAP_VERSION_TO_INSTALL
        # For example, we could skip the processing, raise an error, or set a default value.
        # Here, we simply return None to skip the processing.
        return None

    if get_filter_test_directives(instance) == []:

        return None


        


    repo_script_list = make_repo_script_list(install, repo, repo_directory, base_commit, env_name)
    env_script_list = make_env_script_list(instance, install, env_name)
    eval_script_list = make_eval_script_list(
        instance, install, env_name, repo_directory, base_commit, test_patch
    )



    if platform.machine() in {"aarch64", "arm64"}:
        # use arm64 unless explicitly specified
        arch = "arm64" if instance_id not in USE_X86 else "x86_64"
    elif 'microsoft' in repo or 'prettier' in repo or 'eslint' in repo or 'tailwind' in repo or 'webpack' in repo or 'jest' in repo or 'babel' in repo or 'dayjs' in repo:

        arch = 'x86_64_js'
    elif 'jetty' in repo or 'h2' in repo or 'assertj' in repo or 'gson' in repo or 'netty' in repo:
        arch = 'x86_64_java'
    elif 'junit' in repo or 'retrofit' in repo or 'testng' in repo:
        arch = 'x86_64_java_gradle'
    elif 'mongoose' in repo:

        arch = 'x86_64_js_ubuntu_20'
    elif 'crypto' in instance['repo'] and instance['version']in ['35.0','3.1','3.2','3.3','3.4']:
        arch = 'x86_64_ubuntu_20'
    
    elif 'crypto' in instance['repo'] and (instance['version'].startswith('2.') or instance['version']=='3.0' or instance['version'].startswith('1.')  ):
        arch = 'x86_64_ubuntu_16'

    else:
        arch = "x86_64"

    return TestSpec(
        instance_id=instance_id,
        repo=repo,
        env_script_list=env_script_list,
        repo_script_list=repo_script_list,
        eval_script_list=eval_script_list,
        version=version,
        arch=arch,
        FAIL_TO_PASS=fail_to_pass,
        PASS_TO_PASS=pass_to_pass,
    )
