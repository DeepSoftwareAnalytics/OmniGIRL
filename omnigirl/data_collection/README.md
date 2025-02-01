# Data Collection Tutorial

This module contains scripts and tools for collecting and processing GitHub repository issue data. This tutorial will guide you on how to use these tools for data collection.

## Data Collection Process Overview

The data collection process consists of three main phases:

1. **Raw Repository Data Collection**
   - **Data Extraction**
     - Use the `print_pulls.py` script to collect raw PR data from GitHub repositories with parameters:
       ```bash
       python print_pulls.py <repo_name> <output_file> [--token <token>] [--mode omnigirl]
       ```
       Where:
       - `<repo_name>`: GitHub repository name in format "owner/repo" (e.g., "octocat/Hello-World")
       - `<output_file>`: Output JSONL file path (e.g., "data/prs.jsonl")
       - `--token`: Optional GitHub personal access token (default uses GITHUB_TOKEN env var)
       - `--mode`: Collection mode (default: 'omnigirl')
       
       Example:
       ```bash
       python print_pulls.py octocat/Hello-World data/prs.jsonl --token <your token> --mode omnigirl
       ```
     - Use the `build_dataset.py` script to process collected PR data with parameters:
       ```bash
       python build_dataset.py <pr_file> <output_file> [--token <token>] [--mode omnigirl] [--cutoff_date <date>] [--language <language>]
       ```
       Where:
       - `<pr_file>`: Path to input PR JSONL file (e.g., "data/prs.jsonl")
       - `<output_file>`: Output JSONL file path (e.g., "data/dataset.jsonl")
       - `--token`: Optional GitHub personal access token (default uses GITHUB_TOKEN env var)
       - `--mode`: Collection mode (default: 'omnigirl')
       - `--cutoff_date`: Cutoff date for filtering PRs in YYYY-MM-DDTHH:MM:SSZ format (default: "2024-06-30T23:59:59Z")
       - `--language`: Programming language of the repository
       
       Example:
       ```bash
       python build_dataset.py data/prs.jsonl data/dataset.jsonl --token <your token> --mode omnigirl --language python
       ```

2. **Versioning**
   - Use the `get_versions.py` script to assign version numbers to instances with parameters:
     ```bash
     python get_versions.py --instances_path <instances_path> --retrieval_method github --num_workers <num_workers> --output_dir <output_dir>
     ```
     Where:
     - `--instances_path`: Path to task instances (required)
     - `--retrieval_method`: Version retrieval method (use "github")
     - `--num_workers`: Number of threads to use (default: 1)
     - `--output_dir`: Path to save results
     
     Example:
     ```bash
     python get_versions.py --instances_path data/instances.jsonl --retrieval_method github --num_workers 4 --output_dir data/versions
     ```

3. **Environment Configuration**
   - **Manual Setup Required**: This step requires manual configuration of execution environments for each instance
   - Key configuration steps:
     - Identify and document the required dependencies for each repository version
     - Record the installation commands needed to set up each version's environment
     - Determine and document the appropriate test commands for each version
     
4. **Execution-based Filtering**
   - This step requires manual test execution to verify instances
   - Filtering process:
     1. Run tests without applying the gold patch and record test results
     2. Apply the gold patch and run tests again, recording new results
     3. Compare test results to identify FAIL_TO_PASS cases
     4. Retain instances that have at least one FAIL_TO_PASS test case
   - This ensures:
     - Test cases are executable in configured environments
     - Code changes are verifiable through test execution
     - Only high-quality instances with verifiable fixes are included
   - Generate final dataset for model training from filtered instances
