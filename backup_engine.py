import os, shutil, json
from datetime import datetime, timedelta
from zipfile import ZipFile
from upload_to_gdrive import upload_file
from send_email_report import send_email

base_dir = os.path.dirname(os.path.abspath(__file__))
snapshot_root = os.path.join(base_dir, "GPT_SYSTEM_RESTORE_POINT_FULL")
backup_folder = os.path.join(base_dir, "backups")
os.makedirs(backup_folder, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M')
zip_filename = f"PASZKO_PRO_BACKUP_vΩΩΩX_{timestamp}.zip"
zip_path = os.path.join(base_dir, zip_filename)

def log_alert(msg):
    with open(os.path.join(base_dir, "ALERTS.log"), "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def append_status_row(status_dict):
    csv_path = os.path.join(base_dir, "DAILY_BACKUP_STATUS.csv")
    header = "data,czas,status_backupu,status_github,status_gdrive,status_email,plik"
    if not os.path.exists(csv_path):
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write(header + "\n")
    with open(csv_path, "a", encoding="utf-8") as f:
        f.write(",".join(status_dict.values()) + "\n")

def cleanup_old_backups(folder, days=7):
    now = datetime.now()
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        if os.path.isfile(fpath):
            created = datetime.fromtimestamp(os.path.getctime(fpath))
            if now - created > timedelta(days=days):
                os.remove(fpath)

# Katalogi zgodne z docelową strukturą
required_dirs = [
    "changelog", "config", "engine", "logs", "markdown",
    "memory", "projects", "setup", "tasks", "trained_skills", "backups"
]

# 1. Czyszczenie starych backupów
cleanup_old_backups(backup_folder)

# 2. Tworzenie ZIP-a
status = {"backup": "OK", "github": "PENDING", "gdrive": "FAIL", "email": "FAIL"}
try:
    with ZipFile(zip_path, 'w') as zipf:
        # Puste foldery strukturalne
        for folder in required_dirs:
            zipf.write(os.path.join(base_dir), arcname=folder)  # placeholder

        # Dodanie plików przywracania systemu (jeśli są)
        for file in [
            "SYSTEM_MANIFEST.json",
            "GPT_STATE_RESTORE.instruction.txt",
            "SETTINGS_PASZKO_PRO.env",
            "USER_CONTEXT_snapshot.yaml",
            "README_RESTORE.txt",
            "CHAT_MEMORY_INDEX.json",
            "CUSTOM_GPT_PROFILE.json",
            "PASZKO_SYSTEM_MANIFEST_vOmega.json"
        ]:
            path = os.path.join(base_dir, file)
            if os.path.exists(path):
                zipf.write(path, os.path.basename(path))

        # Dodanie ostatnich backupów ZIP do backups/
        if os.path.exists(backup_folder):
            for f in os.listdir(backup_folder):
                fpath = os.path.join(backup_folder, f)
                arcname = os.path.join("backups", os.path.basename(f))
                zipf.write(fpath, arcname)

    shutil.copy2(zip_path, os.path.join(backup_folder, os.path.basename(zip_path)))
except Exception as e:
    log_alert(f"ZIP ERROR: {str(e)}")
    status["backup"] = "FAIL"

# 3. Upload GDrive
try:
    gdrive_link = upload_file(zip_path)
    status["gdrive"] = "OK"
except Exception as e:
    log_alert(f"GDRIVE ERROR: {str(e)}")

# 4. E-mail
try:
    send_email("🧠 GPT Backup - Daily Snapshot",
               f"Nowy backup został utworzony.\n\nPlik ZIP: {os.path.basename(zip_path)}\nLink do Google Drive:\n{gdrive_link}",
               zip_path)
    status["email"] = "OK"
except Exception as e:
    log_alert(f"EMAIL ERROR: {str(e)}")

# 5. Rejestracja statusu
append_status_row({
    "data": datetime.now().strftime('%Y-%m-%d'),
    "czas": datetime.now().strftime('%H:%M'),
    "status_backupu": status["backup"],
    "status_github": status["github"],
    "status_gdrive": status["gdrive"],
    "status_email": status["email"],
    "plik": zip_filename
})
