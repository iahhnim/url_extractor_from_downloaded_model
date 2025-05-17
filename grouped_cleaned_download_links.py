import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "output")
grouped_dir = os.path.join(script_dir, "grouped_output")
os.makedirs(grouped_dir, exist_ok=True)

# Load scan root
scan_root_path = os.path.join(script_dir, "last_scan_root.txt")
if not os.path.exists(scan_root_path):
    print("❌ Could not find scan root info (last_scan_root.txt). Run extract_links.py first.")
    exit()

with open(scan_root_path, "r", encoding="utf-8") as f:
    scan_root = f.read().strip()

# Find latest output file
txt_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".txt")]
if not txt_files:
    print("❌ No .txt files in output/")
    exit()

latest_txt = max(txt_files, key=os.path.getmtime)

# Track grouping
grouped = {}

with open(latest_txt, "r", encoding="utf-8") as f:
    lines = f.readlines()

current_file_path = None

for line in lines:
    line = line.strip()

    # Only update when seeing a new .civitai.info file
    if line.endswith(".civitai.info"):
        current_file_path = os.path.join(scan_root, line)

    elif line.startswith("Download: https://civitai.com/api/download/models/"):
        url = line.replace("Download: ", "")
        if current_file_path:
            file_dir = os.path.dirname(current_file_path)
            try:
                rel_path = os.path.relpath(file_dir, scan_root)
                category = rel_path.replace(os.sep, "/") if rel_path != "." else os.path.basename(scan_root)
            except Exception:
                category = os.path.basename(scan_root)
            grouped.setdefault(category, []).append(url)

        # Reset path so it doesn't carry over
        current_file_path = None

# Save output
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(grouped_dir, f"grouped_download_links_{timestamp}.txt")

with open(output_file, "w", encoding="utf-8") as out:
    for category, urls in grouped.items():
        out.write(f"{category}:\n")
        for url in urls:
            out.write(f"{url}\n")
        out.write("\n")

print(f"✅ Grouped links saved to:\n{output_file}")
