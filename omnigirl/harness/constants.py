from enum import Enum
from pathlib import Path
from typing import TypedDict

# Constants - Evaluation Log Directories
BASE_IMAGE_BUILD_DIR = Path("image_build_logs/base")
ENV_IMAGE_BUILD_DIR = Path("image_build_logs/env")
INSTANCE_IMAGE_BUILD_DIR = Path("image_build_logs/instances")
RUN_INSTANCE_LOG_DIR = Path("run_instance_logs")


# Constants - Task Instance Class
class SWEbenchInstance(TypedDict):
    repo: str
    instance_id: str
    base_commit: str
    patch: str
    test_patch: str
    problem_statement: str
    hints_text: str
    created_at: str
    version: str
    FAIL_TO_PASS: str
    PASS_TO_PASS: str
    environment_setup_commit: str


# Constants - Test Types + Statuses
FAIL_TO_PASS = "FAIL_TO_PASS"
FAIL_TO_FAIL = "FAIL_TO_FAIL"
PASS_TO_PASS = "PASS_TO_PASS"
PASS_TO_FAIL = "PASS_TO_FAIL"


class ResolvedStatus(Enum):
    NO = "RESOLVED_NO"
    PARTIAL = "RESOLVED_PARTIAL"
    FULL = "RESOLVED_FULL"


class TestStatus(Enum):
    FAILED = "FAILED"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"
    XFAIL = "XFAIL"





MAP_VERSION_TO_INSTALL_GSON = {
    k: {
   "java": 'curl -s "https://get.sdkman.io" | bash && source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 11.0.20.1-tem  && sdk install maven 3.6.3 && mvn --version',
   }

    #version 
    for k in [
        "2.8",
        "2.9",
        "2.10",
        "2.11",
        "3.8"
        ]

}

MAP_VERSION_TO_INSTALL_NETTY = {
    k: {
   "java": 'apt-get update &&apt-get install autoconf automake libtool make tar gcc -y && curl -s "https://get.sdkman.io" | bash && source "$HOME/.sdkman/bin/sdkman-init.sh" &&  sdk install java 8.0.382-tem && sdk install maven && mvn --version',
    }

    #version 
    for k in [
        "3.3",
        "4.0",
        "4.1",
        "5.0"
        ]
}

MAP_VERSION_TO_INSTALL_ASSERTJ = {
    k: {
       "java": 'curl -s "https://get.sdkman.io" | bash && source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 19.0.2-open && sdk install maven 3.9.4 && mvn --version',
    }

    for k in [
        "3.24",
        "3.25",
        "3.26",
        "2.2"
        ]
}

MAP_VERSION_TO_INSTALL_ASSERTJ.update({
    k: {
       "java": 'curl -s "https://get.sdkman.io" | bash && source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 11.0.20.1-tem && sdk install maven 3.9.4 && mvn --version',
       }


    for k in [
        "3.11",
        "3.12",
        "3.13",
        "3.14",
        "3.15",
        "3.16",
        "3.17",
        "3.18",
        "3.19",
        "3.21",
        ]
})

MAP_VERSION_TO_INSTALL_ASSERTJ.update({
    k: {
      "java": 'curl -s "https://get.sdkman.io" | bash && source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 8.0.382-tem && sdk install maven 3.9.4 && mvn --version',


    }

   
    for k in [
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
        "2.3",
        "2.8",
        "2.9",
        "3.5",
        "3.6",
        "3.8",
        "3.9",
        "3.10"
        ]
})






MAP_VERSION_TO_INSTALL_DAYJS = {
    k: {

        "nodejs": "20.1.0",
        'setup_command':['npm install']

    }

    for k in [
        "1.11",
        ]
}

MAP_VERSION_TO_INSTALL_DAYJS.update(  {
    k: {

    "nodejs": "12.20.0",

        'setup_command':['npm install']
      
    }

    for k in [
        "1.10"
        ]
})

MAP_VERSION_TO_INSTALL_DAYJS.update(  {
    k: {

    "nodejs": "12.20.0",

        'setup_command':['npm install']
       
    }

  
    for k in [
       '1.8', "1.9"
        ]
})

# MAP_VERSION_TO_INSTALL_DAYJS.update(  {
#     k: {

#     "nodejs": "12.20.0",

#         'setup_command':['npm install']
      
#     }


#     for k in [
#         "1.8"
#         ]
# })


MAP_VERSION_TO_INSTALL_BABEL = {
    k: {
  
        "nodejs": "20.17.0",
        'setup_command':['volta install yarn','make bootstrap','make build']
    }

    #version 
    for k in [
           
        "7.12",
        "7.13",
        "7.14",
        "7.15",
        "7.16",
        "7.17",
        "7.18",
        "7.19",
        "7.20",
        "7.21",
        "7.22",
        "7.23",
        "7.24",
        "7.25"
        ]
}




MAP_VERSION_TO_INSTALL_JEST = {
    k: {
     
        "nodejs": "20.1.0",
        'apt':['apt-get update ','apt-get -y install mercurial'],
        'setup_command': ['volta install yarn','yarn install','yarn build'],

    }

    #version 
    for k in [
                "23.6",
        "24.0",
        "24.1",
        "24.3",
        "24.5",
        "24.6",
        "24.7",
        "24.8",
        "24.9",
        "25.1",
        "25.2",
        "25.3",
        "25.4",
        "25.5",
        "26.0",
        "26.1",
        "26.2",
        "26.3",
        "26.4",
        "26.5",
        "26.6",
        "27.0",
        "27.1",
        "27.2",
        "27.3",
        "27.4",
        "27.5",
        "28.0",
        "28.1",
        "29.0",
        "29.1",
        "29.2",
        "29.3",
        "29.4",
        "29.5",
        "29.6",
        "29.7",
        "30.0"
        ]
}




MAP_VERSION_TO_INSTALL_TAILWINDCSS= {
    k: {
        #env building
        "nodejs": "20.1.0",

 
        'apt':['apt-get update',
        'apt-get -y install cargo ',
            ],
        'setup_command':['npm install']
       
    }

    #version 
    for k in [
           
     
        "3.0",
        "3.1",
        "3.2",
        "3.3",
        '3.4'
        ]
}

MAP_VERSION_TO_INSTALL_TAILWINDCSS.update( {
    k: {
        #env building
        "nodejs": "12.22.3 ",

        'apt':['apt-get update',
        'apt-get -y install cargo ',
            ],
        'setup_command':['npm install']

    }

    #version 
    for k in [    
        "1.0",
        "1.1",
        "1.2",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
        "1.8",
        "1.9",
        "2.0",
        "2.1",
        "2.2",
        ]
})


MAP_VERSION_TO_INSTALL_WEBPACK = {
    k: {

        "nodejs": "20.1.0",

        'setup_command':['volta install yarn','yarn','yarn link','ls node_modules/.bin/jest']

    }

    #version 
    for k in [
        "5.80",
        "5.81",
        "5.82",
        "5.83",
        "5.84",
        "5.85",
        "5.86",
        "5.88",
        "5.89",
        "5.90",
        "5.91",
        "5.92"
        ]
}
MAP_VERSION_TO_INSTALL_WEBPACK.update(
    {
        k: {

        "nodejs": "20.1.0 ",

        
        'setup_command':['volta install yarn','yarn','yarn link','ls node_modules/.bin/jest','npx browserslist',"sed -i 's/\"maintained node versions\"/\"node 12\"/' test/configCases/ecmaVersion/browserslist/package.json"]

    }
    for k in [
        "5.1",
        "5.2",
        "5.3",
        "5.4",
        "5.9",
        "5.10",
        "5.11",
        "5.13",
        "5.14",
        "5.15",
        "5.16",
        "5.19",
        "5.20",
        "5.21",
        "5.23",
        "5.24",
        "5.25",
        "5.26",
        "5.27",
        "5.30",
        "5.32",
        "5.33",
        "5.35",
        "5.36",
        "5.37",
        "5.39",
        "5.41",
        "5.42",
        "5.43",
        "5.45",
        "5.46",
        "5.48",
        "5.50",
        "5.51",
        "5.52",
        "5.58",
        "5.59",
        "5.60",
        "5.61",
        "5.62",
        "5.63",
        "5.64",
        "5.65",
        "5.66",
        "5.67",
        "5.68",
        "5.69",
        "5.70",
        "5.71",
        "5.72",
        "5.73",
        "5.74",
        "5.75",
        "5.76",
        "5.78",

        "5.92"
        ]

    }
)

MAP_VERSION_TO_INSTALL_PRETTIER = {
    k: {

        "nodejs": "20.1.0",


        'setup_command':['volta install yarn','export PATH=$(yarn bin):$PATH','yarn install','ls node_modules/.bin/jest']
 
    }

    #version 
    for k in [
        '3.3',
        '3.4',
        "3.0",
        "3.1",
        "3.2",
        ]
}

MAP_VERSION_TO_INSTALL_PRETTIER.update( {
    k: {
        "nodejs": "20.1.0",
        'setup_command':['volta install yarn','export PATH=$(yarn bin):$PATH','yarn install','ls node_modules/.bin/jest']
        
    }

    #version 
    for k in [
        "1.9",
        "1.10",
        "1.11",
        "1.12",
        "1.13",
        "1.14",
        "1.15",
        "1.16",
        "1.17",
        "1.18",
        "1.19",
        "1.20",
        "2.0",
        "2.1",
        "2.2",
        "2.3",
        "2.4",
        "2.5",
        "2.6",
        "2.7",
        "2.8",
        "2.9",
        
        ]
})


MAP_VERSION_TO_INSTALL_TQDM = {
    k: {
        "python": "3.8",
        "install": "pip install --upgrade pip && pip install setuptools_scm && pip install -e .&& python -c 'import setuptools_scm; print(setuptools_scm.get_version())' ",
      
    }
    for k in [
  'get_version'
       
       
        
        ]
}
MAP_VERSION_TO_INSTALL_TQDM.update( {
    k: {
        "python": "3.7",
         "install": "pip install --upgrade pip  && pip install -e .[dev]",
        "pip_packages": ["pytest",'pytest-asyncio','numpy','nose','pandas','keras']
    }

    for k in [
      "4.7",
        "4.9",
        "4.10",
        "4.11",
        "4.14",
        "4.17",
        "4.20",
        "4.24",
        "4.26",
        "4.28",
          "4.30",
        "4.31",
        "4.33",
        "4.34",
        "4.35",
        "4.36",
        "4.37",
        "4.38",
          "4.39",
          "4.40",
        "4.41",
        "4.42",
        "4.43",
        "4.45",
        "4.46",
        "4.47",
        "4.48",
        "4.49",
        "4.50",
        "4.51",
        "4.52"
        
        ]
})

