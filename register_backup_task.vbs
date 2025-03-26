Set objShell = CreateObject("WScript.Shell")
strCmd = "SCHTASKS /Create /SC DAILY /TN ""GPT_AutoBackup"" /TR """ & Replace(WScript.ScriptFullName, "register_backup_task.vbs", "run_backup_daily.bat") & """ /ST 07:00"
objShell.Run strCmd, 0, True