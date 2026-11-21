import sys, os
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
import scripts.doc_style_utils as dsu

os.makedirs('help', exist_ok=True)

doc = docx.Document()
dsu.setup_page(doc, learner="Shreyansh", roll_no="2500320140140", project_id="D26", title="Step 5 - Business Requirements Document")

# ══════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "Business Requirements Document (BRD)")
dsu.add_body_p(doc, "Project D26 — Training Effectiveness Data Analysis")
dsu.add_body_p(doc, "Domain: Human Resources Analytics (Corporate Learning & Development)")

# ══════════════════════════════════════════════════════════════
# 1. DOCUMENT CONTROL
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "1. Document Control")

dc_headers = ["Field", "Details"]
dc_widths = [2800, 6838]
dc_data = [
    ["Document Title", "Business Requirements Document — Training Effectiveness Data Analysis (D26)"],
    ["Version", "v1.0"],
    ["Author", "Shreyansh (Roll No: 2500320140140), MCA 2nd Year Data Analyst, ABES Engineering College"],
    ["Date Created", "21 November 2026"],
    ["Last Updated", "21 November 2026"],
    ["Reviewer(s)", "Dinesh Sereno (Project Mentor, ABES IT Department)"],
    ["Approver", "Dinesh Sereno"],
    ["Sign-Off Status", "Pending Review"],
    ["Distribution", "Learner, Mentor, Academic Evaluation Panel"],
    ["Source Documents", "Step 1 (Project Understanding), Step 2 (HMW Statements), Step 3 (Needs Analysis), Step 4 (RTM)"]
]
t_dc = doc.add_table(rows=1, cols=2)
dsu.format_table(t_dc, dc_widths, dc_headers, dc_data)

# Revision history
dsu.add_heading_2(doc, "1a. Revision History")
rev_headers = ["Version", "Date", "Author", "Change Description"]
rev_widths = [1200, 2000, 2800, 3638]
rev_data = [
    ["v0.1", "21/11/2026", "Shreyansh", "Initial draft — BRs from Step 3 Needs Analysis incorporated"],
    ["v1.0", "21/11/2026", "Shreyansh", "Complete BRD with all 13 sections; aligned with RTM (Step 4)"]
]
t_rev = doc.add_table(rows=1, cols=4)
dsu.format_table(t_rev, rev_widths, rev_headers, rev_data)

# ══════════════════════════════════════════════════════════════
# 2. EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "2. Executive Summary")
dsu.add_body_p(doc, "This BRD specifies the business requirements for the Training Effectiveness Data Analytics Platform (Project D26). The platform addresses a critical gap in enterprise HR decision-making: organizations invest millions in employee training programs but lack empirical evidence of whether those programs yield measurable improvements in employee performance, competency scores, and talent retention.")
dsu.add_body_p(doc, "The solution aggregates 5,000 corporate employee training records into a normalised SQLite database, performs rigorous statistical hypothesis testing (paired t-test, ANOVA, Chi-square, Cohen's d), and presents findings through an interactive Streamlit analytics dashboard with role-based access, Plotly visualisations, What-If budget simulation, and automated data export capabilities.")
dsu.add_body_p(doc, "This document consolidates outputs from Steps 1–4 (Project Understanding, HMW Statements, Needs Analysis, and the Requirements Traceability Matrix) into a formal enterprise BRD suitable for academic evaluation and professional reference.")

# ══════════════════════════════════════════════════════════════
# 3. BUSINESS PROBLEM AND OPPORTUNITY
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "3. Business Problem and Opportunity")

dsu.add_heading_2(doc, "3a. The Problem")
dsu.add_body_p(doc, "Enterprise organisations allocate substantial annual budgets (often ₹10–20 Crores) to corporate Learning & Development programs. However, L&D leadership currently lacks:")
problems = [
    "A consolidated metric linking training expenditure to quantifiable employee performance improvement.",
    "Comparative benchmarks to determine which training programs, delivery modes, and vendors yield the highest return on investment.",
    "Early-warning indicators connecting training gaps to employee voluntary attrition (flight risk).",
    "Forward-looking scenario planning tools to forecast the impact of budget reallocations before committing capital.",
    "Secure, role-appropriate access to sensitive employee appraisal data for different organisational levels."
]
for p in problems:
    dsu.add_bullet_p(doc, p)

