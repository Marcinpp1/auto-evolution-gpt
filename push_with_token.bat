@echo off
:: Skrypt do pushu z tokenem – UZUPEŁNIJ TOKEN!
:: Token generujesz na: https://github.com/settings/tokens

set TOKEN=GH_TOKEN_TUTAJ
set USER=Marcinpp1

git remote set-url origin https://%USER%:%TOKEN%@github.com/Marcinpp1/auto-evolution-gpt.git
git push origin main