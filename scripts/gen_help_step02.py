import sys, os
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
import scripts.doc_style_utils as dsu

os.makedirs('help', exist_ok=True)

doc = docx.Document()
dsu.setup_page(doc, learner="Shreyansh", roll_no="2500320140140", project_id="D26", title="Step 2 - HMW Statements")

# ── TITLE ──
dsu.add_heading_1(doc, "STEP 2 — How Might We (HMW) Design Thinking Statements")
dsu.add_callout(doc, "Design-thinking facilitation output derived from Step 1 stakeholder analysis. Each HMW reframes a stakeholder pain point as a human-centered opportunity — specific to this project, neither too broad nor a premature solution.", "DESIGN THINKING METHODOLOGY")

# ═══════════════════════════════════════════════════════════════════
# 1. STAKEHOLDER PAIN POINTS
# ═══════════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "1. Stakeholder Pain Points Analysis")

# SH-01
dsu.add_heading_2(doc, "SH-01: CHRO / VP People (Executive Sponsor)")
pains_01 = [
    ("PP-01a", "Cannot substantiate the ₹14.9 Cr annual L&D budget to the Board of Directors because there is no consolidated metric linking training spend to measurable employee performance improvement."),
    ("PP-01b", "Has no visibility into which departments are over-spending on low-impact training while critical talent pools remain under-invested."),
    ("PP-01c", "Receives anecdotal reports that trained employees still leave the organization at high rates, but lacks quantitative evidence to connect training completion with retention outcomes.")
]
for pid, ptxt in pains_01:
    dsu.add_bullet_p(doc, ptxt, f"{pid}: ")

# SH-02
dsu.add_heading_2(doc, "SH-02: Head of L&D (Business Owner)")
pains_02 = [
    ("PP-02a", "Cannot objectively compare whether expensive In-Person classroom workshops outperform scalable Online modules in terms of actual competency gains."),
    ("PP-02b", "Relies on subjective post-training survey feedback to judge instructor quality; has no statistical method to detect grading anomalies or inflated trainer ratings."),
    ("PP-02c", "Struggles to identify which specific course curricula should be retired versus expanded — decisions are currently made on vendor relationships, not data.")
]
for pid, ptxt in pains_02:
    dsu.add_bullet_p(doc, ptxt, f"{pid}: ")

# SH-03
dsu.add_heading_2(doc, "SH-03: HR Business Partners (Operational Lead)")
pains_03 = [
    ("PP-03a", "Discovers low-performing employee cohorts only during annual appraisal cycles, by which time remedial intervention is too late to prevent attrition."),
    ("PP-03b", "Cannot identify which departments have critically low training participation rates because data is scattered across multiple spreadsheets and email chains."),
    ("PP-03c", "Spends excessive manual hours compiling audit-ready compliance reports for certified corporate trainings.")
]
for pid, ptxt in pains_03:
    dsu.add_bullet_p(doc, ptxt, f"{pid}: ")

# SH-04
dsu.add_heading_2(doc, "SH-04: Department / Engineering Leads (Functional Consumer)")
pains_04 = [
    ("PP-04a", "Cannot determine which engineers should undergo specialized cloud, AI, or leadership certifications to meet upcoming project deliverables."),
    ("PP-04b", "Has no way to verify whether team members who completed training actually demonstrated measurable skill improvement in their post-training appraisals.")
]
for pid, ptxt in pains_04:
    dsu.add_bullet_p(doc, ptxt, f"{pid}: ")

# SH-05
dsu.add_heading_2(doc, "SH-05: Academic Evaluator (Project Assessor)")
pains_05 = [
    ("PP-05a", "Needs to verify that the student applied rigorous statistical hypothesis testing (not just descriptive charts) to draw valid business conclusions."),
    ("PP-05b", "Expects complete bidirectional traceability from business questions through requirements, features, database columns, user stories, tests, and UI screens.")
]
for pid, ptxt in pains_05:
    dsu.add_bullet_p(doc, ptxt, f"{pid}: ")

# ═══════════════════════════════════════════════════════════════════
# 2. HMW STATEMENTS TABLE
# ═══════════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "2. How Might We Statements")
dsu.add_callout(doc, "Format: 'How might we <action> for <user/stakeholder> so that <desired outcome>?' — each statement is specific to this project's dataset and analytics scope.", "HMW FORMAT")

