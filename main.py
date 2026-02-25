import os
from parser import parse_file
from normalizer import normalize
from correlator import correlate
from blocklist_generator import generate_blocklists
from report_generator import generate_report

all_data = []

feeds_folder = "feeds"

for file in os.listdir(feeds_folder):
    path = os.path.join(feeds_folder, file)

    parsed = parse_file(path)
    normalized = normalize(parsed, file)
    all_data.extend(normalized)

correlated = correlate(all_data)

generate_blocklists(correlated)
generate_report(correlated)