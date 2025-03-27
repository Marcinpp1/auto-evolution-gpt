@echo off
cd /d %~dp0
git add .
git commit -m "Automated daily backup %date% %time%"
git push origin main
