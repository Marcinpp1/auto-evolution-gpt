Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "schtasks /create /tn GPT_Backup_03AM /tr "%~dp0run_backup_daily.bat" /sc daily /st 03:00", 0, True