dsu.add_heading_2(doc, "3b. The Opportunity")
dsu.add_body_p(doc, "By building a data-driven analytics platform that integrates cleaning, statistical analysis, interactive visualisation, and simulation capabilities, the organisation can:")
opportunities = [
    "Justify L&D capital allocation to the Board with hard statistical evidence (paired t-test, effect sizes).",
    "Retire underperforming training vendors and reinvest in high-ROI curricula — potentially saving 15–25% of annual training spend.",
    "Reduce voluntary talent attrition by proactively identifying and training at-risk employee cohorts.",
    "Empower non-technical HR stakeholders to independently explore data through interactive drill-down dashboards.",
    "Achieve audit readiness instantly through automated compliance report generation."
]
for o in opportunities:
    dsu.add_bullet_p(doc, o)

# ══════════════════════════════════════════════════════════════
# 4. OBJECTIVES AND SUCCESS METRICS (KPIs)
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "4. Objectives and Success Metrics")

kpi_headers = ["KPI ID", "KPI Name", "Target Metric", "Measurement Method", "Linked OQ"]
kpi_widths = [900, 2400, 2400, 2800, 1138]
kpi_data = [
    ["KPI-01", "Net Performance Rating Uplift", "≥ +0.50 points (pre → post)", "Paired t-test on rating_diff; Cohen's d > 0.80", "OQ-01"],
    ["KPI-02", "Assessment Score Delta", "≥ +15.0% average gain", "AVG(post_score − pre_score) across all records", "OQ-01"],
    ["KPI-03", "Training Participation Rate", "≥ 70.0% across all departments", "COUNT(trained) / COUNT(total) per department", "OQ-05"],
    ["KPI-04", "Cost Per Uplift Point", "≤ ₹60,000 / rating point", "SUM(training_cost) / SUM(rating_diff) by program", "OQ-02"],
    ["KPI-05", "Flight Risk Reduction", "Trained < 20% high-risk vs untrained > 40%", "Chi-square on retention_risk × training_status", "OQ-04"],
    ["KPI-06", "Dashboard Load Time", "< 3.0 seconds initial page render", "Browser DevTools Performance tab measurement", "OQ-10"],
    ["KPI-07", "Test Case Pass Rate", "18/18 tests (100% pass)", "pytest execution report with zero failures", "SC-03"],
    ["KPI-08", "Data Quality Score", "Zero nulls, zero orphan FKs in clean data", "Automated validation script output", "SC-04"]
]
t_kpi = doc.add_table(rows=1, cols=5)
dsu.format_table(t_kpi, kpi_widths, kpi_headers, kpi_data)

# ══════════════════════════════════════════════════════════════
# 5. STAKEHOLDERS — RACI TABLE
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "5. Stakeholders — RACI Matrix")
dsu.add_callout(doc, "R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted (provides input), I = Informed (kept updated).", "RACI LEGEND")

raci_headers = ["Project Phase / Activity", "CHRO\n(SH-01)", "L&D Head\n(SH-02)", "HRBP\n(SH-03)", "Dept Lead\n(SH-04)", "Mentor\n(SH-05)"]
raci_widths = [2600, 1200, 1300, 1200, 1300, 1038]
raci_data = [
    ["Requirements Elicitation (Steps 1–4)", "A", "R", "C", "C", "I"],
    ["Business Requirements Approval (Step 5)", "A", "C", "C", "I", "R"],
    ["Product & Technical Design (Steps 6–7)", "I", "A", "C", "C", "R"],
    ["Database Schema & Data Generation (Steps 8–10)", "I", "C", "I", "I", "R"],
    ["User Story Definition (Step 11)", "C", "A", "R", "C", "I"],
    ["UI/UX Framework Design (Step 12)", "C", "A", "C", "R", "I"],
    ["Test Case Definition & Execution (Step 13)", "I", "C", "R", "I", "A"],
    ["Application Build & Integration (Steps 14–15)", "I", "I", "I", "I", "R"],
    ["Cloud Deployment (Step 16)", "I", "I", "I", "I", "R"],
    ["Final Document & Presentation (Steps 17–18)", "I", "I", "I", "I", "A"],
    ["Acceptance & Sign-Off", "A", "R", "C", "I", "A"]
]
t_raci = doc.add_table(rows=1, cols=6)
dsu.format_table(t_raci, raci_widths, raci_headers, raci_data)

