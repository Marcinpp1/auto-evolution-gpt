import os, json
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))

def write_json(filename, data):
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# SYSTEM_MANIFEST
write_json("SYSTEM_MANIFEST.json", {
    "system_version": "PASZKO_PRO | vΩ.ΩΩΩX",
    "mode": "ULTRASINGULARITY MODE™ + STRATEGIC INTELLIGENCE MODE 3.0",
    "status": "ACTIVE",
    "timestamp": datetime.now().isoformat()
})

# PASZKO_SYSTEM_MANIFEST_vOmega
write_json("PASZKO_SYSTEM_MANIFEST_vOmega.json", {
    "manifest_name": "PASZKO_SYSTEM_MANIFEST_vOmega",
    "last_generated": datetime.now().isoformat(),
    "modules": ["NEUROSYNC CORE™", "AI DECISION SNIPER™", "AUTOEVOLUTION LOOP™"]
})

# CUSTOM_GPT_PROFILE
write_json("CUSTOM_GPT_PROFILE.json", {
    "user": "Gabrysia",
    "protocols": ["NEUROPROTOCOL", "CBD_THERAPY", "EMOTIONAL_SUPPORT"],
    "active_modules": ["ULTRASINGULARITY", "HYPERFOCUS", "COMPLIANCE MATRIX™"]
})

# CHAT_MEMORY_INDEX
write_json("CHAT_MEMORY_INDEX.json", {
    "index": ["SESSION_START", "MODE_UPDATE", "PROTOCOL_DEPLOYMENT"],
    "last_updated": datetime.now().isoformat()
})

# SETTINGS
with open(os.path.join(base_dir, "SETTINGS_PASZKO_PRO.env"), "w", encoding="utf-8") as f:
    f.write("DATA_PATH=D:\\!_GPT\\2_Paszko_pro_Data\nSYNC=true\nVERSION=ΩΩΩX\n")

# YAML: USER_CONTEXT
with open(os.path.join(base_dir, "USER_CONTEXT_snapshot.yaml"), "w", encoding="utf-8") as f:
    f.write(f"""user_profile:
  child_name: Gabrysia
  active_protocols:
    - NEUROPROTOCOL
    - AI PREDICTION
    - CBD SUPPORT
  ai_focus: Seizure prediction + emotional development
  generated: {datetime.now().isoformat()}
""")

# INSTRUCTION
with open(os.path.join(base_dir, "GPT_STATE_RESTORE.instruction.txt"), "w", encoding="utf-8") as f:
    f.write("Instrukcja przywracania systemu PASZKO_PRO | vΩ.ΩΩΩX\n1. Załaduj SYSTEM_MANIFEST.json\n2. Odtwórz USER_CONTEXT + PROFILE\n")

# README
with open(os.path.join(base_dir, "README_RESTORE.txt"), "w", encoding="utf-8") as f:
    f.write("Zestaw danych do przywrócenia pełnej funkcjonalności systemu GPT PASZKO_PRO. Wygenerowano: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
