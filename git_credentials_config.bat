@echo off
:: Rejestracja tokena w Git Credential Manager
:: Token generujesz na: https://github.com/settings/tokens

git config --global credential.helper manager
git config --global user.name "Marcin Paszkowski"
git config --global user.email "041985marcin@gmail.com"
echo ✅ Token może zostać zapamiętany przy następnym użyciu push/pull.
pause