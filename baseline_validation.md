# Baseline Validation & Reproduction Report
(Conforming to ATR_Task Milestone Gate G2 & Prompt 10)

## 1. Baseline Implementation Audit
* **Target Method:** Lexical Overlap Baseline (Token Jaccard Heuristic) vs. Pretrained NLI Verifier (Cross-Encoder Transformer).
* **Reference Literature:** Sarol et al. (2024), Gao et al. (2023) [ALCE], Wadden et al. (2020) [SciFact], and Khot et al. (2018) [SciTail].
* **Execution Environment:** Google Colab / Standard Linux CPU, Seed = 42, deterministic zero-shot inference.

---

## 2. Validation Checklist (VERIFIED / UNCERTAIN / NEEDS CORRECTION)

### [VERIFIED] Data Partition & Schema Alignment
* Dataset loaded: `allenai/scitail` (`snli_format`, test split).
* Total evaluated triplets: $N = 100$.
* Label distribution: `NO_EVIDENCE` (53%), `SUPPORT` (47%), `CONTRADICT` (0%).
* Input shapes: Claim string (hypothesis) aligned with premise passage (evidence).

### [VERIFIED] Comparator Execution & Metric Direction
* Deterministic lexical Jaccard calculated across lowercased alphanumeric tokens.
* Dual decision boundary ($\tau = 0.15$): $\ge 0.15 \rightarrow \text{SUPPORT}$, else $\text{NO\_EVIDENCE}$.
* Cross-encoder forward pass executed under `torch.no_grad()` on CPU.
* Output confusion matrices verified: rows represent Ground Truth, columns represent Model Prediction.

### [VERIFIED] Runtime Latency Profiling
* Jaccard Baseline total runtime ($N=100$): 0.0021 seconds (0.021 ms/sample).
* Pretrained Cross-Encoder total runtime ($N=100$): 92.075 seconds (920.750 ms/sample).
* Computational slowdown factor: $\sim 43,845\times$.

---

## 3. Discrepancy & Adaptation Notes
1. **Primary Dataset Fallback:** Ingestion originally attempted `allenai/scifact`. Due to schema divergence (empty nested dictionary parsing for rationale-free claims), the automated fallback successfully engaged `allenai/scitail`.
2. **Label Space Shift:** SciTail represents a natural 2-class distribution (`neutral` vs. `entails`) mapped to the standard 3-class NLI space. The zero ground-truth instances of `CONTRADICT` isolate the specific challenge of attribution drift: distinguishing substantiated scientific claims from ungrounded claims that mimic technical vocabulary.
