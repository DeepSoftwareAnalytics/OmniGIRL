# OmniGIRL

OmniGIRL is a GitHub issue resolution benchmark with multi-aspect diversity across programming languages, repository domains, and modalities of input information. It specifically highlights the following key features:

* **Extensive Programming Language Coverage**: We provide comprehensive support for **Python, Java, JavaScript, and TypeScript**, ensuring effective evaluation across these four major programming language ecosystems.
* **Rich Multimodal Input Data**: The dataset integrates diverse modalities, requiring evaluated models to **fully understand and leverage** information from text, web, and images **to effectively resolve issues**.
* **Convenient, Standardized Evaluation Environment**: A pre-built **Docker image** is provided, significantly simplifying the environment setup process and guaranteeing the **consistency and reproducibility** of evaluation tests.

## 📦 Environment Setup

To get started, run the bash script below to set up the environment:

```bash
bash setup.sh
```

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

4. For the detailed tutorial about evaluation, please refer to  [omnigirl/harness directory](./omnigirl/harness)

5. Evaluation is recommended to be run on machines with amd64 architecture, consistent with the evaluation environment in the paper.

## 📖 Citation
If you find [OmniGIRL](https://deepsoftwareanalytics.github.io/omnigirl_leaderboard.html) useful for your research and applications, feel free to give us a star ⭐ or cite us using:

```bibtex
@inproceedings{guo2025omnigirl,
  title={OmniGIRL: a multilingual and multimodal benchmark for {GitHub} issue resolution},
  author={Guo, Lianghong and Tao, Wei and Jiang, Runhan and Wang, Yanlin and Chen, Jiachi and Liu, Xilin and Ma, Yuchi and Mao, Mingzhi and Zhang, Hongyu and Zheng, Zibin},
  booktitle={Proceedings of the 34th {ACM} {SIGSOFT} International Symposium on Software Testing and Analysis},
  pages={--}, % to be published
  year={2025},
  publisher={{ACM}},
}
```

## 🙏 Acknowledgements
- We build on prior work — **[SWE-bench](https://arxiv.org/abs/2310.06770)**, **[Agentless](https://arxiv.org/abs/2407.01489)**, and **[AutoCodeRover](https://arxiv.org/abs/2404.05427)** — which laid the groundwork for this study.
- We thank the **[EvalPlus leaderboard](https://github.com/evalplus/evalplus)** team for releasing the elegant page template that inspired this site.
- Finally, we are grateful to the **open-source developer community** for their invaluable contributions.
