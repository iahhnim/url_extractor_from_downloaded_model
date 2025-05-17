import os
import re
from datetime import datetime

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_dir, "output")
clean_folder = os.path.join(script_dir, "cleaned_output")  # ✅ renamed here
os.makedirs(clean_folder, exist_ok=True)

# Find latest .txt file in output folder
txt_files = [
    os.path.join(output_folder, f)
    for f in os.listdir(output_folder)
    if f.endswith(".txt")
]
if not txt_files:
    print("❌ No .txt files found in 'output' folder.")
    exit()

latest_txt = max(txt_files, key=os.path.getmtime)

# Extract download links
download_links = []
with open(latest_txt, "r", encoding="utf-8") as file:
    for line in file:
        match = re.match(r"Download:\s*(https://civitai\.com/api/download/models/\d+)", line.strip())
        if match:
            download_links.append(match.group(1))

# Write to cleaned_output/ folder
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(clean_folder, f"cleaned_download_links_{timestamp}.txt")

with open(output_file, "w", encoding="utf-8") as out:
    for url in download_links:
        out.write(url + "\n")

print(f"✅ Extracted {len(download_links)} links from:\n{latest_txt}")
print(f"📄 Saved to:\n{output_file}")