MAP_VERSION_TO_INSTALL_TQDM.update( {
    k: {
        "python": "3.7",
         "install": "pip install --upgrade pip  && pip install -e .[dev]",
        "pip_packages": ["pytest",'pytest-asyncio','numpy','nose','pandas==0.25.3','keras']
    }

    for k in [
   
          "4.40"
      
        
        ]
})

MAP_VERSION_TO_INSTALL_TQDM.update( {
    k: {
        "python": "3.6  ",
         "install": "pip install --upgrade pip  && pip install -e .[dev]",
        "pip_packages": ["pytest",'pytest-asyncio','nose','pandas==0.23.0']
    }

    for k in [
        '4.251'  
        ]
})

MAP_VERSION_TO_INSTALL_TQDM.update( {
    k: {
        "python": "3.6",
         "install": "pip install --upgrade pip  && pip install -e .[dev]",
        "pip_packages": ["pytest",'pytest-asyncio','nose','pandas==0.18.0']
    }

    for k in [
   
        '4.7'
      
        
        ]
})

MAP_VERSION_TO_INSTALL_TQDM.update( {
    k: {
        "python": "3.6  ",
         "install": "pip install --upgrade pip  && pip install -e .[dev]",
        "pip_packages": ["pytest",'pytest-asyncio','nose','pandas==0.21.1']
    }

    for k in [
   
        '4.25','4.22','4.19'
      
        
        ]
})




MAP_VERSION_TO_INSTALL_REDIS= {
    k: {
        "python": "3.8",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        'apt':['apt-get update','apt-get install -y \
            build-essential \
            tcl \
            wget',
        'wget http://download.redis.io/releases/redis-7.2.0.tar.gz',
        'tar xzf redis-7.2.0.tar.gz',
        'cd redis-7.2.0',
        'make',
        'make install',
        'cd ..'
        # 'apt-get install -y curl gnupg lsb-release',
        # 'curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg',
        # 'echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list',
            # 'apt-get install -y redis-server=7.0.*',
                 ],
        'extra_command':['redis-server --port 6379 --enable-debug-command yes --enable-module-command yes --protected-mode no &',
            'redis-server --port 6380 --replicaof 127.0.0.1 6379 --protected-mode no &',
            'redis-server --port 6479 --enable-debug-command yes --enable-module-command yes &',
            'redis-server --port 36379 --enable-debug-command yes --enable-module-command yes &',
            'redis-server --port 16379 --cluster-enabled yes --cluster-config-file nodes-16379.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16380 --cluster-enabled yes --cluster-config-file nodes-16380.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16381 --cluster-enabled yes --cluster-config-file nodes-16381.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16382 --cluster-enabled yes --cluster-config-file nodes-16382.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16383 --cluster-enabled yes --cluster-config-file nodes-16383.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16384 --cluster-enabled yes --cluster-config-file nodes-16384.conf --cluster-node-timeout 5000  --protected-mode no &',
            
            # 'redis-sentinel ./dockers/sentinel.conf --port 26379 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26380 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26381 &',
            'redis-server --port 6480 &'


                        #  'redis-server --port 36379 &',
                        #  'redis-server --port 6380 &'
        ],
        "install": "pip install --upgrade pip && pip install -r dev_requirements.txt && pip install -r requirements.txt  && pip install -e .[hiredis,ocsp]",
        # "pip_packages": ["hiredis"]
    }
    for k in [
   
        '5.0','5.1'

        ]
}

MAP_VERSION_TO_INSTALL_REDIS.update( {
    k: {
        "python": "3.8",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        'apt':['apt-get update','apt-get install -y \
            build-essential \
            tcl \
            wget',
        
        'wget http://download.redis.io/releases/redis-7.2.1.tar.gz',
        'tar xzf redis-7.2.1.tar.gz',
        'cd redis-7.2.1',
        'make',
        'make install',
        'cd ..'
        # 'apt-get install -y curl gnupg lsb-release',
        # 'curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg',
        # 'echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list',
            # 'apt-get install -y redis-server=7.0.*',
                 ],
        'extra_command':['redis-server --port 6379 --enable-debug-command yes --enable-module-command yes --protected-mode no &',
            'redis-server --port 6380 --replicaof 127.0.0.1 6379 --protected-mode no &',
            'redis-server --port 6479 --enable-debug-command yes --enable-module-command yes &',
            'redis-server --port 36379 --enable-debug-command yes --enable-module-command yes &',
            'redis-server --port 16379 --cluster-enabled yes --cluster-config-file nodes-16379.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16380 --cluster-enabled yes --cluster-config-file nodes-16380.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16381 --cluster-enabled yes --cluster-config-file nodes-16381.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16382 --cluster-enabled yes --cluster-config-file nodes-16382.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16383 --cluster-enabled yes --cluster-config-file nodes-16383.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16384 --cluster-enabled yes --cluster-config-file nodes-16384.conf --cluster-node-timeout 5000  --protected-mode no &',
            
            # 'redis-sentinel ./dockers/sentinel.conf --port 26379 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26380 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26381 &',
            'redis-server --port 6480 &','df -h'


                        #  'redis-server --port 36379 &',
                        #  'redis-server --port 6380 &'
        ],
        "install": "pip install --upgrade pip && pip install -r dev_requirements.txt && pip install -r requirements.txt  && pip install -e .[hiredis,ocsp]",
        # "pip_packages": ["hiredis"]
    }
    for k in [
   
        "4.5", '4.4','4.3','4.2','4.1','4.0'
        ]
})

MAP_VERSION_TO_INSTALL_REDIS.update( {
    k: {
        "python": "3.8",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        'apt':['apt-get update','apt-get install -y \
            build-essential \
            tcl \
            wget \
             pkg-config',
        'wget http://download.redis.io/releases/redis-6.2.6.tar.gz',
        'tar xzf redis-6.2.6.tar.gz',
        'cd redis-6.2.6',
        'make',
        'make install',
        'cd ..'
        # 'apt-get install -y curl gnupg lsb-release',
        # 'curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg',
        # 'echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/redis.list',
            # 'apt-get install -y redis-server=7.0.*',
                 ],
        'extra_command':['redis-server --port 6379  --protected-mode no &',
            'redis-server --port 6380 --replicaof 127.0.0.1 6379 --protected-mode no &',
            'redis-server --port 6378  --protected-mode no &',
            'redis-server --port 6479  --protected-mode no &',
            'redis-server --port 36379  --protected-mode no &',
            'redis-server --port 16379  --cluster-enabled yes --cluster-config-file nodes-16379.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16380  --cluster-enabled yes --cluster-config-file nodes-16380.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16381  --cluster-enabled yes --cluster-config-file nodes-16381.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16382 --cluster-enabled yes  --cluster-config-file nodes-16382.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16383  --cluster-enabled yes --cluster-config-file nodes-16383.conf --cluster-node-timeout 5000  --protected-mode no &',
            'redis-server --port 16384   --cluster-enabled yes --cluster-config-file nodes-16384.conf --cluster-node-timeout 5000  --protected-mode no &',
            
            # 'redis-sentinel ./dockers/sentinel.conf --port 26379 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26380 &',
            # 'redis-sentinel ./dockers/sentinel.conf --port 26381 &',
            'redis-server --port 6480 &'


                        #  'redis-server --port 36379 &',
                        #  'redis-server --port 6380 &'
        ],
        "install": "pip install --upgrade pip && pip install -r dev_requirements.txt && pip install -r requirements.txt  && pip install -e .[hiredis,ocsp]",
        # "pip_packages": ["hiredis"]
    }
    for k in [
   
       ''


        ]
})


MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY = {
    k: {
        "python": "3.8",
        'apt':['apt-get update','conda  install -y openssl=1.1.1* ',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",
    }
    for k in ["35.0"]
}

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update({
    k: {
        "python": "3.8",
        'apt':['apt-get update','conda  install -y openssl=3.0.2 ', 'conda install bcrypt',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",
       
    }
    for k in ["37.0"]
})

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update({
    k: {
        "python": "3.8",

        'apt':['apt-get update','conda  install -y openssl=3.0.2', 'conda install bcrypt',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",

    }
    for k in ["36.0"]
})

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update({
    k: {
        "python": "3.8",

        'apt':['apt-get update','conda  install -y openssl=3.0.5 ',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",

    }
    for k in ["38.0"]
})

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update({
    k: {
        "python": "3.8",

        'apt':['apt-get update','conda  install -y openssl=3.0.2 ',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",

    }
    for k in ["39.0"]
})



MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update({
    k: {
        "python": "3.8",

        'apt':['apt-get update','conda  install -y openssl=3.1.* ',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -e .[test,docs,docstest,pep8test] && pip install -e vectors && pip install -r ci-constraints-requirements.txt && pip install -e . &&openssl version",
        "pip_packages": ["tox"]
    }
    for k in ["40.0",'41.0','42.0','43.0']
})
MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update( {
    k: {
        "python": "3.6",

        'apt':['apt-get update','conda  install -y openssl=1.1.*',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",

    }
    for k in ["3.1",'3.2','3.3','3.4']
})

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update( {
    k: {
        "python": "3.6",

        'apt':['apt-get update','conda  install -y openssl=1.0.*',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",

    }
    for k in ["3.0",'2.9','2.8','2.7','2.6','2.5']
})

MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.update( {
    k: {
        "python": "3.6",
        'apt':['apt-get update','conda  install -y openssl=1.0.*',
               'apt-get -y install build-essential libssl-dev libffi-dev python3-dev cargo rustc',
                 ],
        "install": "pip install --upgrade pip && pip install -r dev-requirements.txt && pip install -e . &&openssl version",
        "pip_packages": ["pytest==3.7.4","hypothesis==6.0.0"]
    }
    for k in ['2.4','2.3','2.2','2.1','2.0','1.9']
})


MAP_VERSION_TO_INSTALL_STATSMODELS={
    k: {
        "python": "3.9.12",
        "install": "pip install --upgrade pip && sed -i '/oldest-supported-numpy/d' requirements-dev.txt && pip install -r requirements-dev.txt && pip install -e .",
        "pip_packages": ["numpy==1.24.3", "pandas==2.0.3", "scipy==1.10.1"]
    }
    for k in ["0.14",'0.13']
}

setup_stats_13="""cat <<EOL > requirements-temp.txt
cython==0.29.34
setuptools==59.2.0
numpy==1.19.3
pandas==1.1.5
scipy==1.5.4
matplotlib==3.3.4
colorama==0.4.4
joblib==1.1.0
pytest==6.2.5
pytest-randomly==3.12.0
pytest-xdist==3.2.0
flake8==3.9.2
isort==5.9.3
sphinx==4.2.0
sphinx-material==0.0.36
jupyter==1.0.0
notebook==6.4.4
nbsphinx==0.8.7
nbconvert==6.1.0
pyyaml==5.4.1
pandas-datareader==0.9.0
simplegeneric==0.8.1
seaborn==0.11.2
numpydoc==1.1.0
theano-pymc==1.0.11
pymc3==3.9
arviz==0.11.4
EOL"""

MAP_VERSION_TO_INSTALL_STATSMODELS.update({
    k: {
        "python": "3.8",
        "install": f"pip install --upgrade pip && eval \"{setup_stats_13}\" && pip install -r requirements-temp.txt && python setup.py develop",
       
    }
    for k in ['0.13dev','0.12']
})


MAP_VERSION_TO_INSTALL_DATEUTIL = {
    k: {
        "python": "3.5",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -e . && python updatezinfo.py",
        "pip_packages": ["tox"]
    }
    for k in ["2.5"]
}


MAP_VERSION_TO_INSTALL_DATEUTIL.update({
         k: {
        "python": "3.6",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -e . && python updatezinfo.py",
        "pip_packages": ["tox","freezegun==0.3.10"]
    }
    for k in ['2.6']
    })
extra_command = 'echo "[pytest]\nmarkers = import_star tzstr rrule tzoffset isoparser parserinfo" > pytest.ini'
MAP_VERSION_TO_INSTALL_DATEUTIL.update({
         k: {
        "python": "3.7",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": f"pip install -r requirements-dev.txt && pip install -e . && python updatezinfo.py && {extra_command}",
        # "pip_packages": []
    }
    for k in ['2.7']
    })


MAP_VERSION_TO_INSTALL_MYPY = {
    k: {
        "python": "3.7",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -r test-requirements.txt && pip install -e . ",
        "pip_packages": ["pytest==6.2.5","typing_extensions==3.10"]
    }
    for k in ["0.920","0.940","0.950","0.960","0.970","0.980","0.990",'1.0','1.1','1.2','1.4']
}

MAP_VERSION_TO_INSTALL_MYPY.update({
    k: {
        "python": "3.10",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -r test-requirements.txt && pip install -e . ",
        "pip_packages": ["pytest==6.2.5","typing_extensions==3.10"]
    }
    for k in ['1.3']
})

MAP_VERSION_TO_INSTALL_MYPY.update(
    {
        k: {
        # "python": "3.7",
        "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -r test-requirements.txt && pip install -e . ",
        "pip_packages": ["pytest==7.4.0","typing_extensions==4.1.0"]
        }
        for k in ['1.5','1.6','1.7']
    }
)
MAP_VERSION_TO_INSTALL_MYPY.update(
    {
        k: {
        "python": "3.7",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -r test-requirements.txt && pip install -e . ",
        "pip_packages": ["typing_extensions==4.6.0"]
        }
        for k in ['1.8','1.9','1.10','1.11']
    }
)
MAP_VERSION_TO_INSTALL_MYPY.update(
    {
        k: {
        "python": "3.5",
        # "python": "3.10.6",
        # "packages": "requirements.txt",
        "install": "pip install -r test-requirements.txt && git submodule update --init mypy/typeshed && pip install -e . ",
        "pip_packages": ["pytest==6.1.0","typing_extensions==3.7.4","types-typing-extensions==3.7.1"]
        }
        for k in ['0.800','0.810','0.820']
    }
)

MAP_VERSION_TO_INSTALL_SKLEARN = {
    k: {
        "python": "3.6",
        "packages": "numpy scipy cython pytest pandas matplotlib",
        "install": "python -m pip install -v --no-use-pep517 --no-build-isolation -e .",
        "pip_packages": [
            "cython",
            "numpy==1.19.2",
            "setuptools",
            "scipy==1.5.2",
        ],
    }
    for k in ["0.20", "0.21", "0.22"]
}
MAP_VERSION_TO_INSTALL_SKLEARN.update(
    {
        k: {
            "python": "3.9",
            "packages": "numpy scipy cython setuptools pytest pandas matplotlib joblib threadpoolctl",
            "install": "python -m pip install -v --no-use-pep517 --no-build-isolation -e .",
            "pip_packages": ["cython", "setuptools", "numpy", "scipy"],
        }
        for k in ["1.3", "1.4",'1.5','1.6']
    }
)


MAP_VERSION_TO_INSTALL_FLASK = {
    "2.0": {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "setuptools==70.0.0",
            "Werkzeug==2.3.7",
            "Jinja2==3.0.1",
            "itsdangerous==2.1.2",
            "click==8.0.1",
            "MarkupSafe==2.1.3",
        ],
    },
    "2.1": {
        "python": "3.10",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "setuptools==70.0.0",
            "click==8.1.3",
            "itsdangerous==2.1.2",
            "Jinja2==3.1.2",
            "MarkupSafe==2.1.1",
            "Werkzeug==2.3.7",
        ],
    },
}
MAP_VERSION_TO_INSTALL_FLASK.update(
    {
        k: {
            "python": "3.11",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": [
                "setuptools==70.0.0",
                "click==8.1.3",
                "itsdangerous==2.1.2",
                "Jinja2==3.1.2",
                "MarkupSafe==2.1.1",
                "Werkzeug==2.3.7",
            ],
        }
        for k in ["2.2", "2.3",'3.0','3.1']
    }
)
MAP_VERSION_TO_INSTALL_DJANGO = {
    k: {
        "python": "3.5",
        "packages": "requirements.txt",
        "pre_install": [
            "apt-get update && apt-get install -y locales",
            "echo 'en_US UTF-8' > /etc/locale.gen",
            "locale-gen en_US.UTF-8",
        ],
        "install": "python setup.py install",
        "pip_packages": ["setuptools"],
        "eval_commands": [
            "export LANG=en_US.UTF-8",
            "export LC_ALL=en_US.UTF-8",
            "export PYTHONIOENCODING=utf8",
            "export LANGUAGE=en_US:en",
        ],
    }
    for k in ["1.7", "1.8", "1.9", "1.10", "1.11", "2.0", "2.1", "2.2"]
}
MAP_VERSION_TO_INSTALL_DJANGO.update(
    {
        k: {"python": "3.5", "install": "python setup.py install"}
        for k in ["1.4", "1.5", "1.6"]
    }
)
MAP_VERSION_TO_INSTALL_DJANGO.update(
    {
        k: {
            "python": "3.6",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "eval_commands": [
                "sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen",
                "export LANG=en_US.UTF-8",
                "export LANGUAGE=en_US:en",
                "export LC_ALL=en_US.UTF-8",
            ],
        }
        for k in ["3.0", "3.1", "3.2"]
    }
)
MAP_VERSION_TO_INSTALL_DJANGO.update(
    {
        k: {
            "python": "3.8",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
        }
        for k in ["4.0"]
    }
)
MAP_VERSION_TO_INSTALL_DJANGO.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
        }
        for k in ["4.1", "4.2"]
    }
)
MAP_VERSION_TO_INSTALL_DJANGO.update(
    {
        k: {
            "python": "3.11",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
        }
        for k in ["5.0"]
    }
)
MAP_VERSION_TO_INSTALL_REQUESTS = {
    k: {"python": "3.9", "packages": "pytest", "install": "python -m pip install ."}
    for k in ["0.7", "0.8", "0.9", "0.11", "0.13", "0.14", "1.1", "1.2", "2.0", "2.2"]
    + ["2.3", "2.4", "2.5", "2.7", "2.8", "2.9", "2.10", "2.11", "2.12", "2.17"]
    + ["2.18", "2.19", "2.22", "2.26", "2.25", "2.27", "3.0"]
}
MAP_VERSION_TO_INSTALL_SEABORN = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "contourpy==1.1.0",
            "cycler==0.11.0",
            "fonttools==4.42.1",
            "importlib-resources==6.0.1",
            "kiwisolver==1.4.5",
            "matplotlib==3.7.2",
            "numpy==1.25.2",
            "packaging==23.1",
            "pandas==1.3.5",  # 2.0.3
            "pillow==10.0.0",
            "pyparsing==3.0.9",
            "pytest",
            "python-dateutil==2.8.2",
            "pytz==2023.3.post1",
            "scipy==1.11.2",
            "six==1.16.0",
            "tzdata==2023.1",
            "zipp==3.16.2",
        ],
    }
    for k in ["0.11","0.9"]
}
MAP_VERSION_TO_INSTALL_SEABORN.update(
    {
        k: {
            "python": "3.9",
            "install": "python -m pip install -e .[dev]",
            "pip_packages": [
                "contourpy==1.1.0",
                "cycler==0.11.0",
                "fonttools==4.42.1",
                "importlib-resources==6.0.1",
                "kiwisolver==1.4.5",
                "matplotlib==3.7.2",
                "numpy==1.25.2",
                "packaging==23.1",
                "pandas==2.0.0",
                "pillow==10.0.0",
                "pyparsing==3.0.9",
                "pytest",
                "python-dateutil==2.8.2",
                "pytz==2023.3.post1",
                "scipy==1.11.2",
                "six==1.16.0",
                "tzdata==2023.1",
                "zipp==3.16.2",
            ],
        }
        for k in ["0.12", "0.13",'0.14']
    }
)
MAP_VERSION_TO_INSTALL_PYTEST = {
    k: {"python": "3.9", "install": "python -m pip install -e ."}
    for k in [
        "4.4",
        "4.5",
        "4.6",
        "5.0",
        "5.1",
        "5.2",
        "5.3",
        "5.4",
        "6.0",
        "6.2",
        "6.3",
        "7.0",
        "7.1",
        "7.2",
        "7.4",
        "8.0",
    ]
}
MAP_VERSION_TO_INSTALL_PYTEST["4.4"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.13.1",
    "py==1.11.0",
    "setuptools==68.0.0",
    "six==1.16.0",
]
MAP_VERSION_TO_INSTALL_PYTEST["4.5"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.11.0",
    "py==1.11.0",
    "setuptools==68.0.0",
    "six==1.16.0",
    "wcwidth==0.2.6",
]
MAP_VERSION_TO_INSTALL_PYTEST["4.6"]["pip_packages"] = [
    "atomicwrites==1.4.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "six==1.16.0",
    "wcwidth==0.2.6",
]
for k in ["5.0", "5.1", "5.2"]:
    MAP_VERSION_TO_INSTALL_PYTEST[k]["pip_packages"] = [
        "atomicwrites==1.4.1",
        "attrs==23.1.0",
        "more-itertools==10.1.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "wcwidth==0.2.6",
    ]
