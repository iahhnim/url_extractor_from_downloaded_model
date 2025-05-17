import os
import shutil

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
output_folders = ["output", "cleaned_output", "grouped_output"]
archive_base = os.path.join(script_dir, "archive_old_outputs")
os.makedirs(archive_base, exist_ok=True)

for folder_name in output_folders:
    folder_path = os.path.join(script_dir, folder_name)
    archive_subfolder = os.path.join(archive_base, folder_name)
    os.makedirs(archive_subfolder, exist_ok=True)

    if not os.path.exists(folder_path):
        print(f"⚠️ Folder not found: {folder_path}")
        continue

    txt_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".txt")
    ]

    if not txt_files:
        print(f"ℹ️ No .txt files in: {folder_name}")
        continue

    latest_file = max(txt_files, key=os.path.getmtime)

    for f in txt_files:
        if f != latest_file:
            target = os.path.join(archive_subfolder, os.path.basename(f))
            shutil.move(f, target)
            print(f"📦 Moved: {f} → {target}")

print("\n✅ All older outputs archived in 'archive_old_outputs/<folder>/'")
