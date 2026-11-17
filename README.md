# Detecting Citation Drift in AI-Generated Literature Summaries
Reproducible Implementation Repository (ATR_Task Lab 02)

## 1. Research Overview
Automated literature summarization systems powered by Large Language Models (LLMs) frequently exhibit citation drift—subtle divergence between generated in-text claims and the empirical findings of cited papers. While superficial citation anomalies (e.g., non-existent DOIs) can be caught by bibliographic lookups, detecting attribution drift requires evaluating semantic entailment between claims and evidence passages.

This repository implements a controlled, reproducible comparative study evaluating claim-level citation support detection under resource-constrained CPU environments, comparing:
1. System 0: Deterministic Lexical Jaccard Overlap Baseline (Token-matching heuristic)
2. System 1: Pretrained NLI Cross-Encoder (cross-encoder/nli-distilroberta-base, 82M params)

---

## 2. Repository Structure
```
AITR_Lab02_Project/
├── README.md                 # Project description and replication guide
├── requirements.txt          # Frozen library dependencies
├── configs/                  # Experimental configurations (hyperparameters, seeds)
│   └── config.yaml
├── data/                     # Dataset acquisition instructions & schema documentation
│   └── README.md
├── notebooks/                # Runnable demonstration & exploration notebooks
├── src/                      # Reusable verification modules
│   └── verifier.py
├── scripts/                  # Executable evaluation entrypoints
│   └── run_evaluation.py
├── results/                  # Verified execution metrics, logs, and confusion matrices
│   └── results.csv
├── paper/                    # Final manuscript files
│   ├── citation_drift_paper.tex
│   ├── references.bib
│   └── citation_drift_paper.pdf
├── research_decisions.md     # Literature-to-experiment design rationale
├── baseline_validation.md    # Baseline reproduction checks and discrepancy log
└── ai_assistance_log.md      # Human-AI collaboration & prompt verification audit
```

---

## 3. Verified Experimental Findings

Evaluated on N = 100 verified scientific claim–evidence pairs from the open-access SciTail benchmark on CPU:

| Metric | System 0 (Jaccard Baseline) | System 1 (NLI Cross-Encoder) | Delta |
| :--- | :---: | :---: | :---: |
| Accuracy | 58.00% | 68.00% | +10.00% |
| Macro-Averaged F1 | 0.3628 | 0.4913 | +0.1285 |
| Binary Macro-F1 (Active) | 0.5443 | 0.7370 | +0.1927 |
| Precision (NO_EVIDENCE) | 0.7895 | 0.7674 | -0.0221 |
| Recall (NO_EVIDENCE) | 0.2830 | 0.6226 | +0.3396 |
| Precision (SUPPORT) | 0.5309 | 0.8333 | +0.3024 |
| Recall (SUPPORT) | 0.9149 | 0.7447 | -0.1702 |
| Latency per Sample (CPU) | 0.021 ms | 920.750 ms | +920.729 ms (~43,845x) |

### Key Insight: Hallucination Blindness of Lexical Overlap
* The Vulnerability: System 0 misclassified 38 out of 53 unsupported citations (71.70%) as SUPPORT. Lexical overlap is easily satisfied by shared technical vocabulary, creating an illusion of attribution.
* The Fix: System 1 eliminated 81.58% of these false-support attributions (reducing errors from 38 to 7) and raised SUPPORT precision from 0.5309 to 0.8333.
* The Cost: System 1 incurs a ~44,000x latency penalty on CPU, motivating a two-tier cascaded architecture (lexical pruning followed by targeted neural verification).

---

## 4. Minimum Reproduction Protocol (Step-by-Step)

### Prerequisites
* Python 3.10+
* Standard CPU (no GPU required)

### Setup & Execution
```bash
# 1. Install pinned dependencies
pip install -r requirements.txt

# 2. Execute evaluation harness (runs in ~92 seconds on CPU)
python scripts/run_evaluation.py
```
