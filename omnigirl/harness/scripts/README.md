# Scripts for reproducing experiment results
This directory includes scripts for reproducing experiment results.

## Evaluation on full set of OmniGIRL
We provide evaluation results for three models—**GPT-4o-2024-08-06**, **DeepSeek-V2.5**, and **Claude-3.5-Sonnet-2024-06-25**—using two methods: **AgentlessX** and **Oracle Retrieval**. To access these results, execute the following scripts:

### GPT-4o-2024-08-06

To evaluate the GPT-4o model:

- **AgentlessX method**:
  ```bash
  cd ..
  bash scripts/Eval_GPT4o_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd ..
  bash scripts/Eval_GPT4o_OracleRetrieval.sh
  ```

### DeepSeek-V2.5

To evaluate the DeepSeek model:

- **AgentlessX method**:
  ```bash
  cd ..
  bash scripts/Eval_DeepSeek_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd ..
  bash scripts/Eval_DeepSeek_OracleRetrieval.sh
  ```

### Claude-3.5-Sonnet-2024-06-25

To evaluate the Claude model:

- **AgentlessX method**:
  ```bash
  cd ..
  bash scripts/Eval_Claude_AgentlessX.sh
  ```

- **Oracle Retrieval method**:
  ```bash
  cd ..
  bash scripts/Eval_Claude_OracleRetrieval.sh
  ```



## Evaluation on subset with visual inputs

In addition to the full set of OmniGIRL, we provide evaluation results for a subset of OmniGIRL with visual inputs. This subset contains 19 task instances. The experiments were conducted using **GPT-4o-2024-08-06** and **Claude-3.5-Sonnet-2024-06-25**, evaluated with both the **AgentlessX** and **Oracle Retrieval** methods. We evaluate LLMs under three different settings: **text-only**, **text&image** and **image-augmented text**. Each experiment was repeated **three times** to ensure robustness. Follow the steps below to run the experiments for each model and evaluation method:

### Claude-3.5-Sonnet-2024-06-25

- **AgentlessX method**:

  ```bash
  cd ..
  bash scripts/Eval_VisualSubset_Claude_AgentlessX.sh
  ```

- **Oracle Retrieval method**:

  ```bash
  cd ..
  bash scripts/Eval_VisualSubset_Claude_OracleRetrieval.sh
  ```

### GPT-4o-2024-08-06

- **AgentlessX method**:

  ```bash
  cd ..
  bash scripts/Eval_VisualSubset_GPT4o_AgentlessX.sh
  ```

- **Oracle Retrieval method**:

  ```bash
  cd ..
  bash scripts/Eval_VisualSubset_GPT4o_OracleRetrieval.sh
  ```
