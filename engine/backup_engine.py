import os
import datetime
import subprocess
import json

REPO_PATH = "/ścieżka/do/repo"  # <-- UZUPEŁNIJ
BACKUP_FOLDER = "setup/backups"
BRANCH = "main"
GPT_MEMORY_PATH = "setup/gpt_memory/"
LOG_PATH = "setup/logs/backup_log.json"

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def backup_gpt_memory():
    if not os.path.exists(GPT_MEMORY_PATH):
        return "📂 Brak pamięci GPT do backupu."
    
    today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"gpt_memory_backup_{today}.zip"
    zip_path = os.path.join(REPO_PATH, BACKUP_FOLDER, zip_name)
    subprocess.run(["zip", "-r", zip_path, GPT_MEMORY_PATH], check=True)
    return f"🧠 Pamięć GPT zapisana jako: {zip_name}"

def log_backup(status, details):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    log_entry = {
        "timestamp": get_timestamp(),
        "status": status,
        "details": details
    }
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry) + "\n")

def commit_and_push():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"🔄 AutoBackup GPT – {get_timestamp()}"], check=True)
    subprocess.run(["git", "push", "origin", BRANCH], check=True)

def run_backup():
    try:
        print("🧠 AutoBackup – start")
        status = backup_gpt_memory()
        log_backup("✅", status)
        commit_and_push()
        print("🚀 Backup i push zakończone sukcesem.")
    except Exception as e:
        log_backup("❌", str(e))
        print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    run_backup()