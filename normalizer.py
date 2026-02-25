from datetime import datetime

def normalize(indicators, source_name):
    normalized = []

    for item in indicators:
        normalized.append({
            "indicator": item["indicator"],
            "type": item["type"],
            "source": source_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d")
        })

    return normalized