import os, json, sys
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
projects_dir = os.path.join(base_dir, "projects")
manifest_path = os.path.join(base_dir, "PROJECTS_MANIFEST.json")

def load_manifest():
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"projects": []}

def save_manifest(data):
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_project(entry_file):
    entry_path = os.path.join(projects_dir, entry_file)
    if not os.path.exists(entry_path):
        print(f"[ERROR] Nie znaleziono: {entry_path}")
        return

    with open(entry_path, "r", encoding="utf-8") as f:
        entry = json.load(f)

    manifest = load_manifest()
    manifest["projects"].append(entry)
    save_manifest(manifest)
    print(f"[✓] Dodano projekt: {entry['project_id']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python ADD_PROJECT_HELPER.py [nazwa_pliku.json]")
    else:
        add_project(sys.argv[1])
