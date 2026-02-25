def generate_report(correlated_data):
    total = len(correlated_data)
    high = sum(1 for item in correlated_data if item["severity"] == "High")

    print("\n--- Threat Intelligence Report ---")
    print(f"Total Indicators: {total}")
    print(f"High Severity Indicators: {high}")

    for item in correlated_data:
        if item["severity"] == "High":
            print(f"[HIGH] {item['indicator']} appears in {item['count']} feeds")