# ══════════════════════════════════════════════════════════════
# 6. SCOPE: IN / OUT
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "6. Scope")

dsu.add_heading_2(doc, "6a. In Scope")
in_items = [
    "Synthetic data generation with realistic Indian corporate workforce distributions (5,000 records, seed 42).",
    "Data cleaning pipeline: deduplication, null imputation, outlier capping, range validation.",
    "Descriptive statistics: mean, median, mode, standard deviation, quartiles, distribution analysis.",
    "Inferential statistics: paired t-test, one-way ANOVA, Chi-square test, Cohen's d effect size.",
    "Interactive Plotly visualisations: grouped bar, scatter, box/violin, area, KDE, heatmap charts.",
    "What-If budget simulation engine with interactive sliders and projected outcome rendering.",
    "Role-based PBKDF2-SHA256 authentication with 4 demo roles and persistent session state.",
    "Filtered data export (CSV/Excel) and auto-generated executive summary memo.",
    "Automated pytest test suite (≥ 18 test cases) with 100% pass validation.",
    "Streamlit Community Cloud deployment with pinned requirements.txt.",
    "Complete 18-step ABES project documentation (Word, Excel, PowerPoint)."
]
for item in in_items:
    dsu.add_bullet_p(doc, item)

dsu.add_heading_2(doc, "6b. Out of Scope")
out_items = [
    "Real-time biometric or RFID attendance hardware integration.",
    "Direct API writeback to enterprise ERP (SAP SuccessFactors, Workday, Oracle HCM).",
    "Native mobile applications (iOS / Android).",
    "Machine learning predictive models (random forest, neural networks) — deferred to v2.0.",
    "Multi-tenant SaaS architecture with per-organisation database isolation."
]
for item in out_items:
    dsu.add_bullet_p(doc, item)

# ══════════════════════════════════════════════════════════════
# 7. BUSINESS REQUIREMENTS (same BR IDs)
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "7. Business Requirements Specification")
dsu.add_callout(doc, "Each requirement preserves the BR ID established in Step 3 (Needs Analysis) and the HMW linkage from Step 2. Requirements state WHAT the business needs, not HOW the system implements it.", "CONSISTENCY NOTE")

br_spec_headers = ["BR ID", "Description", "Rationale", "Priority", "Source HMW", "Acceptance Criteria"]
br_spec_widths = [800, 2400, 1800, 800, 900, 2938]

