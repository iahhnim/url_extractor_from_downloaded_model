@echo off
cd /d "%~dp0"
echo =====================================
echo   Starting full URL extraction run
echo =====================================

:: Step 1: Extract raw info
echo Running extract_links.py ...
python extract_links.py

:: Step 2: Extract cleaned download URLs
echo Running cleaned_download_links.py ...
python cleaned_download_links.py

:: Step 3: Group by folder structure
echo Running grouped_cleaned_download_links.py ...
python grouped_cleaned_download_links.py

echo =====================================
echo  All tasks completed.
pause
