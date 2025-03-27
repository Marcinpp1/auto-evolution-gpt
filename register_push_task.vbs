Set objShell = CreateObject("WScript.Shell")
strCmd = "SCHTASKS /Create /SC DAILY /TN ""GPT_RunAndPush"" /TR """ & Replace(WScript.ScriptFullName, "register_push_task.vbs", "run_and_push_FIXED.bat") & """ /ST 07:00 /RL HIGHEST /F"
objShell.Run strCmd, 0, True