br_specs = [
    ["BR-01", "Measure the net change in employee performance ratings pre vs post training.",
     "Without this metric, L&D budget justification is impossible.", "Must", "HMW-01",
     "Paired t-test returns p < 0.001; Cohen's d > 0.80; delta displayed on KPI card."],

    ["BR-02", "Rank training programs by performance improvement per unit expenditure.",
     "Enables data-driven vendor selection and curriculum pruning.", "Must", "HMW-02",
     "Sorted leaderboard with cost-per-uplift-point; top/bottom quartiles flagged."],

    ["BR-03", "Compare engagement and score gains across Online, In-Person, and Hybrid delivery modes.",
     "Post-pandemic channel mix is the #1 L&D strategic question.", "Must", "HMW-03",
     "Side-by-side score delta comparison validated with ANOVA (p < 0.05)."],

    ["BR-04", "Identify correlation between training completion and reduced flight risk.",
     "Talent retention is the most expensive HR outcome.", "Must", "HMW-04",
     "Chi-square test with proportions; trained vs untrained flight risk difference > 20%."],

    ["BR-05", "Quantify department-level participation rates and coverage gaps.",
     "Ensures learning equity across all business units.", "Must", "HMW-05",
     "Participation rate per department; departments below 60% flagged automatically."],

    ["BR-06", "Track quarterly training spend trends relative to performance yield.",
     "Enables mid-year budget course corrections.", "Should", "HMW-06",
     "Quarterly time-series with spend and uplift trend indicators."],

    ["BR-07", "Detect anomalies in trainer feedback scores (inflation/deflation).",
     "Maintains objective instructor quality assurance.", "Should", "HMW-07",
     "Distribution stats per trainer; outliers beyond ±2 SD flagged."],

    ["BR-08", "Forecast performance impact of hypothetical budget reallocations.",
     "Transforms reporting into strategic forward-looking planning.", "Should", "HMW-08",
     "Simulation outputs projected uplift with adjustable sliders; response < 200ms."],

    ["BR-09", "Surface employees requiring immediate remedial training interventions.",
     "Prevents late discovery of underperformers at annual review time.", "Must", "HMW-09",
     "Filtered list of employees with post-rating < 2.5 or score delta < 0."],

    ["BR-10", "Generate exportable audit-ready compliance reports.",
     "Eliminates manual spreadsheet compilation overhead.", "Could", "HMW-10",
     "One-click CSV/Excel export with filter criteria and timestamp logged."],

    ["BR-11", "Verify individual post-training skill improvement per team member.",
     "Supports evidence-based project staffing decisions.", "Should", "HMW-11",
     "Per-employee record: pre-rating, post-rating, delta, pass/fail (delta ≥ +0.25)."],

    ["BR-12", "Restrict appraisal data access based on organisational role.",
     "Upholds data privacy and confidentiality regulations.", "Must", "HMW-12",
     "Zero unauthorized data exposure; each role limited to permitted views."],

    ["BR-13", "Maintain session continuity across browser refreshes.",
     "Prevents workflow interruption during analytical exploration.", "Must", "HMW-12",
     "Session persists through ≥ 3 consecutive browser reloads."],

    ["BR-14", "Present insights through interactive visual interface with drill-down filtering.",
     "Empowers non-technical stakeholders to self-serve analytics.", "Must", "HMW-01..09",
     "Every OQ (01..10) answered through ≥ 1 interactive view with working filters."]
]
t_br = doc.add_table(rows=1, cols=6)
dsu.format_table(t_br, br_spec_widths, br_spec_headers, br_specs)

# ══════════════════════════════════════════════════════════════
# 8. BUSINESS RULES
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "8. Business Rules")

rules = [
    ("BRULE-01", "Rating Bounds", "All employee performance appraisal ratings must fall within the range 1.0 to 5.0 (inclusive). Any value outside this range is an invalid data point and must be capped or rejected during cleaning."),
    ("BRULE-02", "High-Impact Classification", "A training program is classified as 'High Impact' only if its average rating uplift is ≥ +0.50 AND its average learner feedback score is ≥ 4.00 stars."),
    ("BRULE-03", "Flight Risk Trigger", "An employee is classified as 'High' flight risk if they have tenure < 2 years AND have not completed any training in the preceding 12 months."),
    ("BRULE-04", "Currency Standardisation", "All financial metrics must be rendered in Indian Rupee format. Values above ₹1,00,000 displayed in Lakhs; values above ₹1,00,00,000 displayed in Crores."),
    ("BRULE-05", "Participation Threshold", "A department is flagged as having a 'critical coverage gap' if its training participation rate falls below 60%."),
    ("BRULE-06", "Statistical Significance", "No business insight may be presented as 'validated' unless the underlying statistical test achieves p < 0.05 at minimum. For primary KPIs, p < 0.001 is required."),
    ("BRULE-07", "Session Timeout", "An authenticated user session must remain valid for at least 60 minutes of inactivity. Sessions must survive browser page refreshes without re-authentication.")
]
for rule_id, rule_name, rule_desc in rules:
    dsu.add_body_p(doc, rule_desc, bold_prefix=f"{rule_id} ({rule_name}): ")

# ══════════════════════════════════════════════════════════════
# 9. DATA REQUIREMENTS
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "9. Data Requirements")

