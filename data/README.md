# Data Access & Acquisition Protocol

## Primary Benchmark: SciFact
* **Source:** Allen Institute for AI (`allenai/scifact`)
* **Task:** Verification of claims against cited publication abstracts (`SUPPORTS`, `REFUTES`, `NOINFO`).
* **License:** Apache 2.0 / CC-BY 4.0.
* **Access Mode:** Automated via Hugging Face `datasets.load_dataset("allenai/scifact", "claims")`.

## Fallback Benchmark: SciTail
* **Source:** Allen Institute for AI (`allenai/scitail`, `snli_format`)
* **Task:** Scientific premise-hypothesis entailment verification (`neutral`, `entails`).
* **License:** Apache 2.0 / Open Scholarly Access.
* **Access Mode:** Automated via Hugging Face `datasets.load_dataset("allenai/scitail", "snli_format", split="test")`.

## Data Governance & Leakage Controls
* In accordance with ATR_Task research integrity standards, raw scientific text files are not committed to Git.
* Ingestion pipelines fetch public benchmarks on-the-fly and fix random seeds (`seed=42`) to ensure strict partition isolation.