MAP_VERSION_TO_INSTALL_PYTEST["5.3"]["pip_packages"] = [
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "wcwidth==0.2.6",
]
MAP_VERSION_TO_INSTALL_PYTEST["5.4"]["pip_packages"] = [
    "py==1.11.0",
    "packaging==23.1",
    "attrs==23.1.0",
    "more-itertools==10.1.0",
    "pluggy==0.13.1",
]
MAP_VERSION_TO_INSTALL_PYTEST["6.0"]["pip_packages"] = [
    "attrs==23.1.0",
    "iniconfig==2.0.0",
    "more-itertools==10.1.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
    "toml==0.10.2",
]
for k in ["6.2", "6.3"]:
    MAP_VERSION_TO_INSTALL_PYTEST[k]["pip_packages"] = [
        "attrs==23.1.0",
        "iniconfig==2.0.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "toml==0.10.2",
    ]
MAP_VERSION_TO_INSTALL_PYTEST["7.0"]["pip_packages"] = [
    "attrs==23.1.0",
    "iniconfig==2.0.0",
    "packaging==23.1",
    "pluggy==0.13.1",
    "py==1.11.0",
]
for k in ["7.1", "7.2"]:
    MAP_VERSION_TO_INSTALL_PYTEST[k]["pip_packages"] = [
        "attrs==23.1.0",
        "iniconfig==2.0.0",
        "packaging==23.1",
        "pluggy==0.13.1",
        "py==1.11.0",
        "tomli==2.0.1",
    ]
MAP_VERSION_TO_INSTALL_PYTEST["7.4"]["pip_packages"] = [
    "iniconfig==2.0.0",
    "packaging==23.1",
    "pluggy==1.3.0",
    "exceptiongroup==1.1.3",
    "tomli==2.0.1",
]
MAP_VERSION_TO_INSTALL_PYTEST["8.0"]["pip_packages"] = [
    "iniconfig==2.0.0",
    "packaging==23.1",
    "pluggy==1.3.0",
    "exceptiongroup==1.1.3",
    "tomli==2.0.1",
]
MAP_VERSION_TO_INSTALL_MATPLOTLIB = {
    k: {
        "python": "3.11",
        "packages": "environment.yml",
        "install": "python -m pip install -e .",
        "pre_install": [
            "apt-get -y update && apt-get -y upgrade && apt-get install -y imagemagick ffmpeg texlive texlive-latex-extra texlive-fonts-recommended texlive-xetex texlive-luatex cm-super dvipng"
        ],
        "pip_packages": [
            "contourpy==1.1.0",
            "cycler==0.11.0",
            "fonttools==4.42.1",
            "ghostscript",
            "kiwisolver==1.4.5",
            "numpy==1.25.2",
            "packaging==23.1",
            "pillow==10.0.0",
            "pikepdf",
            "pyparsing==3.0.9",
            "python-dateutil==2.8.2",
            "six==1.16.0",
            "setuptools==68.1.2",
            "setuptools-scm==7.1.0",
            "typing-extensions==4.7.1",
        ],
    }
    for k in ["3.5", "3.6", "3.7"]
}
MAP_VERSION_TO_INSTALL_MATPLOTLIB.update(
    {
        k: {
            "python": "3.8",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && apt-get install -y imagemagick ffmpeg libfreetype6-dev pkg-config texlive texlive-latex-extra texlive-fonts-recommended texlive-xetex texlive-luatex cm-super"
            ],
            "pip_packages": ["pytest", "ipython"],
        }
        for k in ["3.1", "3.2", "3.3", "3.4"]
    }
)
MAP_VERSION_TO_INSTALL_MATPLOTLIB.update(
    {
        k: {
            "python": "3.7",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && apt-get install -y imagemagick ffmpeg libfreetype6-dev pkg-config"
            ],
            "pip_packages": ["pytest"],
        }
        for k in ["3.0"]
    }
)
MAP_VERSION_TO_INSTALL_MATPLOTLIB.update(
    {
        k: {
            "python": "3.5",
            "install": "python setup.py build; python setup.py install",
            "pre_install": [
                "apt-get -y update && apt-get -y upgrade && && apt-get install -y imagemagick ffmpeg"
            ],
            "pip_packages": ["pytest"],
            "execute_test_as_nonroot": True,
        }
        for k in ["2.0", "2.1", "2.2", "1.0", "1.1", "1.2", "1.3", "1.4", "1.5"]
    }
)
MAP_VERSION_TO_INSTALL_SPHINX = {
    k: {
        "python": "3.9",
        "pip_packages": ["tox"],
        "install": "python -m pip install -e .[test]",
        "pre_install": ["sed -i 's/pytest/pytest -rA/' tox.ini"],
    }
    for k in ["1.5", "1.6", "1.7", "1.8", "2.0", "2.1", "2.2", "2.3", "2.4", "3.0"]
    + ["3.1", "3.2", "3.3", "3.4", "3.5", "4.0", "4.1", "4.2", "4.3", "4.4"]
    + ["4.5", "5.0", "5.1", "5.2", "5.3", "6.0", "6.2", "7.0", "7.1", "7.2"]
}
for k in ["3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "4.0", "4.1", "4.2", "4.3", "4.4"]:
    MAP_VERSION_TO_INSTALL_SPHINX[k][
        "pre_install"
    ].extend([
        "sed -i 's/Jinja2>=2.3/Jinja2<3.0/' setup.py",
        "sed -i 's/sphinxcontrib-applehelp/sphinxcontrib-applehelp<=1.0.7/' setup.py",
        "sed -i 's/sphinxcontrib-devhelp/sphinxcontrib-devhelp<=1.0.5/' setup.py",
        "sed -i 's/sphinxcontrib-qthelp/sphinxcontrib-qthelp<=1.0.6/' setup.py",
        "sed -i 's/alabaster>=0.7,<0.8/alabaster>=0.7,<0.7.12/' setup.py",
        'sed -i "s/\'packaging\',/\'packaging\', \'markupsafe<=2.0.1\',/" setup.py',
    ])
    if k in ["4.2", "4.3", "4.4"]:
        MAP_VERSION_TO_INSTALL_SPHINX[k]["pre_install"].extend([
            "sed -i 's/sphinxcontrib-htmlhelp>=2.0.0/sphinxcontrib-htmlhelp>=2.0.0,<=2.0.4/' setup.py",
            "sed -i 's/sphinxcontrib-serializinghtml>=1.1.5/sphinxcontrib-serializinghtml>=1.1.5,<=1.1.9/' setup.py",
        ])
    elif k == "4.1":
        MAP_VERSION_TO_INSTALL_SPHINX[k]["pre_install"].extend([
            (
                "grep -q 'sphinxcontrib-htmlhelp>=2.0.0' setup.py && "
                "sed -i 's/sphinxcontrib-htmlhelp>=2.0.0/sphinxcontrib-htmlhelp>=2.0.0,<=2.0.4/' setup.py || "
                "sed -i 's/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp<=2.0.4/' setup.py"
            ),
            (
                "grep -q 'sphinxcontrib-serializinghtml>=1.1.5' setup.py && "
                "sed -i 's/sphinxcontrib-serializinghtml>=1.1.5/sphinxcontrib-serializinghtml>=1.1.5,<=1.1.9/' setup.py || "
                "sed -i 's/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml<=1.1.9/' setup.py"
            )
        ])
    else:
        MAP_VERSION_TO_INSTALL_SPHINX[k]["pre_install"].extend([
            "sed -i 's/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp<=2.0.4/' setup.py",
            "sed -i 's/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml<=1.1.9/' setup.py",
        ])
MAP_VERSION_TO_INSTALL_SPHINX["7.2"]["pre_install"] += [
    "apt-get update && apt-get install -y graphviz"
]
MAP_VERSION_TO_INSTALL_ASTROPY = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .[test] --verbose",
        "pip_packages": [
            "attrs==23.1.0",
            "exceptiongroup==1.1.3",
            "execnet==2.0.2",
            "hypothesis==6.82.6",
            "iniconfig==2.0.0",
            "numpy==1.25.2",
            "packaging==23.1",
            "pluggy==1.3.0",
            "psutil==5.9.5",
            "pyerfa==2.0.0.3",
            "pytest-arraydiff==0.5.0",
            "pytest-astropy-header==0.2.2",
            "pytest-astropy==0.10.0",
            "pytest-cov==4.1.0",
            "pytest-doctestplus==1.0.0",
            "pytest-filter-subpackage==0.1.2",
            "pytest-mock==3.11.1",
            "pytest-openfiles==0.5.0",
            "pytest-remotedata==0.4.0",
            "pytest-xdist==3.3.1",
            "pytest==7.4.0",
            "PyYAML==6.0.1",
            "setuptools==68.0.0",
            "sortedcontainers==2.4.0",
            "tomli==2.0.1",
        ],
    }
    for k in ["0.1", "0.2", "0.3", "0.4", "1.1", "1.2", "1.3", "3.0", "3.1", "3.2"]
    + ["4.1", "4.2", "4.3", "5.0", "5.1", "5.2"]
}
for k in ["4.1", "4.2", "4.3", "5.0", "5.1", "5.2"]:
    MAP_VERSION_TO_INSTALL_ASTROPY[k]["pre_install"] = [
        'sed -i \'s/requires = \\["setuptools",/requires = \\["setuptools==68.0.0",/\' pyproject.toml'
    ]
