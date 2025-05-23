[![SVG Banners](https://svg-banners.vercel.app/api?type=origin&text1=OmniGIRL%20🧑‍💻&text2=💖%20GitHub%20Issue%20Resolusion&width=900&height=200)](https://github.com/Akshay090/svg-banners)


# 👉🏻 OmniGIRL 👈🏻


🌐 <a href="https://deepsoftwareanalytics.github.io/omnigirl_leaderboard.html" target="_blank">Website</a>  •  🤗 <a href="https://huggingface.co/datasets/Deep-Software-Analytics/OmniGIRL" target="_blank">Hugging Face</a>  •  🐋 <a href="https://hub.docker.com/r/guolianghong/omnigirl/tags" target="_blank">Env Docker Image</a>  •   📃 <a href="http://arxiv.org/abs/2505.04606" target="_blank">arXiv Paper</a> ·  📓 <a href="https://conf.researchr.org/details/issta-2025/issta-2025-papers/2/OmniGIRL-A-Multilingual-and-Multimodal-Benchmark-for-GitHub-Issue-Resolution" target="_blank">ISSTA 2025</a>  



## ✨ Key Features

* 🚀 **Convenient, Standardized Evaluation Environment**

   [Provide Pre-built **Docker images**](https://hub.docker.com/r/guolianghong/omnigirl/tags), significantly simplifying the environment setup process and guaranteeing the **consistency and reproducibility** of evaluation tests.

* 🕸 **Extensive Programming Language Coverage**

   Support **Python, Java, JavaScript, and TypeScript**, ensuring effective evaluation across these four major programming language ecosystems.

* 🗂️ **Rich Multimodal Input Data**

   Integrate diverse modalities (text, web content, and images), requiring evaluated models to **understand and leverage** information from all sources **to effectively resolve issues**.

* ⚒ **Automatic Environment Setup & Dataset Construction Tool** (will release before June 2025)

  Automatically setup the executable environment and construct the dataset, accelerating the construction of the benchmark for the task, which is labor-intensive currently.

---

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
  title={OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution},
  author={Guo, Lianghong and Tao, Wei and Jiang, Runhan and Wang, Yanlin and Chen, Jiachi and Liu, Xilin and Ma, Yuchi and Mao, Mingzhi and Zhang, Hongyu and Zheng, Zibin},
  booktitle={Proceedings of the 34rd ACM SIGSOFT International Symposium on Software Testing and Analysis},
  year={2025},
  publisher={{ACM}},
}
```

## 🙏 Acknowledgements
- We build on prior work — **[SWE-bench](https://arxiv.org/abs/2310.06770)**, **[Agentless](https://arxiv.org/abs/2407.01489)**, and **[AutoCodeRover](https://arxiv.org/abs/2404.05427)** — which laid the groundwork for this study.
- We thank the **[EvalPlus leaderboard](https://github.com/evalplus/evalplus)** team for releasing the elegant page template that inspired this site.
- Finally, we are grateful to the **open-source developer community** for their invaluable contributions.