data_headers2 = ["Attribute", "Details"]
data_widths2 = [2800, 6838]
data_data2 = [
    ["Data Source", "Synthetic dataset generated by scripts/generate_data.py using random seed 42 with realistic Indian corporate workforce distributions."],
    ["Primary Fact Table", "training_records — 5,000 rows, 14 columns (record_id, employee_id, training_type, program_name, delivery_mode, duration_days, training_cost, pre_score, post_score, score_delta, post_rating, rating_diff, feedback_score, completion_date)."],
    ["Primary Dimension Table", "employees — 5,000 rows, 8 columns (employee_id, full_name, department, job_role, experience_years, location, pre_rating, retention_risk)."],
    ["Authentication Tables", "users (4 demo accounts with PBKDF2 hashes) and active_sessions (session persistence tokens)."],
    ["Data Storage", "SQLite 3 database file (training_analytics.db) embedded in the project repository root."],
    ["Data Refresh Frequency", "Static dataset — no live data refresh. Future v2.0 may integrate periodic HR system ETL."],
    ["Data Quality Standards", "Zero nulls in cleaned dataset, zero orphaned foreign keys, all values within CHECK constraint ranges, deduplication applied."],
    ["Raw vs Clean Pipeline", "data/raw/ contains CSV with deliberate anomalies (2–3% missing values, duplicates, outliers). data/clean/ contains validated, cleaned output."]
]
t_data = doc.add_table(rows=1, cols=2)
dsu.format_table(t_data, data_widths2, data_headers2, data_data2)

# ══════════════════════════════════════════════════════════════
# 10. ASSUMPTIONS, CONSTRAINTS, DEPENDENCIES
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "10. Assumptions, Constraints, and Dependencies")

dsu.add_heading_2(doc, "10a. Assumptions")
assumptions = [
    "Performance ratings follow a standardised 1.0–5.0 corporate appraisal scale across all departments and locations.",
    "Training evaluation aligns with Kirkpatrick Model Level 2 (Learning) and Level 3 (Behavior) criteria.",
    "The synthetic dataset is statistically representative of realistic Indian corporate training patterns.",
    "Stakeholders possess basic familiarity with web-based dashboards and can interpret statistical summary cards.",
    "Internet connectivity is available for Streamlit Community Cloud access during evaluation."
]
for a in assumptions:
    dsu.add_bullet_p(doc, a)

dsu.add_heading_2(doc, "10b. Constraints")
constraints = [
    "Streamlit Community Cloud free tier: 1 GB RAM limit, single-threaded execution, shared infrastructure.",
    "SQLite single-writer locking restricts concurrent write throughput (acceptable for read-heavy analytics workload).",
    "Project timeline: one academic semester (~6 weeks active development across 3 agile sprints).",
    "No access to real enterprise HR data — all analysis on synthetic generated records only.",
    "Tailwind CSS loaded via CDN inside st.components.v1.html(); not natively supported by Streamlit."
]
for c in constraints:
    dsu.add_bullet_p(doc, c)

dsu.add_heading_2(doc, "10c. Dependencies")
deps = [
    "Python 3.10+ runtime environment available on both local machine and Streamlit Cloud.",
    "GitHub repository (Shreyansh713/Training-Effectiveness-Analytics) accessible for CI/CD deployment.",
    "Required Python packages installable via pip: streamlit, pandas, numpy, scipy, plotly, python-docx, openpyxl.",
    "Streamlit Community Cloud account linked to GitHub for one-click deployment."
]
for d in deps:
    dsu.add_bullet_p(doc, d)

# ══════════════════════════════════════════════════════════════
# 11. RISKS AND MITIGATION
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "11. Risks and Mitigation")

