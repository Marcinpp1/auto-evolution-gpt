@echo off
echo 🔁 Pull z GitHuba z opcją scalania historii...

:: Zaciągnięcie historii remote (main) – auto-merge
git pull origin main --allow-unrelated-histories

:: Jeśli wystąpi edytor (vim), wpisz :wq i zatwierdź

echo ✅ Pull zakończony. Teraz możesz wykonać push.
pause