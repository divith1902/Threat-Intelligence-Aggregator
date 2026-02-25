def generate_blocklists(correlated_data):
    ip_list = []
    domain_list = []
    hash_list = []
    url_list = []

    for item in correlated_data:
        if item["severity"] == "High":
            indicator = item["indicator"]

            if indicator.startswith("http"):
                url_list.append(indicator)
            elif "." in indicator:
                domain_list.append(indicator)
            else:
                ip_list.append(indicator)

    with open("ip_blocklist.txt", "w") as f:
        f.write("\n".join(ip_list))

    with open("domain_blocklist.txt", "w") as f:
        f.write("\n".join(domain_list))

    with open("url_blocklist.txt", "w") as f:
        f.write("\n".join(url_list))