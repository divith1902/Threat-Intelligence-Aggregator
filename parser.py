import re
import ipaddress

def parse_file(filepath):
    indicators = []

    with open(filepath, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # IP validation
        try:
            ipaddress.ip_address(line)
            indicators.append({"indicator": line, "type": "IP"})
            continue
        except:
            pass

        # URL detection
        if line.startswith("http"):
            indicators.append({"indicator": line, "type": "URL"})
            continue

        # Hash detection (simple check)
        if re.fullmatch(r"[a-fA-F0-9]{32,64}", line):
            indicators.append({"indicator": line, "type": "HASH"})
            continue

        # Domain detection
        if "." in line:
            indicators.append({"indicator": line, "type": "DOMAIN"})

    return indicators