risk_headers = ["Risk ID", "Risk Description", "Likelihood", "Impact", "Mitigation Strategy"]
risk_widths = [900, 3000, 1200, 1200, 3338]
risk_data = [
    ["R-01", "What-If simulation parameters are over-fitted to training data distributions, producing misleading forecasts.", "Medium", "High",
     "Apply bounded linear sensitivity limits based on empirical historical department distributions. Display confidence bands."],
    ["R-02", "Streamlit Cloud resource limits (1 GB RAM) cause out-of-memory crashes on large aggregations.", "Low", "High",
     "Use @st.cache_data with TTL caching; pre-aggregate heavy computations; keep dataset under 10,000 rows."],
    ["R-03", "SQLite database file corruption during concurrent access in cloud environment.", "Low", "High",
     "Set WAL journal mode; restrict writes to session management only; all analytics are read-only queries."],
    ["R-04", "Synthetic data does not adequately represent real-world enterprise training patterns.", "Medium", "Medium",
     "Built deliberate patterns (department variance, delivery mode effects) validated against published L&D industry benchmarks."],
    ["R-05", "PBKDF2 authentication adds perceptible login delay (100K iterations).", "Medium", "Low",
     "One-click demo role bypass for evaluators; PBKDF2 delay is < 300ms on modern hardware, acceptable for security."],
    ["R-06", "Tailwind CSS CDN unavailable in restricted network environments.", "Low", "Low",
     "Fallback to native Streamlit styling; Tailwind is enhancement-only, not a functional dependency."]
]
t_risk = doc.add_table(rows=1, cols=5)
dsu.format_table(t_risk, risk_widths, risk_headers, risk_data)

# ══════════════════════════════════════════════════════════════
# 12. GLOSSARY
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "12. Glossary")

gloss_headers = ["Term", "Definition"]
gloss_widths = [2800, 6838]
gloss_data = [
    ["BRD", "Business Requirements Document — formal specification of what the business needs from a solution."],
    ["Cohen's d", "Standardised measure of effect size; the difference between two group means divided by pooled standard deviation. Values > 0.80 indicate a large effect."],
    ["Flight Risk", "Predictive classification of an employee's probability of voluntary resignation within the next 12 months."],
    ["Kirkpatrick Model", "Globally recognised 4-level framework for evaluating corporate training effectiveness (Reaction, Learning, Behavior, Results)."],
    ["KPI", "Key Performance Indicator — a quantifiable measure used to evaluate success against objectives."],
    ["L&D", "Learning & Development — the organisational function responsible for employee training and professional growth."],
    ["MoSCoW", "Prioritisation framework: Must have, Should have, Could have, Won't have (in this release)."],
    ["Paired t-test", "Statistical hypothesis test comparing two related measurements (e.g., pre and post scores from the same individuals)."],
    ["PBKDF2", "Password-Based Key Derivation Function 2 — a cryptographic algorithm that makes password hashing computationally expensive to resist brute-force attacks."],
    ["RACI", "Responsibility assignment matrix: Responsible, Accountable, Consulted, Informed."],
    ["Rating Uplift", "Net change in annual performance appraisal score (Post-Training Rating minus Pre-Training Rating)."],
    ["ROI", "Return on Investment — the ratio of net benefit to cost, expressed as a percentage or monetary value."],
    ["RTM", "Requirements Traceability Matrix — a document linking requirements to their origins, implementations, and verifications."],
    ["SQLite", "Lightweight, serverless, file-based relational database engine embedded directly in applications."],
    ["What-If Analysis", "Scenario modelling technique that explores the impact of changing input parameters on projected outcomes."]
]
t_gloss = doc.add_table(rows=1, cols=2)
dsu.format_table(t_gloss, gloss_widths, gloss_headers, gloss_data)

# ══════════════════════════════════════════════════════════════
# 13. SIGN-OFF
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "13. Sign-Off")

sign_headers = ["Role", "Name", "Signature", "Date"]
sign_widths = [2400, 3000, 2200, 2038]
sign_data = [
    ["Author / Learner", "Shreyansh (Roll No: 2500320140140)", "___________________", "21/11/2026"],
    ["Project Mentor / Reviewer", "Dinesh Sereno (ABES IT Dept)", "___________________", "__/__/2026"],
    ["Academic Evaluator", "[Evaluator Name]", "___________________", "__/__/2026"]
]
t_sign = doc.add_table(rows=1, cols=4)
dsu.format_table(t_sign, sign_widths, sign_headers, sign_data)

dsu.add_callout(doc, "No new requirements were introduced beyond BR-01..14 from Step 3. The RTM (Step 4) does not need updating at this stage.", "RTM UPDATE CHECK")

doc.save("help/05_Shreyansh_BRD.docx")
print("SUCCESS: Generated help/05_Shreyansh_BRD.docx")
