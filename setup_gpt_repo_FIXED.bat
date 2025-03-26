@echo off
echo 🧠 Inicjalizacja repozytorium GPT...
cd /d %~dp0

:: Konfiguracja użytkownika Git (jeśli brak)
git config --global user.name "Marcin Paszkowski"
git config --global user.email "041985marcin@gmail.com"

:: Inicjalizacja repo (jeśli nie istnieje)
if not exist ".git" (
    git init
)

:: Dodanie zdalnych repozytoriów, jeśli nie istnieją
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/Marcinpp1/auto-evolution-gpt.git
    git remote set-url --add --push origin https://github.com/Marcinpp1/setup.git
)

:: Dodanie plików i commit
git add .
git commit -m "🚀 Initial GPT system backup commit"

:: Ustawienie branch i wypchnięcie na GitHub
git branch -M main
git push -u origin main

echo ✅ Repozytorium zostało poprawnie skonfigurowane i wypchnięte.
pause