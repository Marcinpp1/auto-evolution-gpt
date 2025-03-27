import os, json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
drafts_dir = os.path.join(base_dir, "drafts")
projects_dir = os.path.join(base_dir, "projects")
os.makedirs(drafts_dir, exist_ok=True)
os.makedirs(projects_dir, exist_ok=True)

manifest_path = os.path.join(base_dir, "PROJECTS_MANIFEST.json")
projects = [
    "GPT", "GABRYSIA", "GIEŁDA I KRYPTO", "Sklep", "ZABAWA", "ASYSTENCI", "Projektowanie"
]

def mock_draft_md(project):
    return f"""# Projekt: {project}

Status: roboczy
Ostatnia aktualizacja: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Cele:
- Częściowe zadania i eksperymenty
- Testy GPT, checklisty, pomysły

## Notatki:
(To miejsce może być uzupełniane przez GPT automatycznie)

"""

def load_manifest():
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"projects": []}

def save_manifest(data):
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

manifest = load_manifest()

for project in projects:
    filename = f"DRAFT_{project.upper().replace(' ', '_')}.md"
    filepath = os.path.join(drafts_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(mock_draft_md(project))

    manifest["projects"].append({
        "project_id": f"{project.upper()}_DRAFT",
        "title": f"Zapis roboczy: {project}",
        "category": "projekty robocze GPT",
        "status": "in-progress",
        "created": datetime.now().isoformat(),
        "files": [filename],
        "tags": ["GPT", "robocze", project.lower()]
    })

save_manifest(manifest)
print("[✓] Wygenerowano snapshot projektów roboczych.")
