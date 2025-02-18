#!/usr/bin/env python3

"""Given the `<owner/name>` of a GitHub repo, this script writes the raw information for all the repo's PRs to a single `.jsonl` file."""

import argparse
import json
import logging
import os
from typing import Optional
from tqdm import tqdm
from fastcore.xtras import obj2dict
from utils import Repo

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def log_all_pulls(repo: Repo, output: str, mode: str, pr_data_list=None):
    """
    Iterate over all pull requests in a repository and log them to a file

    Args:
        repo (Repo): repository object
        output (str): output file name
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if mode == 'swebench':
        with open(output, "w") as output_file:
            for pull in repo.get_all_pulls():
                setattr(pull, "resolved_issues", repo.extract_resolved_issues(pull))
                print(json.dumps(obj2dict(pull)), end="\n", flush=True, file=output_file)
    else:
        pulls = repo.get_all_pulls_with_official_github_api()
        print(f'total prs number: {len(pulls)}')
        with open(output, 'a') as f:
            for pull in tqdm(pulls):
                if pr_data_list and pull['number'] in pr_data_list:
                    continue
                else:
                    issues = repo.extract_resolved_issues_with_official_github_api(pull)
                    pull["resolved_issues"] = issues
                    json.dump(pull, f)
                    f.write('\n')  # 写入换行符以分隔 JSON 对象

                


def main(repo_name: str, output: str, token: Optional[str] = None,mode: Optional[str]  ='swebench'):
    """
    Logic for logging all pull requests in a repository

    Args:
        repo_name (str): name of the repository
        output (str): output file name
        token (str, optional): GitHub token
    """
    if token is None:
        token = os.environ["GITHUB_TOKEN"]
    try:
        owner, repo = repo_name.split("/")
    except:
        print(repo_name)
    logger.info(repo_name)
    repo = Repo(owner, repo, token=token)
    if os.path.exists(output):
        pr_data_list = []
        with open(output, 'r', encoding='utf-8') as f:
            for line in f:  
                pr_data_list.append(json.loads(line)['number'])
        log_all_pulls(repo, output,mode,pr_data_list)
    else:
        log_all_pulls(repo, output,mode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo_name", type=str, help="Name of the repository")
    parser.add_argument("output", type=str, help="Output file name")
    parser.add_argument("--token", type=str, help="GitHub token")
    parser.add_argument("--mode", type=str, default='omnigirl',help="GitHub token")
    args = parser.parse_args()
    main(**vars(args))
