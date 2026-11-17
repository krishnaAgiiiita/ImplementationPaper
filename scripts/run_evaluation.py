"""
Execution entrypoint for citation-drift verification experiment.
"""

import time
import json
import torch
import numpy as np
from datasets import load_dataset
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def run_experiment(sample_size: int = 100, seed: int = 42):
    torch.manual_seed(seed)
    np.random.seed(seed)
    
    print("[1/4] Ingesting evaluation benchmark...")
    try:
        ds = load_dataset("allenai/scitail", "snli_format", split="test")
    except Exception as e:
        raise RuntimeError(f"Failed to load dataset: {e}")
        
    label_map = {"neutral": 1, "entails": 2}
    data = []
    for item in ds:
        gold = item.get("gold_label", "").lower()
        if gold in label_map:
            data.append({
                "evidence": item["sentence1"],
                "claim": item["sentence2"],
                "label": label_map[gold]
            })
        if len(data) >= sample_size:
            break
            
    gold = [d["label"] for d in data]
    
    print("[2/4] Executing System 0: Lexical Jaccard Baseline...")
    j_preds = []
    t0 = time.time()
    for d in data:
        c_tok = set(d["claim"].lower().split())
        e_tok = set(d["evidence"].lower().split())
        j = len(c_tok & e_tok) / len(c_tok | e_tok) if (c_tok | e_tok) else 0.0
        j_preds.append(2 if j >= 0.15 else 1)
    j_time = time.time() - t0
    
    print("[3/4] Executing System 1: Pretrained Cross-Encoder NLI...")
    model_name = "cross-encoder/nli-distilroberta-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.eval()
    
    nli_preds = []
    t1 = time.time()
    with torch.no_grad():
        for d in data:
            inputs = tokenizer(d["claim"], d["evidence"], truncation=True, max_length=256, return_tensors="pt")
            logits = model(**inputs).logits
            nli_preds.append(int(torch.argmax(logits, dim=1).item()))
    nli_time = time.time() - t1
    
    print("[4/4] Outputting verification metrics...")
    target_names = ["CONTRADICT (0)", "NO_EVIDENCE (1)", "SUPPORT (2)"]
    print("--- SYSTEM 0 REPORT ---")
    print(classification_report(gold, j_preds, target_names=["NO_EVIDENCE (1)", "SUPPORT (2)"], zero_division=0))
    print("Confusion Matrix:\n", confusion_matrix(gold, j_preds))
    print(f"Latency: {j_time/sample_size*1000:.3f} ms/sample")
    
    print("\n--- SYSTEM 1 REPORT ---")
    print(classification_report(gold, nli_preds, labels=[0, 1, 2], target_names=target_names, zero_division=0))
    print("Confusion Matrix:\n", confusion_matrix(gold, nli_preds, labels=[0, 1, 2]))
    print(f"Latency: {nli_time/sample_size*1000:.3f} ms/sample")

if __name__ == "__main__":
    run_experiment()
