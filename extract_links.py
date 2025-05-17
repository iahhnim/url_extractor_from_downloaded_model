import os
import json
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Folder picker GUI
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory(title="Select root folder with .civitai.info files")
    
if not folder_path:
    print("No folder selected. Exiting.")
    exit()



# Output setup
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "output")
os.makedirs(output_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = os.path.join(output_dir, f"download_links_{timestamp}.txt")

# Track issues
missing_downloads = []
missing_previews = []
broken_files = []

# Walk all folders
with open(output_file, "w", encoding="utf-8") as out:
    for root_dir, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".civitai.info"):
                file_path = os.path.join(root_dir, filename)
                relative_path = os.path.relpath(file_path, folder_path)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    file_entry = data.get("files", [{}])[0]
                    image_entry = data.get("images", [{}])[0]

                    download_url = file_entry.get("downloadUrl", "")
                    preview_url = image_entry.get("url", "")

                    if not download_url:
                        missing_downloads.append(relative_path)
                    if not preview_url:
                        missing_previews.append(relative_path)

                    out.write(f"{relative_path}\n")
                    out.write(f"Download: {download_url if download_url else '❌ No download URL'}\n")
                    out.write(f"Preview: {preview_url if preview_url else '❌ No preview image'}\n\n")

                except Exception as e:
                    broken_files.append(relative_path)
                    out.write(f"{relative_path}\n❌ Error parsing file: {e}\n\n")

    # Report missing DOWNLOADS
    if missing_downloads:
        out.write("\n⚠️ Files with missing download URL:\n")
        for name in missing_downloads:
            out.write(f"- {name}\n")

    # Report missing PREVIEWS
    if missing_previews:
        out.write("\n⚠️ Files with missing preview image URL:\n")
        for name in missing_previews:
            out.write(f"- {name}\n")

    # Report broken JSONs
    if broken_files:
        out.write("\n❌ Files that could not be parsed (broken JSON):\n")
        for name in broken_files:
            out.write(f"- {name}\n")

# Save scan root to temp file for other scripts to read
with open(os.path.join(script_dir, "last_scan_root.txt"), "w", encoding="utf-8") as tmp:
    tmp.write(folder_path)

print(f"\n✅ Done! Output saved to:\n{output_file}")
if missing_downloads or missing_previews or broken_files:
    print("⚠️ Some files had issues. See the summary at the end of the output file.")
