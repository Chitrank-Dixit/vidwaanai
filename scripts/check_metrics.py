#!/usr/bin/env python3
"""
Regression test script to check if retrieval metrics meet defined thresholds.
Acts as a Quality Gate in the CI/CD pipeline.
"""

import json
import os
import sys


def check_metrics():
    # Define thresholds
    THRESHOLDS = {
        "mean_recall_at_10": 0.70,
        "mean_precision_at_10": 0.05,  # Low baseline for top-k
    }

    report_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "docs", "retrieval_baseline.json"
    )

    if not os.path.exists(report_path):
        print(f"❌ Report not found at {report_path}")
        sys.exit(1)

    with open(report_path, "r") as f:
        data = json.load(f)

    # Handle different schema versions (flat vs nested metrics)
    # The new evaluate_retrieval.py schema has 'metrics' key?
    # Wait, RetrieverEvaluator.generate_report() returns dict with 'avg_precision' keys at top level usually?
    # Let's check schema. evaluate_retrieval.py sets:
    # report["categories"][cat] = ...
    # And base report has keys: avg_precision, avg_recall, etc.

    # Map from report keys to threshold keys
    metrics = {
        "mean_recall_at_10": data.get("avg_recall", 0),
        "mean_precision_at_10": data.get("avg_precision", 0),
    }

    failed = False
    print("\n🔍 Checking Quality Gate Thresholds...")
    print(f"{'-'*40}")

    for metric, threshold in THRESHOLDS.items():
        val = metrics.get(metric, 0)
        status = "✅ PASS" if val >= threshold else "❌ FAIL"
        if val < threshold:
            failed = True
        print(f"{metric:<25}: {val:.4f} (Target: >={threshold}) {status}")

    print(f"{'-'*40}")

    if failed:
        print("🚨 Quality Gate FAILED. Metrics are below acceptable thresholds.")
        sys.exit(1)
    else:
        print("✨ Quality Gate PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    check_metrics()
