from collections import defaultdict

def correlate(data):
    counter = defaultdict(list)

    for item in data:
        counter[item["indicator"]].append(item["source"])

    results = []

    for indicator, sources in counter.items():
        severity = "Low"
        if len(sources) >= 2:
            severity = "High"

        results.append({
            "indicator": indicator,
            "count": len(sources),
            "severity": severity,
            "sources": sources
        })

    return results