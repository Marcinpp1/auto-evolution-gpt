@echo off
echo 🧠 Włączanie Git Credential Manager...

git config --global credential.helper manager
git config --global user.name "Marcin Paszkowski"
git config --global user.email "041985marcin@gmail.com"

echo ✅ Git Credential Manager aktywny. Token będzie zapamiętany lokalnie.
pause