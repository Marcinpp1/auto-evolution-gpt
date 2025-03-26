@echo off
echo 🧠 Uruchamianie AutoBackup GPT...

:: Backup danych
python engine\backup_engine.py

:: Wysyłka na GitHub
call push_with_token.bat

echo ✅ Backup i push zakończone pomyślnie.
pause