hmw_headers = ["HMW ID", "How Might We ...?", "Stakeholder", "Pain Point", "Linked OQ"]
hmw_widths = [900, 3800, 1200, 1200, 1538]
hmw_data = [
    ["HMW-01", "How might we quantify the exact performance rating gain attributable to each training program for executive leadership so that L&D capital allocation is justified with hard evidence?", "SH-01", "PP-01a", "OQ-01"],
    ["HMW-02", "How might we rank training programs by net productivity uplift per rupee spent for L&D managers so that underperforming vendor curricula can be data-retired?", "SH-01, SH-02", "PP-01b, PP-02c", "OQ-02"],
    ["HMW-03", "How might we compare learner engagement and competency score gains across Online, In-Person, and Hybrid delivery modes for curriculum designers so that instructional budgets are channelled optimally?", "SH-02", "PP-02a", "OQ-03"],
    ["HMW-04", "How might we identify employees whose training gaps correlate with high voluntary flight risk for HRBPs so that at-risk talent cohorts receive proactive skills enablement before they resign?", "SH-01, SH-03", "PP-01c, PP-03a", "OQ-04"],
    ["HMW-05", "How might we visualize department-level training participation rates and coverage blind spots for HR partners so that learning equity is maintained across all business units?", "SH-03, SH-04", "PP-03b", "OQ-05"],
    ["HMW-06", "How might we track quarterly training expenditure velocity against targeted performance yield for financial controllers so that budget overruns are detected and corrected mid-year?", "SH-01", "PP-01b", "OQ-06"],
    ["HMW-07", "How might we detect anomalous trainer feedback distributions and rating inflation for quality assurance leads so that instructor grading bias is identified and remediated?", "SH-02", "PP-02b", "OQ-07"],
    ["HMW-08", "How might we simulate the performance impact of shifting training budgets across delivery channels and departments for the CHRO so that future L&D investments are forecast with high confidence before committing capital?", "SH-01, SH-02", "PP-01a, PP-01b", "OQ-08"],
    ["HMW-09", "How might we surface employees requiring immediate remedial interventions based on post-training appraisal scores for HR partners so that corrective action happens in real-time rather than at the next annual review?", "SH-03", "PP-03a", "OQ-09"],
    ["HMW-10", "How might we automate the generation of compliance and certification audit reports for HR operations so that audit readiness is instantaneous and manual spreadsheet effort is eliminated?", "SH-03", "PP-03c", "OQ-09"],
    ["HMW-11", "How might we verify that team members who completed training demonstrated measurable skill improvement for department leads so that project staffing decisions are evidence-based?", "SH-04", "PP-04b", "OQ-01, OQ-02"],
    ["HMW-12", "How might we provide role-based authenticated access with persistent sessions across browser reloads for all portal users so that confidential appraisal data remains protected while user experience stays seamless?", "SH-01..05", "PP-05a", "OQ-10"]
]
t = doc.add_table(rows=1, cols=len(hmw_headers))
dsu.format_table(t, hmw_widths, hmw_headers, hmw_data)

# ═══════════════════════════════════════════════════════════════════
# 3. TOP 5 PRIORITY HMW STATEMENTS
# ═══════════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "3. Top 5 Priority HMW Statements")
dsu.add_callout(doc, "These five HMWs are marked PRIORITY because they address the highest-impact pain points, cover the most critical OQs, and directly drive the core MVP features of the analytics platform.", "PRIORITY RATIONALE")

priority_data = [
    ("1. HMW-01 (PRIORITY) — Performance Rating Delta", "This is the foundational analytical question for the entire project. Without proving a statistically significant performance uplift, the platform has no core business value proposition. It directly addresses the CHRO's inability to justify L&D spend."),
    ("2. HMW-02 (PRIORITY) — Cost-ROI Program Ranking", "Ranking programs by cost-effectiveness enables the single most actionable executive decision: which courses to fund, which to cut. This eliminates the ₹14.9 Cr 'black box' budget allocation problem."),
    ("3. HMW-03 (PRIORITY) — Delivery Mode Comparison", "The Online vs In-Person vs Hybrid debate is the #1 strategic question every L&D leader faces post-pandemic. Data-driven delivery mode selection directly impacts budget efficiency and learner engagement."),
    ("4. HMW-04 (PRIORITY) — Flight Risk & Training Correlation", "Talent retention is the most expensive HR outcome. If training reduces voluntary attrition from 48.2% to 14.1% in targeted cohorts, the financial impact dwarfs the cost of any individual training program."),
    ("5. HMW-08 (PRIORITY) — What-If Budget Simulation", "Executive leaders need forward-looking foresight, not just backward-looking reports. The What-If simulator transforms the dashboard from a reporting tool into a strategic planning instrument.")
]
for title, reason in priority_data:
    dsu.add_body_p(doc, reason, bold_prefix=f"{title}\n")

# ═══════════════════════════════════════════════════════════════════
# 4. OQ COVERAGE VERIFICATION
# ═══════════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "4. Coverage Verification: Every OQ Covered by ≥ 1 HMW")

cov_headers = ["OQ ID", "Covered By HMW(s)", "Coverage Status"]
cov_widths = [1500, 5000, 3138]
cov_data = [
    ["OQ-01", "HMW-01, HMW-11", "✓ Covered (Priority)"],
    ["OQ-02", "HMW-02, HMW-11", "✓ Covered (Priority)"],
    ["OQ-03", "HMW-03", "✓ Covered (Priority)"],
    ["OQ-04", "HMW-04", "✓ Covered (Priority)"],
    ["OQ-05", "HMW-05", "✓ Covered"],
    ["OQ-06", "HMW-06", "✓ Covered"],
    ["OQ-07", "HMW-07", "✓ Covered"],
    ["OQ-08", "HMW-08", "✓ Covered (Priority)"],
    ["OQ-09", "HMW-09, HMW-10", "✓ Covered"],
    ["OQ-10", "HMW-12", "✓ Covered"]
]
t2 = doc.add_table(rows=1, cols=len(cov_headers))
dsu.format_table(t2, cov_widths, cov_headers, cov_data)

dsu.add_callout(doc, "Result: 10/10 Operational Questions are covered by at least one HMW statement. Zero gaps detected. The 5 Priority HMWs collectively cover OQ-01, OQ-02, OQ-03, OQ-04, and OQ-08 — the highest-impact analytical questions.", "VERIFICATION PASSED")

doc.save("help/02_Shreyansh_HMW_Statements.docx")
print("SUCCESS: Generated help/02_Shreyansh_HMW_Statements.docx")
