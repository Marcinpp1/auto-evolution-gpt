@echo off
cd /d %~dp0
echo [GPT] Aktualizuję stan sesji do memory/GPT_STATE_CURRENT.json...
python generate_gpt_system_snapshot.py
echo [✓] Aktualizacja zakończona.
pause