MAP_VERSION_TO_INSTALL_SYMPY = {
    k: {
        "python": "3.9",
        "packages": "mpmath flake8",
        "pip_packages": ["mpmath==1.3.0", "flake8-comprehensions"],
        "install": "python -m pip install -e .",
    }
    for k in ["0.7", "1.0", "1.1", "1.10", "1.11", "1.12", "1.2", "1.4", "1.5", "1.6"]
    + ["1.7", "1.8", "1.9"]
}
MAP_VERSION_TO_INSTALL_SYMPY.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": ["mpmath==1.3.0"],
        }
        for k in ["1.13"]
    }
)
MAP_VERSION_TO_INSTALL_PYLINT = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
    }
    for k in [
        "2.10",
        "2.11",
        "2.13",
        "2.14",
        "2.15",
        "2.16",
        "2.17",
        "2.8",
        "2.9",
        "3.0",
    ]
}
MAP_VERSION_TO_INSTALL_PYLINT["2.8"]["pip_packages"] = ["pyenchant==3.2"]
MAP_VERSION_TO_INSTALL_PYLINT["2.8"]["pre_install"] = [
    "apt-get update && apt-get install -y libenchant-2-dev hunspell-en-us"
]
MAP_VERSION_TO_INSTALL_PYLINT.update(
    {
        k: {
            **MAP_VERSION_TO_INSTALL_PYLINT[k],
            "pip_packages": ["astroid==3.0.0a6", "setuptools"],
        }
        for k in ["3.0"]
    }
)
for v in ["2.14", "2.15", "2.17", "3.0"]:
    MAP_VERSION_TO_INSTALL_PYLINT[v]["nano_cpus"] = int(2e9)
for v in ["4.49",'4.37']:
    MAP_VERSION_TO_INSTALL_TQDM[v]["nano_cpus"] = int(2e9)
MAP_VERSION_TO_INSTALL_XARRAY = {
    k: {
        "python": "3.10",
        "packages": "environment.yml",
        "install": "python -m pip install -e .",
        "pip_packages": [
            "numpy==1.23.0",
            "packaging==23.1",
            "pandas==1.5.3",
            "pytest==7.4.0",
            "python-dateutil==2.8.2",
            "pytz==2023.3",
            "six==1.16.0",
            "scipy==1.11.1",
            "setuptools==68.0.0"
        ],
        "no_use_env": True,
    }
    for k in ["0.12", "0.18", "0.19", "0.20", "2022.03", "2022.06", "2022.09"]
}

MAP_VERSION_TO_INSTALL_SQLFLUFF = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
    }
    for k in [
        "0.10",
        "0.11",
        "0.12",
        "0.13",
        "0.4",
        "0.5",
        "0.6",
        "0.8",
        "0.9",
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "2.0",
        "2.1",
        "2.2",
    ]
}
MAP_VERSION_TO_INSTALL_DBT_CORE = {
    k: {
        "python": "3.9",
        "packages": "requirements.txt",
        "install": "python -m pip install -e .",
    }
    for k in [
        "0.13",
        "0.14",
        "0.15",
        "0.16",
        "0.17",
        "0.18",
        "0.19",
        "0.20",
        "0.21",
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
    ]
}
MAP_VERSION_TO_INSTALL_PYVISTA = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": ["pytest"],
    }
    for k in ["0.20", "0.21", "0.22", "0.23"]
}
MAP_VERSION_TO_INSTALL_PYVISTA.update(
    {
        k: {
            "python": "3.9",
            "packages": "requirements.txt",
            "install": "python -m pip install -e .",
            "pip_packages": ["pytest"],
        }
        for k in [
            "0.24",
            "0.25",
            "0.26",
            "0.27",
            "0.28",
            "0.29",
            "0.30",
            "0.31",
            "0.32",
            "0.33",
            "0.34",
            "0.35",
            "0.36",
            "0.37",
            "0.38",
            "0.39",
            "0.40",
            "0.41",
            "0.42",
            "0.43",
        ]
    }
)
MAP_VERSION_TO_INSTALL_ASTROID = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .",
        "pip_packages": ["pytest"],
    }
    for k in [
        "2.10",
        "2.12",
        "2.13",
        "2.14",
        "2.15",
        "2.16",
        "2.5",
        "2.6",
        "2.7",
        "2.8",
        "2.9",
        "3.0",
    ]
}
MAP_VERSION_TO_INSTALL_MARSHMALLOW = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e '.[dev]'",
    }
    for k in [
        "2.18",
        "2.19",
        "2.20",
        "3.0",
        "3.1",
        "3.10",
        "3.11",
        "3.12",
        "3.13",
        "3.15",
        "3.16",
        "3.19",
        "3.2",
        "3.4",
        "3.8",
        "3.9",
    ]
}
MAP_VERSION_TO_INSTALL_PVLIB = {
    k: {
        "python": "3.9",
        "install": "python -m pip install -e .[all]",
        "packages": "pandas scipy",
        "pip_packages": ["jupyter", "ipython", "matplotlib", "pytest", "flake8"],
    }
    for k in ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]
}
MAP_VERSION_TO_INSTALL_PYDICOM = {
    k: {"python": "3.6", "install": "python -m pip install -e .", "packages": "numpy","pip_packages": ["pytest"],}
    for k in [
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "2.0",
        "2.1",
        "2.2",
        "2.3",
        "2.4",
        "3.0",
    ]
}
MAP_VERSION_TO_INSTALL_PYDICOM.update(
    {k: {**MAP_VERSION_TO_INSTALL_PYDICOM[k], "python": "3.8"} for k in ["1.4", "2.0"]}
)
MAP_VERSION_TO_INSTALL_PYDICOM.update(
    {k: {**MAP_VERSION_TO_INSTALL_PYDICOM[k], "python": "3.9"} for k in ["2.1", "2.2"]}
)
MAP_VERSION_TO_INSTALL_PYDICOM.update(
    {k: {**MAP_VERSION_TO_INSTALL_PYDICOM[k], "python": "3.10"} for k in ["2.3"]}
)
MAP_VERSION_TO_INSTALL_PYDICOM.update(
    {k: {**MAP_VERSION_TO_INSTALL_PYDICOM[k], "python": "3.11"} for k in ["2.4", "3.0"]}
)
MAP_VERSION_TO_INSTALL_HUMANEVAL = {k: {"python": "3.9"} for k in ["1.0"]}

# Constants - Task Instance Instllation Environment
MAP_VERSION_TO_INSTALL = {
    "astropy/astropy": MAP_VERSION_TO_INSTALL_ASTROPY,
    "dbt-labs/dbt-core": MAP_VERSION_TO_INSTALL_DBT_CORE,
    "django/django": MAP_VERSION_TO_INSTALL_DJANGO,
    "matplotlib/matplotlib": MAP_VERSION_TO_INSTALL_MATPLOTLIB,
    "marshmallow-code/marshmallow": MAP_VERSION_TO_INSTALL_MARSHMALLOW,
    "mwaskom/seaborn": MAP_VERSION_TO_INSTALL_SEABORN,
    "pallets/flask": MAP_VERSION_TO_INSTALL_FLASK,
    "psf/requests": MAP_VERSION_TO_INSTALL_REQUESTS,
    "pvlib/pvlib-python": MAP_VERSION_TO_INSTALL_PVLIB,
    "pydata/xarray": MAP_VERSION_TO_INSTALL_XARRAY,
    "pydicom/pydicom": MAP_VERSION_TO_INSTALL_PYDICOM,
    "pylint-dev/astroid": MAP_VERSION_TO_INSTALL_ASTROID,
    "pylint-dev/pylint": MAP_VERSION_TO_INSTALL_PYLINT,
    "pytest-dev/pytest": MAP_VERSION_TO_INSTALL_PYTEST,
    "pyvista/pyvista": MAP_VERSION_TO_INSTALL_PYVISTA,
    "scikit-learn/scikit-learn": MAP_VERSION_TO_INSTALL_SKLEARN,
    "sphinx-doc/sphinx": MAP_VERSION_TO_INSTALL_SPHINX,
    "sqlfluff/sqlfluff": MAP_VERSION_TO_INSTALL_SQLFLUFF,
    "swe-bench/humaneval": MAP_VERSION_TO_INSTALL_HUMANEVAL,
    "sympy/sympy": MAP_VERSION_TO_INSTALL_SYMPY,
    "python/mypy": MAP_VERSION_TO_INSTALL_MYPY,
    'dateutil/dateutil':MAP_VERSION_TO_INSTALL_DATEUTIL,
    'statsmodels/statsmodels':MAP_VERSION_TO_INSTALL_STATSMODELS,
    'pyca/cryptography':MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY,
    'redis/redis-py':MAP_VERSION_TO_INSTALL_REDIS,
    'tqdm/tqdm':MAP_VERSION_TO_INSTALL_TQDM,
    'prettier/prettier':MAP_VERSION_TO_INSTALL_PRETTIER,
    'tailwindlabs/tailwindcss':MAP_VERSION_TO_INSTALL_TAILWINDCSS,
    'webpack/webpack':MAP_VERSION_TO_INSTALL_WEBPACK,
    'jestjs/jest':MAP_VERSION_TO_INSTALL_JEST,
    'babel/babel':MAP_VERSION_TO_INSTALL_BABEL,
    'iamkun/dayjs':MAP_VERSION_TO_INSTALL_DAYJS,
    'assertj/assertj':MAP_VERSION_TO_INSTALL_ASSERTJ,
    'netty/netty':MAP_VERSION_TO_INSTALL_NETTY,
    'google/gson':MAP_VERSION_TO_INSTALL_GSON,

}

# Constants - Repository Specific Installation Instructions
MAP_REPO_TO_INSTALL = {}

