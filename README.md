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

OmniGIRL supports evaluation across different models and retrieval methods. Each model can be tested using either the **AgentlessX** or **Oracle Retrieval** methods.

### GPT-4o-2024-08-06

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

### DeepSeek-V2.5

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

### Claude-3.5-Sonnet-2024-06-25

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

