@echo off
echo 🔥 Trwa czyszczenie historii GIT z pliku push_with_token.bat...

git filter-branch --force --index-filter ^
  "git rm --cached --ignore-unmatch push_with_token.bat" ^
  --prune-empty --tag-name-filter cat -- --all

echo ✅ Historia wyczyszczona. Wykonaj force push:
echo git push --force --all
pause