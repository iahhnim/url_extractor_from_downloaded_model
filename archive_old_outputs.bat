@echo off
cd /d "%~dp0"
echo Archiving old .txt outputs...
python archive_old_outputs.py
pause
