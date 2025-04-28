# OmniGIRL 
A GitHub issue resolution benchmark with multi-aspect diversity across programming languages, repository domains, and modalities of input information.


## 📦 Environment Setup

To get started, follow the steps below to set up the environment:

```bash
conda create --name omnigirl python=3.11.5 -y
conda activate omnigirl
pip install -r requirements.txt
```

## 🚀 Running Evaluations

After setup the environment, you need to do following things to run evaluation:

1. Prediction file: Some patch files in JSONL format, each item containing:
   - `model_name_or_path`: Model Name
   - `instance_id`: Task Instance id
   - `prediction_patch`: Prediction Patch Content

    Example:
    ```json
    {
        "model_name_or_path": "agentless-v1",
        "instance_id": "prettier__prettier-12260",
        "fix_patch": "diff --git ...."
    }
    ```
2. Dataset Files: Dataset files in JSON format available on omnigirl/harness/benchmark/OmniGIRL.json

3. Move to omnigirl/harness, then you can run the evaluation using the following command:

```bash
# required
cd omnigirl/harness

python run_evaluation.py --dataset_name benchmark/OmniGIRL.json \
                         --predictions_path <path of your prediction results> \
                         --max_workers 15 \
                         --run_id <unique id number of this evaluation>
```

4. By default, your evaluation results will be generated in omnigirl/harness/reports.

## 🙏 Acknowledgements
- We build on prior work — **[SWE-bench](https://arxiv.org/abs/2310.06770)**, **[Agentless](https://arxiv.org/abs/2407.01489)**, and **[AutoCodeRover](https://arxiv.org/abs/2404.05427)** — which laid the groundwork for this study.
- We thank the **[EvalPlus leaderboard](https://github.com/evalplus/evalplus)** team for releasing the elegant page template that inspired this site.
- Finally, we are grateful to the **open-source developer community** for their invaluable contributions.
