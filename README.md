# 🧠 Civitai Link Extractor Toolset

This toolset helps you extract, clean, group, and organize download links from `.civitai.info` files used in Stable Diffusion model datasets (e.g., LoRA, checkpoints, etc.).

---

## 📁 Project Structure

```
.
├── extract_links.py                 # Step 1: Extracts raw download & preview URLs
├── cleaned_download_links.py       # Step 2: Cleans URLs into flat list
├── grouped_cleaned_download_links.py # Step 3: Groups URLs by folder structure
├── append_subfolder_tag.py         # Optional: Adds ::Subfolder=... tags
├── archive_old_outputs.py          # Archives old .txt logs from output folders
├── original_links.txt              # Input for tag append tool
├── updated_links.txt               # Output with ::Subfolder tags
├── run_all.bat                     # Runs all 3 steps: extract → clean → group
├── append_tag_run.bat              # Runs tag appending tool
├── archive_old_outputs.bat         # Runs archive script
├── output/                         # Stores full extraction results
├── cleaned_output/                 # Stores cleaned links only
├── grouped_output/                 # Stores folder-grouped links
├── archive_old_outputs/           # Where old outputs are moved
```

---

## 🚀 Usage

###  1: Extract all info
Run:
```bash
run_all.bat
```
This performs:
- 📂 Folder popup: Select folder containing `.civitai.info` files
- ✅ Extracts full model info
- ✅ Extracts only valid download links
- ✅ Groups download links by original folder structure

---

### 2: Tag your links (Optional)
Run:
```bash
append_tag_run.bat
```
- Prompts you to enter a tag (e.g. `face_lora`, `nsfw`, etc.)
- Adds tag to each line in `original_links.txt`
- Saves to `updated_links.txt`

Output format:
```
https://civitai.com/api/download/models/123456::Subfolder=face_lora
```

---

###  3: Archive older output files
Run:
```bash
archive_old_outputs.bat
```
- Moves all `.txt` files except the latest from:
  - `output/`
  - `cleaned_output/`
  - `grouped_output/`
- To: `archive_old_outputs/<folder>/`

---

## 🛠 Dependencies

- Python 3.8+
- No external packages required
- Uses standard libraries: `os`, `json`, `tkinter`, `datetime`, `re`, `shutil`

---

## 💡 Tips

- Works well with thousands of `.civitai.info` files
- Grouped output preserves subfolders like `face/smile/`, `nsfw/furry/`
- You can run each `.py` script separately if needed
- Ideal for dataset cleanup or batch re-download setups

---

## 🧑‍💻 Author

Developed by iahhnim and ChatGPT for managing Civitai-based SD datasets efficiently.

---

## 📄 License

MIT License — use, modify, or adapt freely.