# Constants - Task Instance Test Frameworks
TEST_PYTEST = "pytest --no-header -rA --tb=no -p no:cacheprovider"
MAP_REPO_TO_TEST_FRAMEWORK = {

    'netty/netty':{
        k:(
            "mvn clean install && mvn test {pl_option} -Dtest="
            if k in["3.3"]   
            else(
                "mvn versions:set -DremoveSnapshot && mvn versions:commit && mvn clean install -DskipTests  && mvn test {pl_option} -Dtest="
            )
        )
        for k in MAP_VERSION_TO_INSTALL_NETTY.keys()
    },
    'google/gson':{k:"mvn clean install -DskipTests=true -Dmaven.test.failure.ignore=true && mvn clean test-compile && mvn -pl gson test -Dtest=" for k in MAP_VERSION_TO_INSTALL_GSON.keys()},
    'assertj/assertj':{
        k:(
            'mvn clean install -DskipTests && mvn -pl assertj-core test -Dtest=' 
            if k in ["3.24","3.25","3.26"]
            else (
                'mvn clean install -DskipTests && mvn test -Dtest=' 
              
            )
        )
        for k in MAP_VERSION_TO_INSTALL_ASSERTJ.keys()
    },
    'iamkun/dayjs': {k: " npm run test -- " for k in MAP_VERSION_TO_INSTALL_DAYJS.keys()},
    'babel/babel': {k: "make build && yarn jest " for k in MAP_VERSION_TO_INSTALL_BABEL.keys()},
    'jestjs/jest': {k:'yarn build && yarn jest'  for k in MAP_VERSION_TO_INSTALL_JEST.keys()},
    'webpack/webpack':{k:'yarn jest'  for k in MAP_VERSION_TO_INSTALL_WEBPACK.keys()},
    'tailwindlabs/tailwindcss': { 
        k: (
            'npm run build && npm run test' 
            if k in ['3.2', '3.3', '3.4'] 
            else (
                'npm run swcify && npm run test' 
                if k in ['3.1', '3.0'] 
                else 'npm run babelify && npm run test'
            )
        )
        for k in MAP_VERSION_TO_INSTALL_TAILWINDCSS.keys()
    },
    # "npm test"
    'prettier/prettier': {k: "yarn cross-env NODE_OPTIONS=--experimental-vm-modules jest --runInBand --verbose" for k in MAP_VERSION_TO_INSTALL_PRETTIER.keys()},
    'tqdm/tqdm':{k: "pytest --no-header -rA  --tb=no -p no:cacheprovider" for k in MAP_VERSION_TO_INSTALL_TQDM.keys()},
    "astropy/astropy": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_ASTROPY.keys()},
    "django/django": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_MARSHMALLOW.keys()
    },
     "statsmodels/statsmodels": {
        k: "pytest --no-header -rA --tb=long -p no:cacheprovider"
        # k: "ls & pytest --no-header -rA --tb=no -p no:cacheprovider -n0 "
        for k in MAP_VERSION_TO_INSTALL_STATSMODELS.keys()
    },
    "redis/redis-py": {
        k: "pytest --no-header -rA --tb=long -p no:cacheprovider"
        # k: "ls & pytest --no-header -rA --tb=no -p no:cacheprovider -n0 "
        for k in MAP_VERSION_TO_INSTALL_REDIS.keys()
    },
    "pyca/cryptography": {
        k: (
            "pytest -rA --tb=long -p no:cacheprovider -v" 
            if k in ['2.4','2.3','2.2','2.1','2.0','1.9']
            else "pytest --no-header -rA --tb=long -p no:cacheprovider" 
            if k.startswith('3.') or k.startswith('2.') 
            else "pytest --no-header -rA --tb=long -p no:cacheprovider -n4"
        )
        for k in MAP_VERSION_TO_INSTALL_CRYPTOGRAPHY.keys()
    },
    "python/mypy": {
        k: "pytest --no-header -rA --tb=no -p no:cacheprovider -n4"
        # k: "ls & pytest --no-header -rA --tb=no -p no:cacheprovider -n0 "
        for k in MAP_VERSION_TO_INSTALL_MYPY.keys()
    },

    "dateutil/dateutil": {
        "2.5":"python setup.py test", #"tox -epy35 -v --",#
        "2.6":"python setup.py test", #'tox -epy36 -v --',#
        
        "2.7": "python -m pytest --no-header -rA --tb=long -p no:cacheprovider",
        "2.8": "tox",
        "2.9": "tox",
    # Add more specific versions or ranges as needed
    },

    "marshmallow-code/marshmallow": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_MARSHMALLOW.keys()
    },
    "matplotlib/matplotlib": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_MATPLOTLIB.keys()
    },
    "mwaskom/seaborn": {
        k: "pytest --no-header -rA" for k in MAP_VERSION_TO_INSTALL_SEABORN.keys()
    },
    "pallets/flask": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_FLASK.keys()},
    "psf/requests": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_REQUESTS.keys()},
    "pvlib/pvlib-python": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_PVLIB.keys()},
    "pydata/xarray": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_XARRAY.keys()},
    "pydicom/pydicom": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_PYDICOM.keys()},
    "pylint-dev/astroid": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_ASTROID.keys()
    },
    "pylint-dev/pylint": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_PYLINT.keys()},
    "pytest-dev/pytest": {
        k: "pytest -rA" for k in MAP_VERSION_TO_INSTALL_PYTEST.keys()
    },
    "pyvista/pyvista": {k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_PYVISTA.keys()},
    "scikit-learn/scikit-learn": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_SKLEARN.keys()
    },
    "sphinx-doc/sphinx": {
        k: "tox -epy39 -v --" for k in MAP_VERSION_TO_INSTALL_SPHINX.keys()
    },
    "sqlfluff/sqlfluff": {
        k: TEST_PYTEST for k in MAP_VERSION_TO_INSTALL_SQLFLUFF.keys()
    },
    "swe-bench/humaneval": {
        k: "python" for k in MAP_VERSION_TO_INSTALL_HUMANEVAL.keys()
    },
    "sympy/sympy": {
        k: "PYTHONWARNINGS='ignore::UserWarning,ignore::SyntaxWarning' bin/test -C --verbose"
        for k in MAP_VERSION_TO_INSTALL_SYMPY.keys()
    },
}
MAP_REPO_TO_TEST_FRAMEWORK["django/django"]["1.9"] = "./tests/runtests.py --verbosity 2"

TEST_PYTEST_VERBOSE = "pytest -rA --tb=long -p no:cacheprovider"
MAP_REPO_TO_TEST_FRAMEWORK_VERBOSE = {
    "astropy/astropy": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_ASTROPY.keys()
    },
    "django/django": {
        k: "./tests/runtests.py --verbosity 2 --settings=test_sqlite --parallel 1"
        for k in MAP_VERSION_TO_INSTALL_DJANGO.keys()
    },
    "marshmallow-code/marshmallow": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_MARSHMALLOW.keys()
    },
    "matplotlib/matplotlib": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_MATPLOTLIB.keys()
    },
    "mwaskom/seaborn": {
        k: "pytest -rA --tb=long" for k in MAP_VERSION_TO_INSTALL_SEABORN.keys()
    },
    "pallets/flask": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_FLASK.keys()
    },
    "psf/requests": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_REQUESTS.keys()
    },
    "pvlib/pvlib-python": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_PVLIB.keys()
    },
    "pydata/xarray": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_XARRAY.keys()
    },
    "pydicom/pydicom": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_PYDICOM.keys()
    },
    "pylint-dev/astroid": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_ASTROID.keys()
    },
    "pylint-dev/pylint": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_PYLINT.keys()
    },
    "pytest-dev/pytest": {
        k: "pytest -rA --tb=long" for k in MAP_VERSION_TO_INSTALL_PYTEST.keys()
    },
    "pyvista/pyvista": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_PYVISTA.keys()
    },
    "scikit-learn/scikit-learn": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_SKLEARN.keys()
    },
    "sphinx-doc/sphinx": {
        k: "tox -epy39 -v --" for k in MAP_VERSION_TO_INSTALL_SPHINX.keys()
    },
    "sqlfluff/sqlfluff": {
        k: TEST_PYTEST_VERBOSE for k in MAP_VERSION_TO_INSTALL_SQLFLUFF.keys()
    },
    "swe-bench/humaneval": {
        k: "python" for k in MAP_VERSION_TO_INSTALL_HUMANEVAL.keys()
    },
    "sympy/sympy": {
        k: "bin/test -C --verbose" for k in MAP_VERSION_TO_INSTALL_SYMPY.keys()
    },
}
MAP_REPO_TO_TEST_FRAMEWORK["django/django"]["1.9"] = "./tests/runtests.py --verbosity 2"

# Constants - Task Instance Requirements File Paths
MAP_REPO_TO_REQS_PATHS = {
    "dbt-labs/dbt-core": ["dev-requirements.txt", "dev_requirements.txt"],
    "django/django": ["tests/requirements/py3.txt"],
    "matplotlib/matplotlib": [
        "requirements/dev/dev-requirements.txt",
        "requirements/testing/travis_all.txt",
    ],
    "pallets/flask": ["requirements/dev.txt"],
    "pylint-dev/pylint": ["requirements_test.txt"],
    "pyvista/pyvista": ["requirements_test.txt", "requirements.txt"],
    "sqlfluff/sqlfluff": ["requirements_dev.txt"],
    "sympy/sympy": ["requirements-dev.txt"],
    "python/mypy":["test-requirements.txt"],
}

# Constants - Task Instance environment.yml File Paths
MAP_REPO_TO_ENV_YML_PATHS = {
    "matplotlib/matplotlib": ["environment.yml"],
    "pydata/xarray": ["ci/requirements/environment.yml", "environment.yml"],
}

# Constants - Evaluation Keys
KEY_INSTANCE_ID = "instance_id"
KEY_MODEL = "model_name_or_path"
KEY_PREDICTION = "model_patch"

# Constants - Logging
APPLY_PATCH_FAIL = ">>>>> Patch Apply Failed"
APPLY_PATCH_PASS = ">>>>> Applied Patch"
INSTALL_FAIL = ">>>>> Init Failed"
INSTALL_PASS = ">>>>> Init Succeeded"
INSTALL_TIMEOUT = ">>>>> Init Timed Out"
RESET_FAILED = ">>>>> Reset Failed"
TESTS_ERROR = ">>>>> Tests Errored"
TESTS_FAILED = ">>>>> Some Tests Failed"
TESTS_PASSED = ">>>>> All Tests Passed"
TESTS_TIMEOUT = ">>>>> Tests Timed Out"


# Constants - Patch Types
class PatchType(Enum):
    PATCH_GOLD = "gold"
    PATCH_PRED = "pred"
    PATCH_PRED_TRY = "pred_try"
    PATCH_PRED_MINIMAL = "pred_minimal"
    PATCH_PRED_MINIMAL_TRY = "pred_minimal_try"
    PATCH_TEST = "test"

    def __str__(self):
        return self.value


