import json
import os
from datetime import datetime


def generate_report():
    print(f"\n{'='*50}")
    print("VIDWAAN AI - EVALUATION REPORT")
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    report_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "docs", "retrieval_baseline.json"
    )

    if not os.path.exists(report_path):
        print(f"⚠️  No retrieval evaluation results found at {report_path}")
        print("Run 'make -f Makefile-docker docker-analyze' first.")
        return

    try:
        with open(report_path, "r") as f:
            data = json.load(f)

        # Map flat metrics to expected structure
        metrics = {
            "mean_precision_at_10": data.get("avg_precision", 0),
            "mean_recall_at_10": data.get("avg_recall", 0),
            "mean_mrr": data.get("avg_mrr", 0),
            "mean_ndcg": data.get("avg_ndcg", 0),  # Replaced f1 with ndcg as per output
        }
        query_results = data.get("queries", [])

        print("Type: Retrieval Evaluation")
        print(f"Total Queries: {len(query_results)}")
        print(f"{'-'*30}")
        print("Metrics:")
        print(f"  • Mean Precision@10: {metrics.get('mean_precision_at_10', 0):.4f}")
        print(f"  • Mean Recall@10:    {metrics.get('mean_recall_at_10', 0):.4f}")
        print(f"  • Mean MRR:          {metrics.get('mean_mrr', 0):.4f}")
        print(f"  • Mean NDCG:         {metrics.get('mean_ndcg', 0):.4f}")
        print(f"{'-'*30}\n")

        categories = data.get("categories", {})
        if categories:
            print("Category Breakdown:")
            print(
                f"{'Category':<15} | {'Queries':<7} | {'Prec@10':<7} | {'Rec@10':<7} | {'NDCG':<7}"
            )
            print(f"{'-'*15}-+-{'-'*7}-+-{'-'*7}-+-{'-'*7}-+-{'-'*7}")
            for cat, stats in categories.items():
                print(
                    f"{cat:<15} | {stats['num_queries']:<7} | {stats['avg_precision']:.2f}    | {stats['avg_recall']:.2f}    | {stats['avg_ndcg']:.2f}"
                )
            print(f"{'-'*50}\n")

        print("Detailed Query Performance (Top 5 lowest scoring):")
        # Sort by F1 score ascending
        sorted_results = sorted(query_results, key=lambda x: x.get("f1_score", 0))

        for i, res in enumerate(sorted_results[:5]):
            print(f" {i+1}. Query: '{res.get('query', 'N/A')}'")
            print(
                f"    Prec@10: {res.get('precision_at_10', 0):.2f}, Rec@10: {res.get('recall_at_10', 0):.2f}"
            )

    except Exception as e:
        print(f"❌ Error reading report: {e}")

    print(f"\n{'='*50}")


if __name__ == "__main__":
    generate_report()
