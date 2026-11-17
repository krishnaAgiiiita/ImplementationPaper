"""
Source modules for claim-level citation support verification.
"""

from typing import List, Dict, Set, Tuple
import re

def compute_jaccard_overlap(claim: str, evidence: str) -> float:
    """Computes token-level Jaccard similarity across lowercased alphanumeric tokens."""
    claim_tokens = set(re.findall(r'\b\w+\b', claim.lower()))
    evidence_tokens = set(re.findall(r'\b\w+\b', evidence.lower()))
    if not claim_tokens or not evidence_tokens:
        return 0.0
    intersection = claim_tokens.intersection(evidence_tokens)
    union = claim_tokens.union(evidence_tokens)
    return len(intersection) / len(union) if union else 0.0

def predict_jaccard(claim: str, evidence: str, threshold: float = 0.15) -> int:
    """
    Predicts citation support label:
    2: SUPPORT (if overlap >= threshold)
    1: NO_EVIDENCE (sub-threshold overlap)
    """
    j = compute_jaccard_overlap(claim, evidence)
    return 2 if j >= threshold else 1
