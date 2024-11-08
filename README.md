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

We provide evaluation results for three models—**GPT-4o-2024-08-06**, **DeepSeek-V2.5**, and **Claude-3.5-Sonnet-2024-06-25**—using two methods: **AgentlessX** and **Oracle Retrieval**. To access these results, execute the following scripts:

### Evaluation on full set of OmniGIRL

#### GPT-4o-2024-08-06

To evaluate the GPT-4o model:

- **AgentlessX method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_GPT4o_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_GPT4o_OracleRetrieval.sh
  ```

#### DeepSeek-V2.5

To evaluate the DeepSeek model:

- **AgentlessX method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_DeepSeek_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_DeepSeek_OracleRetrieval.sh
  ```

#### Claude-3.5-Sonnet-2024-06-25

To evaluate the Claude model:

- **AgentlessX method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_Claude_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd omnigirl/harness
  bash scripts/Eval_Claude_OracleRetrieval.sh
  ```



### OmniGIRL - Visual Input Subset Evaluation

In addition to the full OmniGIRL set, we provide evaluation results for a subset with **visual input data**. This subset contains tasks requiring multi-modal analysis, combining **text-only** and **image-augmented text** scenarios. The experiments were conducted using **GPT-4o-2024-08-06** and **Claude-3.5-Sonnet-2024-06-25**, evaluated with both the **AgentlessX** and **Oracle Retrieval** methods. Each experiment was repeated **three times** to ensure robustness.

#### Experiment Scenarios

1. **Text Only**: Evaluates performance with purely textual inputs.
2. **Text & Image**: Evaluates performance with a combination of text and accompanying images.
3. **Image-Augmented Text**: Evaluates performance on text inputs enhanced with image-based context.


Follow the steps below to run the experiments for each model and evaluation method:

#### Claude-3.5-Sonnet-2024-06-25

- **AgentlessX method**:

```bash
cd omnigirl/harness
bash scripts/Eval_VisualSubset_Claude_AgentlessX.sh
```

- **Oracle Retrieval method**:

```bash
cd omnigirl/harness
bash scripts/Eval_VisualSubset_Claude_OracleRetrieval.sh
```

#### GPT-4o-2024-08-06

- **AgentlessX method**:

```bash
cd omnigirl/harness
bash scripts/Eval_VisualSubset_GPT4o_AgentlessX.sh
```

- **Oracle Retrieval method**:

```bash
cd omnigirl/harness
bash scripts/Eval_VisualSubset_GPT4o_OracleRetrieval.sh
```

