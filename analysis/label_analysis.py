# analysis/label_analysis.py
from collections import Counter

def analyze_issue_labels(issues):
    label_counts = Counter()
    for issue in issues:
        labels = issue.get("labels", [])
        label_counts.update(labels)
    return label_counts
