@echo off
echo 🧠 Inicjalizacja repozytorium GPT...
cd /d %~dp0

:: Inicjalizacja git
git init
git branch -M main

:: Podpięcie zdalnych repozytoriów
git remote add origin https://github.com/Marcinpp1/auto-evolution-gpt.git
git remote set-url --add --push origin https://github.com/Marcinpp1/auto-evolution-gpt.git
git remote set-url --add --push origin https://github.com/Marcinpp1/setup.git

:: Pierwszy commit
git add .
git commit -m "🚀 Initial GPT system backup commit"

:: Push na oba repozytoria
git push -u origin main

echo ✅ Gotowe! Repozytorium zostało utworzone i wypchnięte na GitHub.
pause