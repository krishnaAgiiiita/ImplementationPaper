# Human-AI Collaboration & Research Integrity Log
(Conforming to ATR_Task Milestone Gate G4 & Prompt 18)

## 1. Project Information
* **Project Title:** Detecting Citation Drift in AI-Generated Literature Summaries
* **Student Role:** Primary Researcher & Evaluator
* **AI Assistance Role:** Supervised Technical Pair Programmer & Scaffold Writer (Gemini Notebook)
* **Date:** November 2026

---

## 2. Activity Provenance Matrix

| Milestone Activity | Prompt / Interaction | AI Proposal | Human Review & Decision | Verification Method | Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Gap Identification** | Prompt 01 & 02 | Proposed 5 candidate gaps from literature review. | Selected Gap 4 (Lexical vs. Pretrained NLI trade-off on CPU) due to strict 1-day timeline. | Cross-referenced against review scope in `review_scope.md`. | Research direction anchored to CPU-feasible comparative study. |
| **Stage 2: Dataset Selection** | Prompt 06 & 08 | Suggested direct download of SciFact without corpus mapping. | Identified schema error (`ValueError: Dataset is empty!`) during execution. | Inspected dataset dictionary structure and SciFact documentation. | Specified fallback loader to `allenai/scitail` (`snli_format`) ensuring non-empty extraction. |
| **Stage 3: Experiment Execution** | Prompt 08 & 09 | Emitted modular Python evaluation script. | Verified that script runs strictly under `torch.no_grad()` on CPU without training. | Executed script in Google Colab; captured genuine terminal log. | Empirical metrics generated for $N=100$ samples without GPU dependence. |
| **Stage 4: Manuscript Drafting** | Prompt 15 | Drafted complete LaTeX manuscript incorporating exact metrics. | Audited all table values against Colab execution logs. | Re-checked every cell of confusion matrix in `Output` note. | 100% data fidelity: zero fabricated metrics or hallucinated p-values. |

---

## 3. Real Examples of AI Limitations & Manual Corrections
1. **Schema Parsing Error in SciFact:** The AI initially wrote an ingestion loop expecting `item["evidence"]` to be a plain string. In `allenai/scifact`, evidence is stored as a nested dictionary keyed by document ID. When executed, this threw a `ValueError: Dataset is empty!`. The student prompted the AI to structure a formal code-generation prompt with a robust fallback handler to `allenai/scitail`.
2. **Over-Generalization of Macro-F1:** Standard 3-class Macro-F1 averages across all 3 classes (including `CONTRADICT`, which had 0 ground-truth examples). The student ensured the manuscript explicitly reported both the 3-class Macro-F1 (0.4913) and the active 2-class binary Macro-F1 (0.7370) to prevent misleading interpretations.
3. **Hardware Latency Calibration:** The AI originally projected inference times based on GPU environments. Under human supervision, the actual CPU execution was profiled at 920.75 ms/sample, prompting the formulation of the Two-Tier Cascaded Architecture in the Discussion section.

---

## 4. Statement of Research Ownership
All code was inspected, executed, and validated by the student. Reported results derive strictly from authentic executions on public benchmarks. No proprietary weights or confidential credentials were used.
