import sys
import json

file = "/tmp/registry_network_info.json"
with open(file, "r") as f:
    json_lines = json.load(f)  # Read the JSON list of strings

# Check if json_lines is a list of strings
if isinstance(json_lines, list) and all(isinstance(line, str) for line in json_lines):
    json_string = "".join(json_lines)  # Join into a valid JSON format
    data = json.loads(json_string)  # Parse JSON
else:
    data = json_lines  # Assume already parsed JSON

# Extract only IPv4 addresses
ipv4_addresses = [
    ip_entry["ip-address"]
    for interface in data
    for ip_entry in interface["ip-addresses"]
    if ip_entry["ip-address-type"] == "ipv4"
]

print(ipv4_addresses[-1])
sys.exit(0)