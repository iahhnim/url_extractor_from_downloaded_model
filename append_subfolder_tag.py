# append_subfolder_tag.py
import tkinter as tk
from tkinter import simpledialog

# Prompt for suffix
root = tk.Tk()
root.withdraw()
suffix_input = simpledialog.askstring("Enter Folder Name", "Enter the folder name to tag each link (used in ::Subfolder=...):")
if not suffix_input:
    print("❌ No folder name entered. Exiting.")
    exit()

suffix = f"::Subfolder={suffix_input}"

# Paths
input_file = "original_links.txt"
output_file = "updated_links.txt"

# Read and process
with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

updated_lines = [line.strip() + suffix + "\n" for line in lines if line.strip()]

# Write result
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(updated_lines)

print(f"✅ Updated links saved to: {output_file}")
