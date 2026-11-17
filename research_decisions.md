### Research Decisions Log
**Project:**  Detecting Citation Drift in AI-Generated Literature Summaries
**Purpose:**  Portable record of decisions, reasons, supporting evidence, uncertainty, and next actions.
#### Decision 001 — Project constraints and preferred direction
*   **Decision:**  Use Python in Google Colab, without GPU dependence, for a postgraduate dissertation; prioritize direction A, a claim-level citation support detector.
*   **Status:**  VERIFIED — supplied directly by the user on 2026-10-21.
*   **Reason:**  Fits the stated environment and preferred research direction.
*   **Constraint:**  One day is available, so the initial target is a small pilot/prototype.
*   **Next action:**  Validate dataset and baseline feasibility before coding.
#### Decision 002 — Conditional implementation plan
*   **Decision:**  Start with a simple lexical or semantic baseline; add a pretrained natural-language-inference (NLI) verifier only if the selected data, dependencies, and CPU runtime support it.
*   **Status:**  INFERRED — proposed engineering plan, not yet tested.
*   **Reason:**  Avoids committing to costly training or GPU-dependent components.
*   **Evidence required:**  Successful Colab run, dependency versions, runtime notes, and actual evaluation output.
*   **Next action:**  Verify candidate dataset and baseline sources.
#### Decision 003 — Dataset-first gate
*   **Decision:**  Do not select a final model or define final labels until the dataset's annotation scheme and source-evidence availability are checked.
*   **Status:**  INFERRED — methodological safeguard.
*   **Reason:**  Claim-level support detection requires appropriate claim/evidence pairs and a defensible label mapping.
*   **Unknowns:**  Dataset access, license, label granularity, evidence spans, class balance, split design, and CPU feasibility.
*   **Next action:**  Check the original dataset paper and official data documentation.
#### Decision 004 — Separate unsupported from contradicted
*   **Decision:**  Keep “unsupported” distinct from “contradicted” wherever the dataset permits.
*   **Status:**  INFERRED — recommended annotation/evaluation principle.
*   **Reason:**  A source's failure to support a claim does not by itself establish that the source contradicts it.
*   **Constraint:**  Do not relabel data contrary to the original annotation scheme without documenting and justifying the transformation.
*   **Next action:**  Inspect the actual dataset label definitions.
#### Decision 005 — No unverified performance or novelty claims
*   **Decision:**  Report no performance numbers before running the experiment; make no novelty claim before a separate literature search.
*   **Status:**  VERIFIED — follows the user's explicit research requirements.
*   **Reason:**  Preserves research integrity and reproducibility.
*   **Next action:**  Record executed commands, versions, seeds, split strategy, metrics, and results once available.
#### Candidate research questions (provisional)
1. How effectively can a claim-level pipeline identify citation claims that are supported, unsupported, or contradicted by their cited evidence?
2. Does an explicit support-verification model improve performance over a simple lexical/semantic baseline under the same data split and evaluation protocol?
3. Which error types remain most common, and can errors be attributed to evidence retrieval versus support judgment if the dataset and pipeline expose both stages?
*   **Status:**  INFERRED / PROVISIONAL — these questions must be narrowed after dataset and source verification.
#### Candidate gaps (provisional; not novelty claims)
1. Fine-grained claim-level citation support evaluation.
2. Separating evidence-retrieval failures from support-judgment failures.
3. Robustness under domain or claim-specificity shifts.
4. Comparing simple and pretrained verification methods under a common protocol.
5. Measuring the quality/runtime trade-off of a multi-stage pipeline.
*   **Status:**  INFERRED — candidates derived from the literature-review analysis; not independently validated against the full current literature.
*   **Next action:**  Verify the original cited studies and perform a separate novelty search before selecting a final gap.
#### Change log
| Date | Change |
| ------ | ------ |
| 2026-10-21 | Created initial portable workspace and decision log from user-provided constraints and prior review analysis. |