# Constants - Miscellaneous
NON_TEST_EXTS = [
    ".json",
    ".png",
    "csv",
    ".txt",
    ".md",
    ".jpg",
    ".jpeg",
    ".pkl",
    ".yml",
    ".yaml",
    ".toml",
]
# SWE_BENCH_URL_RAW = "https://github.com/"
SWE_BENCH_URL_RAW = "https://raw.githubusercontent.com/"
USE_X86 = {
    "astropy__astropy-7973",
    "django__django-10087",
    "django__django-10097",
    "django__django-10213",
    "django__django-10301",
    "django__django-10316",
    "django__django-10426",
    "django__django-11383",
    "django__django-12185",
    "django__django-12497",
    "django__django-13121",
    "django__django-13417",
    "django__django-13431",
    "django__django-13447",
    "django__django-14155",
    "django__django-14164",
    "django__django-14169",
    "django__django-14170",
    "django__django-15180",
    "django__django-15199",
    "django__django-15280",
    "django__django-15292",
    "django__django-15474",
    "django__django-15682",
    "django__django-15689",
    "django__django-15695",
    "django__django-15698",
    "django__django-15781",
    "django__django-15925",
    "django__django-15930",
    "django__django-5158",
    "django__django-5470",
    "django__django-7188",
    "django__django-7475",
    "django__django-7530",
    "django__django-8326",
    "django__django-8961",
    "django__django-9003",
    "django__django-9703",
    "django__django-9871",
    "matplotlib__matplotlib-13983",
    "matplotlib__matplotlib-13984",
    "matplotlib__matplotlib-13989",
    "matplotlib__matplotlib-14043",
    "matplotlib__matplotlib-14471",
    "matplotlib__matplotlib-22711",
    "matplotlib__matplotlib-22719",
    "matplotlib__matplotlib-22734",
    "matplotlib__matplotlib-22767",
    "matplotlib__matplotlib-22815",
    "matplotlib__matplotlib-22835",
    "matplotlib__matplotlib-22865",
    "matplotlib__matplotlib-22871",
    "matplotlib__matplotlib-22883",
    "matplotlib__matplotlib-22926",
    "matplotlib__matplotlib-22929",
    "matplotlib__matplotlib-22931",
    "matplotlib__matplotlib-22945",
    "matplotlib__matplotlib-22991",
    "matplotlib__matplotlib-23031",
    "matplotlib__matplotlib-23047",
    "matplotlib__matplotlib-23049",
    "matplotlib__matplotlib-23057",
    "matplotlib__matplotlib-23088",
    "matplotlib__matplotlib-23111",
    "matplotlib__matplotlib-23140",
    "matplotlib__matplotlib-23174",
    "matplotlib__matplotlib-23188",
    "matplotlib__matplotlib-23198",
    "matplotlib__matplotlib-23203",
    "matplotlib__matplotlib-23266",
    "matplotlib__matplotlib-23267",
    "matplotlib__matplotlib-23288",
    "matplotlib__matplotlib-23299",
    "matplotlib__matplotlib-23314",
    "matplotlib__matplotlib-23332",
    "matplotlib__matplotlib-23348",
    "matplotlib__matplotlib-23412",
    "matplotlib__matplotlib-23476",
    "matplotlib__matplotlib-23516",
    "matplotlib__matplotlib-23562",
    "matplotlib__matplotlib-23563",
    "matplotlib__matplotlib-23573",
    "matplotlib__matplotlib-23740",
    "matplotlib__matplotlib-23742",
    "matplotlib__matplotlib-23913",
    "matplotlib__matplotlib-23964",
    "matplotlib__matplotlib-23987",
    "matplotlib__matplotlib-24013",
    "matplotlib__matplotlib-24026",
    "matplotlib__matplotlib-24088",
    "matplotlib__matplotlib-24111",
    "matplotlib__matplotlib-24149",
    "matplotlib__matplotlib-24177",
    "matplotlib__matplotlib-24189",
    "matplotlib__matplotlib-24224",
    "matplotlib__matplotlib-24250",
    "matplotlib__matplotlib-24257",
    "matplotlib__matplotlib-24265",
    "matplotlib__matplotlib-24334",
    "matplotlib__matplotlib-24362",
    "matplotlib__matplotlib-24403",
    "matplotlib__matplotlib-24431",
    "matplotlib__matplotlib-24538",
    "matplotlib__matplotlib-24570",
    "matplotlib__matplotlib-24604",
    "matplotlib__matplotlib-24619",
    "matplotlib__matplotlib-24627",
    "matplotlib__matplotlib-24637",
    "matplotlib__matplotlib-24691",
    "matplotlib__matplotlib-24749",
    "matplotlib__matplotlib-24768",
    "matplotlib__matplotlib-24849",
    "matplotlib__matplotlib-24870",
    "matplotlib__matplotlib-24912",
    "matplotlib__matplotlib-24924",
    "matplotlib__matplotlib-24970",
    "matplotlib__matplotlib-24971",
    "matplotlib__matplotlib-25027",
    "matplotlib__matplotlib-25052",
    "matplotlib__matplotlib-25079",
    "matplotlib__matplotlib-25085",
    "matplotlib__matplotlib-25122",
    "matplotlib__matplotlib-25126",
    "matplotlib__matplotlib-25129",
    "matplotlib__matplotlib-25238",
    "matplotlib__matplotlib-25281",
    "matplotlib__matplotlib-25287",
    "matplotlib__matplotlib-25311",
    "matplotlib__matplotlib-25332",
    "matplotlib__matplotlib-25334",
    "matplotlib__matplotlib-25340",
    "matplotlib__matplotlib-25346",
    "matplotlib__matplotlib-25404",
    "matplotlib__matplotlib-25405",
    "matplotlib__matplotlib-25425",
    "matplotlib__matplotlib-25430",
    "matplotlib__matplotlib-25433",
    "matplotlib__matplotlib-25442",
    "matplotlib__matplotlib-25479",
    "matplotlib__matplotlib-25498",
    "matplotlib__matplotlib-25499",
    "matplotlib__matplotlib-25515",
    "matplotlib__matplotlib-25547",
    "matplotlib__matplotlib-25551",
    "matplotlib__matplotlib-25565",
    "matplotlib__matplotlib-25624",
    "matplotlib__matplotlib-25631",
    "matplotlib__matplotlib-25640",
    "matplotlib__matplotlib-25651",
    "matplotlib__matplotlib-25667",
    "matplotlib__matplotlib-25712",
    "matplotlib__matplotlib-25746",
    "matplotlib__matplotlib-25772",
    "matplotlib__matplotlib-25775",
    "matplotlib__matplotlib-25779",
    "matplotlib__matplotlib-25785",
    "matplotlib__matplotlib-25794",
    "matplotlib__matplotlib-25859",
    "matplotlib__matplotlib-25960",
    "matplotlib__matplotlib-26011",
    "matplotlib__matplotlib-26020",
    "matplotlib__matplotlib-26024",
    "matplotlib__matplotlib-26078",
    "matplotlib__matplotlib-26089",
    "matplotlib__matplotlib-26101",
    "matplotlib__matplotlib-26113",
    "matplotlib__matplotlib-26122",
    "matplotlib__matplotlib-26160",
    "matplotlib__matplotlib-26184",
    "matplotlib__matplotlib-26208",
    "matplotlib__matplotlib-26223",
    "matplotlib__matplotlib-26232",
    "matplotlib__matplotlib-26249",
    "matplotlib__matplotlib-26278",
    "matplotlib__matplotlib-26285",
    "matplotlib__matplotlib-26291",
    "matplotlib__matplotlib-26300",
    "matplotlib__matplotlib-26311",
    "matplotlib__matplotlib-26341",
    "matplotlib__matplotlib-26342",
    "matplotlib__matplotlib-26399",
    "matplotlib__matplotlib-26466",
    "matplotlib__matplotlib-26469",
    "matplotlib__matplotlib-26472",
    "matplotlib__matplotlib-26479",
    "matplotlib__matplotlib-26532",
    "pydata__xarray-2905",
    "pydata__xarray-2922",
    "pydata__xarray-3095",
    "pydata__xarray-3114",
    "pydata__xarray-3151",
    "pydata__xarray-3156",
    "pydata__xarray-3159",
    "pydata__xarray-3239",
    "pydata__xarray-3302",
    "pydata__xarray-3305",
    "pydata__xarray-3338",
    "pydata__xarray-3364",
    "pydata__xarray-3406",
    "pydata__xarray-3520",
    "pydata__xarray-3527",
    "pydata__xarray-3631",
    "pydata__xarray-3635",
    "pydata__xarray-3637",
    "pydata__xarray-3649",
    "pydata__xarray-3677",
    "pydata__xarray-3733",
    "pydata__xarray-3812",
    "pydata__xarray-3905",
    "pydata__xarray-3976",
    "pydata__xarray-3979",
    "pydata__xarray-3993",
    "pydata__xarray-4075",
    "pydata__xarray-4094",
    "pydata__xarray-4098",
    "pydata__xarray-4182",
    "pydata__xarray-4184",
    "pydata__xarray-4248",
    "pydata__xarray-4339",
    "pydata__xarray-4356",
    "pydata__xarray-4419",
    "pydata__xarray-4423",
    "pydata__xarray-4442",
    "pydata__xarray-4493",
    "pydata__xarray-4510",
    "pydata__xarray-4629",
    "pydata__xarray-4683",
    "pydata__xarray-4684",
    "pydata__xarray-4687",
    "pydata__xarray-4695",
    "pydata__xarray-4750",
    "pydata__xarray-4758",
    "pydata__xarray-4759",
    "pydata__xarray-4767",
    "pydata__xarray-4802",
    "pydata__xarray-4819",
    "pydata__xarray-4827",
    "pydata__xarray-4879",
    "pydata__xarray-4911",
    "pydata__xarray-4939",
    "pydata__xarray-4940",
    "pydata__xarray-4966",
    "pydata__xarray-4994",
    "pydata__xarray-5033",
    "pydata__xarray-5126",
    "pydata__xarray-5131",
    "pydata__xarray-5180",
    "pydata__xarray-5187",
    "pydata__xarray-5233",
    "pydata__xarray-5362",
    "pydata__xarray-5365",
    "pydata__xarray-5455",
    "pydata__xarray-5580",
    "pydata__xarray-5662",
    "pydata__xarray-5682",
    "pydata__xarray-5731",
    "pydata__xarray-6135",
    "pydata__xarray-6386",
    "pydata__xarray-6394",
    "pydata__xarray-6400",
    "pydata__xarray-6461",
    "pydata__xarray-6548",
    "pydata__xarray-6598",
    "pydata__xarray-6599",
    "pydata__xarray-6601",
    "pydata__xarray-6721",
    "pydata__xarray-6744",
    "pydata__xarray-6798",
    "pydata__xarray-6804",
    "pydata__xarray-6823",
    "pydata__xarray-6857",
    "pydata__xarray-6882",
    "pydata__xarray-6889",
    "pydata__xarray-6938",
    "pydata__xarray-6971",
    "pydata__xarray-6992",
    "pydata__xarray-6999",
    "pydata__xarray-7003",
    "pydata__xarray-7019",
    "pydata__xarray-7052",
    "pydata__xarray-7089",
    "pydata__xarray-7101",
    "pydata__xarray-7105",
    "pydata__xarray-7112",
    "pydata__xarray-7120",
    "pydata__xarray-7147",
    "pydata__xarray-7150",
    "pydata__xarray-7179",
    "pydata__xarray-7203",
    "pydata__xarray-7229",
    "pydata__xarray-7233",
    "pydata__xarray-7347",
    "pydata__xarray-7391",
    "pydata__xarray-7393",
    "pydata__xarray-7400",
    "pydata__xarray-7444",
    "pytest-dev__pytest-10482",
    "scikit-learn__scikit-learn-10198",
    "scikit-learn__scikit-learn-10297",
    "scikit-learn__scikit-learn-10306",
    "scikit-learn__scikit-learn-10331",
    "scikit-learn__scikit-learn-10377",
    "scikit-learn__scikit-learn-10382",
    "scikit-learn__scikit-learn-10397",
    "scikit-learn__scikit-learn-10427",
    "scikit-learn__scikit-learn-10428",
    "scikit-learn__scikit-learn-10443",
    "scikit-learn__scikit-learn-10452",
    "scikit-learn__scikit-learn-10459",
    "scikit-learn__scikit-learn-10471",
    "scikit-learn__scikit-learn-10483",
    "scikit-learn__scikit-learn-10495",
    "scikit-learn__scikit-learn-10508",
    "scikit-learn__scikit-learn-10558",
    "scikit-learn__scikit-learn-10577",
    "scikit-learn__scikit-learn-10581",
    "scikit-learn__scikit-learn-10687",
    "scikit-learn__scikit-learn-10774",
    "scikit-learn__scikit-learn-10777",
    "scikit-learn__scikit-learn-10803",
    "scikit-learn__scikit-learn-10844",
    "scikit-learn__scikit-learn-10870",
    "scikit-learn__scikit-learn-10881",
    "scikit-learn__scikit-learn-10899",
    "scikit-learn__scikit-learn-10908",
    "scikit-learn__scikit-learn-10913",
    "scikit-learn__scikit-learn-10949",
    "scikit-learn__scikit-learn-10982",
    "scikit-learn__scikit-learn-10986",
    "scikit-learn__scikit-learn-11040",
    "scikit-learn__scikit-learn-11042",
    "scikit-learn__scikit-learn-11043",
    "scikit-learn__scikit-learn-11151",
    "scikit-learn__scikit-learn-11160",
    "scikit-learn__scikit-learn-11206",
    "scikit-learn__scikit-learn-11235",
    "scikit-learn__scikit-learn-11243",
    "scikit-learn__scikit-learn-11264",
    "scikit-learn__scikit-learn-11281",
    "scikit-learn__scikit-learn-11310",
    "scikit-learn__scikit-learn-11315",
    "scikit-learn__scikit-learn-11333",
    "scikit-learn__scikit-learn-11346",
    "scikit-learn__scikit-learn-11391",
    "scikit-learn__scikit-learn-11496",
    "scikit-learn__scikit-learn-11542",
    "scikit-learn__scikit-learn-11574",
    "scikit-learn__scikit-learn-11578",
    "scikit-learn__scikit-learn-11585",
    "scikit-learn__scikit-learn-11596",
    "scikit-learn__scikit-learn-11635",
    "scikit-learn__scikit-learn-12258",
    "scikit-learn__scikit-learn-12421",
    "scikit-learn__scikit-learn-12443",
    "scikit-learn__scikit-learn-12462",
    "scikit-learn__scikit-learn-12471",
    "scikit-learn__scikit-learn-12486",
    "scikit-learn__scikit-learn-12557",
    "scikit-learn__scikit-learn-12583",
    "scikit-learn__scikit-learn-12585",
    "scikit-learn__scikit-learn-12625",
    "scikit-learn__scikit-learn-12626",
    "scikit-learn__scikit-learn-12656",
    "scikit-learn__scikit-learn-12682",
    "scikit-learn__scikit-learn-12704",
    "scikit-learn__scikit-learn-12733",
    "scikit-learn__scikit-learn-12758",
    "scikit-learn__scikit-learn-12760",
    "scikit-learn__scikit-learn-12784",
    "scikit-learn__scikit-learn-12827",
    "scikit-learn__scikit-learn-12834",
    "scikit-learn__scikit-learn-12860",
    "scikit-learn__scikit-learn-12908",
    "scikit-learn__scikit-learn-12938",
    "scikit-learn__scikit-learn-12961",
    "scikit-learn__scikit-learn-12973",
    "scikit-learn__scikit-learn-12983",
    "scikit-learn__scikit-learn-12989",
    "scikit-learn__scikit-learn-13010",
    "scikit-learn__scikit-learn-13013",
    "scikit-learn__scikit-learn-13017",
    "scikit-learn__scikit-learn-13046",
    "scikit-learn__scikit-learn-13087",
    "scikit-learn__scikit-learn-13124",
    "scikit-learn__scikit-learn-13135",
    "scikit-learn__scikit-learn-13142",
    "scikit-learn__scikit-learn-13143",
    "scikit-learn__scikit-learn-13157",
    "scikit-learn__scikit-learn-13165",
    "scikit-learn__scikit-learn-13174",
    "scikit-learn__scikit-learn-13221",
    "scikit-learn__scikit-learn-13241",
    "scikit-learn__scikit-learn-13253",
    "scikit-learn__scikit-learn-13280",
    "scikit-learn__scikit-learn-13283",
    "scikit-learn__scikit-learn-13302",
    "scikit-learn__scikit-learn-13313",
    "scikit-learn__scikit-learn-13328",
    "scikit-learn__scikit-learn-13333",
    "scikit-learn__scikit-learn-13363",
    "scikit-learn__scikit-learn-13368",
    "scikit-learn__scikit-learn-13392",
    "scikit-learn__scikit-learn-13436",
    "scikit-learn__scikit-learn-13439",
    "scikit-learn__scikit-learn-13447",
    "scikit-learn__scikit-learn-13454",
    "scikit-learn__scikit-learn-13467",
    "scikit-learn__scikit-learn-13472",
    "scikit-learn__scikit-learn-13485",
    "scikit-learn__scikit-learn-13496",
    "scikit-learn__scikit-learn-13497",
    "scikit-learn__scikit-learn-13536",
    "scikit-learn__scikit-learn-13549",
    "scikit-learn__scikit-learn-13554",
    "scikit-learn__scikit-learn-13584",
    "scikit-learn__scikit-learn-13618",
    "scikit-learn__scikit-learn-13620",
    "scikit-learn__scikit-learn-13628",
    "scikit-learn__scikit-learn-13641",
    "scikit-learn__scikit-learn-13704",
    "scikit-learn__scikit-learn-13726",
    "scikit-learn__scikit-learn-13779",
    "scikit-learn__scikit-learn-13780",
    "scikit-learn__scikit-learn-13828",
    "scikit-learn__scikit-learn-13864",
    "scikit-learn__scikit-learn-13877",
    "scikit-learn__scikit-learn-13910",
    "scikit-learn__scikit-learn-13915",
    "scikit-learn__scikit-learn-13933",
    "scikit-learn__scikit-learn-13960",
    "scikit-learn__scikit-learn-13974",
    "scikit-learn__scikit-learn-13983",
    "scikit-learn__scikit-learn-14012",
    "scikit-learn__scikit-learn-14024",
    "scikit-learn__scikit-learn-14053",
    "scikit-learn__scikit-learn-14067",
    "scikit-learn__scikit-learn-14087",
    "scikit-learn__scikit-learn-14092",
    "scikit-learn__scikit-learn-14114",
    "scikit-learn__scikit-learn-14125",
    "scikit-learn__scikit-learn-14141",
    "scikit-learn__scikit-learn-14237",
    "scikit-learn__scikit-learn-14309",
    "scikit-learn__scikit-learn-14430",
    "scikit-learn__scikit-learn-14450",
    "scikit-learn__scikit-learn-14458",
    "scikit-learn__scikit-learn-14464",
    "scikit-learn__scikit-learn-14496",
    "scikit-learn__scikit-learn-14520",
    "scikit-learn__scikit-learn-14544",
    "scikit-learn__scikit-learn-14591",
    "scikit-learn__scikit-learn-14629",
    "scikit-learn__scikit-learn-14704",
    "scikit-learn__scikit-learn-14706",
    "scikit-learn__scikit-learn-14710",
    "scikit-learn__scikit-learn-14732",
    "scikit-learn__scikit-learn-14764",
    "scikit-learn__scikit-learn-14806",
    "scikit-learn__scikit-learn-14869",
    "scikit-learn__scikit-learn-14878",
    "scikit-learn__scikit-learn-14890",
    "scikit-learn__scikit-learn-14894",
    "scikit-learn__scikit-learn-14898",
    "scikit-learn__scikit-learn-14908",
    "scikit-learn__scikit-learn-14983",
    "scikit-learn__scikit-learn-14999",
    "scikit-learn__scikit-learn-15028",
    "scikit-learn__scikit-learn-15084",
    "scikit-learn__scikit-learn-15086",
    "scikit-learn__scikit-learn-15094",
    "scikit-learn__scikit-learn-15096",
    "scikit-learn__scikit-learn-15100",
    "scikit-learn__scikit-learn-15119",
    "scikit-learn__scikit-learn-15120",
    "scikit-learn__scikit-learn-15138",
    "scikit-learn__scikit-learn-15393",
    "scikit-learn__scikit-learn-15495",
    "scikit-learn__scikit-learn-15512",
    "scikit-learn__scikit-learn-15524",
    "scikit-learn__scikit-learn-15535",
    "scikit-learn__scikit-learn-15625",
    "scikit-learn__scikit-learn-3840",
    "scikit-learn__scikit-learn-7760",
    "scikit-learn__scikit-learn-8554",
    "scikit-learn__scikit-learn-9274",
    "scikit-learn__scikit-learn-9288",
    "scikit-learn__scikit-learn-9304",
    "scikit-learn__scikit-learn-9775",
    "scikit-learn__scikit-learn-9939",
    "sphinx-doc__sphinx-11311",
    "sphinx-doc__sphinx-7910",
    "sympy__sympy-12812",
    "sympy__sympy-14248",
    "sympy__sympy-15222",
    "sympy__sympy-19201",
}
