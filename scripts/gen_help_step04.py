import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

os.makedirs('help', exist_ok=True)

# Styles
HEADER_FILL = PatternFill(start_color="A51C30", end_color="A51C30", fill_type="solid")
HEADER_FONT = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
ROW_FONT = Font(name="Calibri", size=9.5, color="151514")
ALT_FILL = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
WHITE_FILL = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
GREEN_FONT = Font(name="Calibri", size=9.5, color="16A34A", bold=True)
GREY_FONT = Font(name="Calibri", size=9.5, color="9CA3AF", italic=True)
THIN_BORDER = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

def style_header(ws, headers, col_widths=None):
    ws.append(headers)
    for col_num in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = THIN_BORDER
    ws.row_dimensions[1].height = 30
    if col_widths:
        for i, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w

def add_row(ws, row_num, data, is_alt=False, empty_cols=None):
    ws.append(data)
    fill = ALT_FILL if is_alt else WHITE_FILL
    for c_idx in range(1, len(data) + 1):
        cell = ws.cell(row=row_num, column=c_idx)
        cell.font = ROW_FONT
        cell.fill = fill
        cell.border = THIN_BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        # Style empty placeholder columns in grey italic
        if empty_cols and c_idx in empty_cols and str(cell.value).startswith("("):
            cell.font = GREY_FONT
    ws.row_dimensions[row_num].height = 45

wb = openpyxl.Workbook()

# ═══════════════════════════════════════════════════════════════════
# SHEET 1: Traceability Matrix
# ═══════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Traceability_Matrix"

headers = [
    "OQ ID", "HMW ID", "Req ID (BR)", "Requirement Description",
    "Stakeholder (SH)", "Priority", "Status",
    "Feature ID", "DB table.column", "User Story",
    "UI Screen", "Test Case (TC-F / TC-T)"
]
col_widths = [10, 10, 11, 52, 14, 11, 12, 12, 22, 12, 12, 18]
style_header(ws1, headers, col_widths)

# Empty column indices (8-12) for later steps
empty_cols = {8, 9, 10, 11, 12}

rtm_data = [
    ["OQ-01", "HMW-01", "BR-01",
     "The business needs to measure the net change in employee performance ratings before and after each training program so that leadership can determine whether training produces a statistically significant competency uplift.",
     "SH-01, SH-04", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-02", "HMW-02", "BR-02",
     "The business needs to rank training programs by the performance improvement generated per unit of expenditure so that low-yield curricula can be identified and retired.",
     "SH-01, SH-02", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-03", "HMW-03", "BR-03",
     "The business needs to compare learner engagement and competency score gains across different instructional delivery channels so that budget allocation between channels is evidence-based.",
     "SH-02, SH-04", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-04", "HMW-04", "BR-04",
     "The business needs to identify whether a correlation exists between training completion and reduced employee voluntary turnover risk so that retention strategies can be linked to L&D investments.",
     "SH-01, SH-03", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-05", "HMW-05", "BR-05",
     "The business needs to quantify department-level training participation rates and highlight business units with critical coverage gaps so that learning equity is maintained.",
     "SH-03, SH-04", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-06", "HMW-06", "BR-06",
     "The business needs to track how training expenditure has trended over quarterly periods relative to performance improvement yield so that mid-year budget corrections can be made proactively.",
     "SH-01", "Should", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-07", "HMW-07", "BR-07",
     "The business needs to detect statistical anomalies in trainer feedback scores and identify cases of rating inflation or deflation so that instructor quality assurance remains objective.",
     "SH-02", "Should", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-08", "HMW-08", "BR-08",
     "The business needs to forecast the expected performance impact of hypothetical budget reallocations across departments and delivery channels so that strategic workforce planning is data-driven.",
     "SH-01, SH-02", "Should", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-09", "HMW-09", "BR-09",
     "The business needs to surface individual employees requiring immediate remedial training interventions based on their post-training appraisal performance so that corrective action is timely.",
     "SH-03", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-09", "HMW-10", "BR-10",
     "The business needs to generate exportable, audit-ready compliance reports for certified corporate training programs so that regulatory readiness is maintained without manual effort.",
     "SH-03", "Could", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-01, OQ-02", "HMW-11", "BR-11",
     "The business needs to verify that individual team members who completed training demonstrated measurable skill improvement in their subsequent appraisals so that staffing decisions are evidence-based.",
     "SH-04", "Should", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-10", "HMW-12", "BR-12",
     "The business needs to restrict access to sensitive employee appraisal data to authorized personnel based on their organizational role so that data privacy regulations are upheld.",
     "SH-01..05", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-10", "HMW-12", "BR-13",
     "The business needs to maintain user session continuity across browser interactions and page refreshes so that analytical workflows are not interrupted by session timeouts.",
     "SH-01..05", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],

    ["OQ-01..10", "HMW-01..09", "BR-14",
     "The business needs to present all analytical insights through an interactive visual interface with drill-down filtering so that non-technical stakeholders can explore data independently.",
     "SH-01..04", "Must", "Identified",
     "(Step 6)", "(Step 8)", "(Step 11)", "(Step 12)", "(Step 13)"],
]

for idx, row in enumerate(rtm_data, start=2):
    add_row(ws1, idx, row, is_alt=(idx % 2 == 1), empty_cols=empty_cols)

# Enable auto-filter
ws1.auto_filter.ref = f"A1:L{len(rtm_data)+1}"

# Freeze top row
ws1.freeze_panes = "A2"

# ═══════════════════════════════════════════════════════════════════
# SHEET 2: Coverage Check
# ═══════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet(title="Coverage_Check")

