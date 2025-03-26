from fpdf import FPDF
import json
import os

LOG_PATH = "setup/logs/backup_log.json"
OUTPUT_PDF = "setup/reports/backup_changelog.pdf"

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "🧠 GPT AutoBackup Changelog", ln=True, align='C')

    def chapter_body(self, text):
        self.set_font("Arial", '', 11)
        self.multi_cell(0, 8, text)
        self.ln()

def create_pdf():
    if not os.path.exists(LOG_PATH):
        print("❌ Brak logu.")
        return

    pdf = PDF()
    pdf.add_page()

    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            body = f"""
🕒 {entry['timestamp']}
Status: {entry['status']}
Szczegóły: {entry['details']}
-----------------------------
"""
            pdf.chapter_body(body)

    os.makedirs(os.path.dirname(OUTPUT_PDF), exist_ok=True)
    pdf.output(OUTPUT_PDF)
    print(f"✅ PDF changelog zapisany: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_pdf()