Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "schtasks /create /tn GPT_Weekly_Project_Backup /tr \"%~dp0weekly_project_export.bat\" /sc weekly /d FRI /st 21:00", 0, True