cov_headers = ["Check Type", "Items Checked", "Items Covered", "Items with Gaps", "Gap Details", "Status"]
cov_widths = [28, 18, 18, 18, 40, 14]
style_header(ws2, cov_headers, cov_widths)

cov_data = [
    ["HMW without any BR",
     "HMW-01, HMW-02, HMW-03, HMW-04, HMW-05, HMW-06, HMW-07, HMW-08, HMW-09, HMW-10, HMW-11, HMW-12",
     "12 / 12 (100%)", "0", "No gaps — every HMW maps to at least one BR.", "✓ PASS"],

    ["BR without any source HMW",
     "BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14",
     "14 / 14 (100%)", "0", "No gaps — every BR traces back to a source HMW.", "✓ PASS"],

    ["OQ not covered by any HMW→BR chain",
     "OQ-01, OQ-02, OQ-03, OQ-04, OQ-05, OQ-06, OQ-07, OQ-08, OQ-09, OQ-10",
     "10 / 10 (100%)", "0", "No gaps — every OQ is addressable through the HMW→BR chain.", "✓ PASS"],

    ["Must-priority BRs without OQ linkage",
     "BR-01, BR-02, BR-03, BR-04, BR-05, BR-09, BR-12, BR-13, BR-14",
     "9 / 9 (100%)", "0", "Every Must BR links to at least one OQ.", "✓ PASS"],
]

for idx, row in enumerate(cov_data, start=2):
    ws2.append(row)
    fill = ALT_FILL if idx % 2 == 1 else WHITE_FILL
    for c in range(1, 7):
        cell = ws2.cell(row=idx, column=c)
        cell.font = ROW_FONT
        cell.fill = fill
        cell.border = THIN_BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        if c == 6:
            cell.font = GREEN_FONT
    ws2.row_dimensions[idx].height = 50

ws2.auto_filter.ref = f"A1:F{len(cov_data)+1}"
ws2.freeze_panes = "A2"

# ═══════════════════════════════════════════════════════════════════
# SHEET 3: OQ-to-HMW-to-BR Map
# ═══════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet(title="OQ_HMW_BR_Map")

map_headers = ["OQ ID", "Linked HMW(s)", "Linked BR(s)", "Priority Mix", "Coverage"]
map_widths = [12, 20, 20, 18, 14]
style_header(ws3, map_headers, map_widths)

map_data = [
    ["OQ-01", "HMW-01, HMW-11", "BR-01, BR-11", "Must + Should", "✓ Full"],
    ["OQ-02", "HMW-02, HMW-11", "BR-02, BR-11", "Must + Should", "✓ Full"],
    ["OQ-03", "HMW-03", "BR-03", "Must", "✓ Full"],
    ["OQ-04", "HMW-04", "BR-04", "Must", "✓ Full"],
    ["OQ-05", "HMW-05", "BR-05", "Must", "✓ Full"],
    ["OQ-06", "HMW-06", "BR-06", "Should", "✓ Full"],
    ["OQ-07", "HMW-07", "BR-07", "Should", "✓ Full"],
    ["OQ-08", "HMW-08", "BR-08", "Should", "✓ Full"],
    ["OQ-09", "HMW-09, HMW-10", "BR-09, BR-10", "Must + Could", "✓ Full"],
    ["OQ-10", "HMW-12", "BR-12, BR-13", "Must + Must", "✓ Full"],
]

for idx, row in enumerate(map_data, start=2):
    ws3.append(row)
    fill = ALT_FILL if idx % 2 == 1 else WHITE_FILL
    for c in range(1, 6):
        cell = ws3.cell(row=idx, column=c)
        cell.font = ROW_FONT
        cell.fill = fill
        cell.border = THIN_BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        if c == 5:
            cell.font = GREEN_FONT
    ws3.row_dimensions[idx].height = 22

ws3.auto_filter.ref = f"A1:E{len(map_data)+1}"
ws3.freeze_panes = "A2"

# ═══════════════════════════════════════════════════════════════════
# SHEET 4: Update Log
# ═══════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet(title="Update_Log")

log_headers = ["Step #", "Update Description", "Columns Filled", "Date", "Status"]
log_widths = [10, 40, 28, 14, 14]
style_header(ws4, log_headers, log_widths)

log_data = [
    ["Step 4", "Initial RTM created with OQ, HMW, BR, Stakeholder, Priority, Status", "A through G", "21/11/2026", "✓ Done"],
    ["Step 6", "Fill 'Feature ID' column from PRD feature mapping", "H (Feature ID)", "(Pending)", "(Pending)"],
    ["Step 8", "Fill 'DB table.column' from database design", "I (DB table.column)", "(Pending)", "(Pending)"],
    ["Step 11", "Fill 'User Story' from agile user stories", "J (User Story)", "(Pending)", "(Pending)"],
    ["Step 12", "Fill 'UI Screen' from UI framework wireframes", "K (UI Screen)", "(Pending)", "(Pending)"],
    ["Step 13", "Fill 'Test Case' from functional and technical test cases", "L (Test Case)", "(Pending)", "(Pending)"],
]

for idx, row in enumerate(log_data, start=2):
    ws4.append(row)
    fill = ALT_FILL if idx % 2 == 1 else WHITE_FILL
    for c in range(1, 6):
        cell = ws4.cell(row=idx, column=c)
        cell.font = ROW_FONT if idx == 2 else GREY_FONT
        if idx == 2:
            cell.font = GREEN_FONT if c == 5 else ROW_FONT
        cell.fill = fill
        cell.border = THIN_BORDER
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws4.row_dimensions[idx].height = 24

ws4.freeze_panes = "A2"

wb.save("help/04_Shreyansh_Traceability_Matrix.xlsx")
print("SUCCESS: Generated help/04_Shreyansh_Traceability_Matrix.xlsx")
