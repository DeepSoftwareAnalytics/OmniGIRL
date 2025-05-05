# OmniGIRL Evaluation
This directory is used for evaluating patch predictions on the OmniGIRL benchmark.


## 🚀 Running Evaluations

After setup the environment, you need to do following things to run evaluation:

1. Prepare Prediction file: Some patch files in JSONL format, each item containing:
   - `model_name_or_path`: Model Name
   - `instance_id`: Task Instance id
   - `prediction_patch`: Prediction Patch Content

    Example:
    ```json
    {
        "model_name_or_path": "agentless-v1",
        "instance_id": "prettier__prettier-12260",
        "model_patch": "diff --git ...."
    }
    ```

2. Move to omnigirl/harness, then you can run the evaluation using the following command:

```bash
# required
cd omnigirl/harness

python run_evaluation.py --predictions_path <path of your prediction results> \
                         --max_workers <number of workers> \
                         --run_id <unique id number of this evaluation>
```

3. By default, your evaluation results will be generated in omnigirl/harness/reports.

## ⚙️Configuration Parameters
parameters of run_evluation.py

| Parameter            | Description                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| `--dataset_name`     | Name of the dataset or path to a JSON file. Default: `"Deep-Software-Analytics/OmniGIRL"`         |
| `--predictions_path` | Path to prediction file                            |
| `--from_hub`         | Whether to pull Docker images from DockerHub (`True`) or build locally (`False`). Default: `True` |
| `--max_workers`      | Max number of parallel workers. Default: `4`                                                      |
| `--run_id`           | Unique ID to identify this evaluation run (**required**)                                          |
| `--instance_ids`     | Specific instance IDs to evaluate (space-separated list)                                          |
| `--timeout`          | Timeout (in seconds) for each instance. Default: `3600` (60 mins)                                 |
| `--reports_dir`      | Directory to save the output reports. Default: `"reports"`                                        |
| `--force_rebuild`    | Whether to force rebuild all Docker images. Default: `False`                                      |
| `--split`            | Dataset split to evaluate. Default: `"test"`                                                      |
| `--open_file_limit`  | Limit on number of open files. Default: `4096`                                                    |
| `--cache_level`      | Cache strategy: `"none"`, `"base"`, `"env"`, or `"instance"`. Default: `"env"`                    |
| `--clean`            | If `True`, remove all cached images above the cache level. Default: `False`                       |
| `--version_spec`     | Version specifier for filtering tasks. Default: `"all"`                                           |


## 💡 Usage Tips
1. Use amd64 architecture: This ensures full compatibility with Docker images and matches the evaluation setup in the paper.

2. --from_hub defaults to True: It will automatically pull images from DockerHub, allowing evaluation without requiring local image builds.

3. No need to set --dataset_name manually: By default, it pulls from Hugging Face. You can also specify a local file like benchmark/OmniGIRL.json.

4. Recommended --cache_level is env: Using instance may cache large amounts of image data, occupying excessive local disk space.

5. Adjust --max_workers based on your hardware: Over-parallelization may degrade performance or lead to unstable evaluations.

6. The --run_id parameter creates a unique directory: It stores logs and evaluation artifacts, while --reports_dir saves the final report.