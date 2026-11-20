import openpyxl
from openpyxl.styles import Font

# Feature mapping: BR → Feature ID
br_to_feat = {
    "BR-01": "FEAT-02, FEAT-11",
    "BR-02": "FEAT-03",
    "BR-03": "FEAT-04",
    "BR-04": "FEAT-05",
    "BR-05": "FEAT-06",
    "BR-06": "FEAT-07",
    "BR-07": "FEAT-08",
    "BR-08": "FEAT-09",
    "BR-09": "FEAT-05",
    "BR-10": "FEAT-10",
    "BR-11": "FEAT-03, FEAT-11",
    "BR-12": "FEAT-01",
    "BR-13": "FEAT-01",
    "BR-14": "FEAT-02..12 (all views)"
}

wb = openpyxl.load_workbook("help/04_Shreyansh_Traceability_Matrix.xlsx")
ws = wb["Traceability_Matrix"]

FILLED_FONT = Font(name="Calibri", size=9.5, color="16A34A", bold=True)

for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
    br_cell = row[2]  # Column C = Req ID (BR)
    feat_cell = row[7]  # Column H = Feature ID
    br_id = str(br_cell.value).strip()
    if br_id in br_to_feat:
        feat_cell.value = br_to_feat[br_id]
        feat_cell.font = FILLED_FONT

# Update the log sheet
ws_log = wb["Update_Log"]
for row in ws_log.iter_rows(min_row=2, max_row=ws_log.max_row):
    if str(row[0].value).strip() == "Step 6":
        row[3].value = "21/11/2026"
        row[4].value = "✓ Done"
        row[3].font = Font(name="Calibri", size=9.5, color="151514")
        row[4].font = Font(name="Calibri", size=9.5, color="16A34A", bold=True)
        break

wb.save("help/04_Shreyansh_Traceability_Matrix.xlsx")
print("SUCCESS: Updated RTM — Feature ID column filled (Step 6)")
