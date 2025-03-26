@echo off
cd /d %~dp0
echo 🧠 Uruchamianie AutoBackup GPT...

:: Backup danych
python engine\backup_engine.py

:: Push na GitHub
call push_with_token.bat

echo ✅ Backup i push zakończone pomyślnie.
pause