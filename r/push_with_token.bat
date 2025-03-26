@echo off
:: Skrypt do pushu z tokenem – UZUPEŁNIJ TOKEN!
:: Token generujesz na: https://github.com/settings/tokens

set TOKEN=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
set USER=Marcinpp1

git remote set-url origin https://%USER%:%TOKEN%@github.com/Marcinpp1/auto-evolution-gpt.git
git push origin main