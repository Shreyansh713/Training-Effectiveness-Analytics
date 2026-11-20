import sys, os
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
import scripts.doc_style_utils as dsu

os.makedirs('help', exist_ok=True)

doc = docx.Document()
dsu.setup_page(doc, learner="Shreyansh", roll_no="2500320140140", project_id="D26", title="Step 1 - Project Understanding")

# ── TITLE ──
dsu.add_heading_1(doc, "STEP 1 — Project Understanding")
dsu.add_callout(doc, "Project D26: Training Effectiveness Data Analysis | Domain: Human Resources Analytics (Corporate L&D) | Learner: Shreyansh (Roll 2500320140140) | Mentor: Dr. Anjali Pandey | ABES Engineering College, Ghaziabad", "PROJECT METADATA")

# ── 1. PROJECT OVERVIEW ──
dsu.add_heading_2(doc, "1. Project Overview")
dsu.add_body_p(doc, "This project designs and delivers an interactive data analytics platform that evaluates the effectiveness of corporate employee training programs. Using a dataset of 5,000 synthetic but realistic employee-training records, the application performs descriptive, inferential, and predictive analytics to empower HR leadership with evidence-based insights for optimizing Learning & Development (L&D) investments.")

# ── 2. PROBLEM STATEMENT ──
dsu.add_heading_2(doc, "2. Problem Statement")
dsu.add_body_p(doc, "Enterprise organizations invest significant capital in employee training programs but lack a consolidated, data-driven mechanism to measure whether these programs yield statistically significant improvements in employee performance ratings, competency assessment scores, and talent retention — leading to uninformed budget allocations and suboptimal workforce development strategies.")

# ── 3. INTENDED AUDIENCE / USERS ──
dsu.add_heading_2(doc, "3. Intended Audience / Users")
audience_headers = ["User Role", "Who They Are", "How Often They Use the App", "What They Look For"]
audience_widths = [2000, 2600, 2000, 3038]
audience_data = [
    ["CHRO / VP People", "Chief Human Resources Officer at a mid-to-large enterprise", "Quarterly / Monthly", "Macro KPIs: total spend, net rating uplift, flight risk summary"],
    ["Head of L&D", "Corporate Learning & Development program manager", "Bi-weekly", "Program-level ROI, delivery mode comparison, trainer feedback trends"],
    ["HR Business Partner", "Operational HR liaisons assigned to business units", "Weekly", "Department-wise participation rates, low-performer remediation lists"],
    ["Department / Eng Lead", "Functional managers overseeing engineering or operations teams", "Monthly", "Team capability uplift, certification completion gaps"],
    ["Academic Evaluator", "ABES project mentor / external examiner", "One-time (project review)", "Statistical rigor, database design, code quality, test coverage"]
]
t = doc.add_table(rows=1, cols=len(audience_headers))
dsu.format_table(t, audience_widths, audience_headers, audience_data)

# ── 4. STAKEHOLDERS ANALYSIS ──
dsu.add_heading_2(doc, "4. Stakeholders Analysis")
sh_headers = ["SH ID", "Stakeholder", "Role", "Interest", "Influence", "Decision They Make with the App"]
sh_widths = [900, 1600, 1600, 1600, 1000, 2938]
sh_data = [
    ["SH-01", "CHRO / VP People", "Executive Sponsor", "Overall training ROI, talent retention, budget justification", "High", "Approves or cuts annual L&D budget allocations based on demonstrated returns"],
    ["SH-02", "Head of L&D", "Business Owner", "Curriculum efficacy, vendor performance, delivery channel optimization", "High", "Retires underperforming training vendors; doubles down on high-ROI programs"],
    ["SH-03", "HR Business Partners", "Operational Lead", "Team appraisals, participation equity, remediation targeting", "Medium", "Mandates remedial training interventions for low-performing employee cohorts"],
    ["SH-04", "Dept / Engineering Leads", "Functional Consumer", "Capability uplift, certification gaps, project readiness", "Medium", "Approves team hours for specific technical and leadership certifications"],
    ["SH-05", "Academic Evaluator", "Project Assessor", "Statistical methodology, database design, code architecture", "High", "Evaluates and grades the project on analytical rigour and engineering quality"]
]
t2 = doc.add_table(rows=1, cols=len(sh_headers))
dsu.format_table(t2, sh_widths, sh_headers, sh_data)

# ── 5. OPERATIONAL QUESTIONS ──
dsu.add_heading_2(doc, "5. Operational Questions the App Must Answer")
dsu.add_callout(doc, "Each OQ must be answerable from the data stored in training_analytics.db. Verification is provided in the rightmost column.", "TRACEABILITY CHECK")

oq_headers = ["OQ ID", "Operational Question", "Data Required", "Answerable?"]
oq_widths = [900, 4000, 2800, 938]
oq_data = [
    ["OQ-01", "What is the net statistical uplift in employee performance ratings and competency scores after training?", "pre_rating, post_rating, pre_score, post_score (training_records)", "Yes ✓"],
    ["OQ-02", "Which specific training programs deliver the highest performance improvement per rupee spent?", "training_type, program_name, training_cost, rating_diff (training_records)", "Yes ✓"],
    ["OQ-03", "How do instructional delivery modes (Online, In-Person, Hybrid) compare in learner engagement and score delta?", "delivery_mode, score_delta, feedback_score (training_records)", "Yes ✓"],
    ["OQ-04", "Is there a statistically significant correlation between training completion and reduction in employee flight risk?", "retention_risk (employees), post_rating, training completion flag", "Yes ✓"],
    ["OQ-05", "What are the departmental participation rates, and where do critical training coverage gaps exist?", "department (employees), employee_id presence in training_records", "Yes ✓"],
    ["OQ-06", "How has training expenditure trended quarterly across departments relative to performance output?", "training_cost, completion_date (training_records), department (employees)", "Yes ✓"],
    ["OQ-07", "Are trainer feedback scores normally distributed or biased by learner satisfaction anomalies?", "feedback_score (training_records) — distribution & skewness test", "Yes ✓"],
    ["OQ-08", "What is the projected performance uplift under simulated budget reallocation across departments?", "training_cost, delivery_mode, rating_diff — What-If simulation inputs", "Yes ✓"],
    ["OQ-09", "Which employee cohorts require immediate targeted remedial interventions based on post-training appraisals?", "post_rating, retention_risk, department (employees + training_records join)", "Yes ✓"],
    ["OQ-10", "Does the system maintain secure role-based session states across user interactions and browser reloads?", "users, active_sessions tables — session_token, role, last_active", "Yes ✓"]
]
t3 = doc.add_table(rows=1, cols=len(oq_headers))
dsu.format_table(t3, oq_widths, oq_headers, oq_data)

# ── 6. SMART OBJECTIVES ──
dsu.add_heading_2(doc, "6. Objectives (SMART)")
obj_headers = ["Obj #", "Objective Statement", "S", "M", "A", "R", "T"]
obj_widths = [700, 4038, 900, 900, 900, 900, 1300]
obj_data = [
    ["O-01", "Ingest, clean, and validate 5,000 corporate employee training records with 100% relational integrity in SQLite", "Defined data pipeline with named scripts", "Zero nulls, zero orphan FKs in cleaned data", "Scripts already built & tested", "Foundation for all analytics", "Sprint 1 (Week 1-2)"],
    ["O-02", "Achieve a statistically validated performance rating uplift of ≥ +0.50 points verified via paired t-test (p < 0.001)", "Paired t-test on pre vs post ratings", "t-stat, p-value, Cohen's d reported", "SciPy library available", "Proves training drives results", "Sprint 2 (Week 3-4)"],
    ["O-03", "Deliver an interactive Streamlit dashboard with ≥ 5 analytical views, KPI cards, and Plotly visualizations", "Named screens: Overview, Dept, Benchmark, EDA, Simulator", "5+ views all rendering without error", "Streamlit + Plotly stack proven", "Directly answers all 10 OQs", "Sprint 2–3 (Week 3-5)"],
    ["O-04", "Implement PBKDF2 role-based authentication with session persistence across browser reloads", "PBKDF2-SHA256 with 100K iterations + salt", "Login survives page refresh; zero unauthorized access", "hashlib built-in Python library", "Protects sensitive appraisal data", "Sprint 3 (Week 5)"],
    ["O-05", "Pass 100% of automated test cases (≥ 18 tests: 10 functional + 8 technical pytest)", "Named test cases TC-F-01..10, TC-T-01..08", "18/18 tests pass with zero failures", "pytest framework installed", "Guarantees delivery quality", "Sprint 3 (Week 5-6)"],
    ["O-06", "Deploy the production application to Streamlit Community Cloud accessible via public URL", "GitHub main branch → Streamlit Cloud auto-deploy", "Live URL loads without errors", "Free tier available", "Enables remote evaluation", "Sprint 3 (Week 6)"]
]
t4 = doc.add_table(rows=1, cols=len(obj_headers))
dsu.format_table(t4, obj_widths, obj_headers, obj_data)

# ── 7. SCOPE ──
dsu.add_heading_2(doc, "7. Scope: In / Out")

dsu.add_heading_3(doc, "7a. In Scope")
in_scope = [
    "End-to-end data pipeline: synthetic CSV generation → cleaning → SQLite ingestion → cached querying",
    "Descriptive statistics: mean, median, mode, standard deviation, quartiles, distribution plots",
    "Inferential statistics: paired t-test, one-way ANOVA, Chi-square test of independence, Cohen's d effect size",
    "Interactive Plotly visualizations: grouped bar, scatter, box/violin, area, KDE, heatmap charts",
    "What-If budget simulator: interactive sliders forecasting performance uplift under hypothetical allocations",
    "PBKDF2 role-based authentication with 4 demo roles and persistent session state",
    "Data export: filtered CSV/Excel download and auto-generated executive summary memo",
    "Automated pytest test suite (≥ 18 test cases) with 100% pass validation",
    "Streamlit Community Cloud deployment with pinned requirements.txt",
    "Complete 18-step ABES project documentation suite (Word, Excel, PowerPoint)"
]
for item in in_scope:
    dsu.add_bullet_p(doc, item)

dsu.add_heading_3(doc, "7b. Out of Scope")
out_scope = [
    "Real-time biometric or RFID employee attendance tracking hardware integration",
    "Direct API writeback to enterprise ERP systems (SAP SuccessFactors, Workday HCM, Oracle HCM)",
    "Native mobile applications for iOS or Android platforms",
    "Machine learning predictive models (random forest, neural networks) — deferred to v2.0",
    "Multi-tenant SaaS architecture with per-organization database isolation"
]
for item in out_scope:
    dsu.add_bullet_p(doc, item)

# ── 8. ASSUMPTIONS & CONSTRAINTS ──
dsu.add_heading_2(doc, "8. Assumptions and Constraints")

dsu.add_heading_3(doc, "8a. Assumptions")
assumptions = [
    "Employee performance ratings are recorded on a standardized 1.0 to 5.0 annual appraisal scale across all departments.",
    "Training evaluation data follows Kirkpatrick Model Level 2 (Learning) and Level 3 (Behavior) frameworks.",
    "The synthetic dataset is representative of realistic Indian corporate workforce demographics and training patterns.",
    "Stakeholders have basic familiarity with web-based dashboards and can interpret statistical summary cards.",
    "Internet connectivity is available for Streamlit Community Cloud access during project evaluation."
]
for item in assumptions:
    dsu.add_bullet_p(doc, item)

dsu.add_heading_3(doc, "8b. Constraints")
constraints = [
    "Streamlit Community Cloud free tier limits: 1 GB RAM, single-threaded execution, shared infrastructure.",
    "SQLite single-writer locking restricts concurrent write throughput (acceptable for read-heavy analytics).",
    "Project timeline constrained to one academic semester (~6 weeks of active development).",
    "No access to real enterprise HR data — all analysis performed on synthetic generated records.",
    "Tailwind CSS is loaded via CDN inside st.components.v1.html(); not natively supported by Streamlit."
]
for item in constraints:
    dsu.add_bullet_p(doc, item)

# ── 9. SUCCESS CRITERIA ──
dsu.add_heading_2(doc, "9. Measurable Success Criteria")
sc_headers = ["Criteria #", "Success Criterion", "Target Metric", "Measurement Method"]
sc_widths = [1000, 3600, 2500, 2538]
sc_data = [
    ["SC-01", "Dashboard page loads within acceptable time", "< 3.0 seconds initial load", "Browser DevTools Network tab measurement"],
    ["SC-02", "Statistical hypothesis test confirms training effectiveness", "Paired t-test p < 0.001, Cohen's d > 0.80", "SciPy ttest_rel() output logged in notebook"],
    ["SC-03", "All automated test cases pass successfully", "18/18 tests (100% pass rate)", "pytest --tb=short output with zero failures"],
    ["SC-04", "Cleaned dataset has zero data quality issues", "0 nulls, 0 duplicates, all values in valid ranges", "Validation report from cleaning pipeline script"],
    ["SC-05", "Role-based authentication prevents unauthorized access", "Zero unauthorized data exposure across all 4 roles", "Manual testing of each role + session persistence check"],
    ["SC-06", "Every Operational Question (OQ-01..10) is answered by at least one dashboard view", "10/10 OQs mapped to UI screens", "RTM traceability verification (Step 4 spreadsheet)"],
    ["SC-07", "Application deploys and runs without errors on Streamlit Community Cloud", "Live public URL accessible with no crash", "End-to-end smoke test on deployed URL"],
    ["SC-08", "Complete project documentation suite generated and submitted", "16 document files in docs/ folder", "File count and format verification"]
]
t5 = doc.add_table(rows=1, cols=len(sc_headers))
dsu.format_table(t5, sc_widths, sc_headers, sc_data)

# ── TRACEABILITY CHECK ──
dsu.add_heading_2(doc, "10. Traceability Verification: Can Every OQ Be Answered from Data?")
dsu.add_body_p(doc, "Yes. All 10 Operational Questions (OQ-01 through OQ-10) can be fully answered using the columns available in the training_analytics.db SQLite database. The primary data sources are the 'employees' master dimension table (8 columns) and the 'training_records' fact table (14 columns), which together provide all demographic, performance, cost, feedback, and temporal attributes required for comprehensive descriptive and inferential analysis.")
dsu.add_callout(doc, "Verification: The OQ column in the table above confirms each question maps to specific database columns. Full bidirectional traceability will be established in Step 4 (Requirements Traceability Matrix).", "TRACEABILITY CONFIRMED")

doc.save("help/01_Shreyansh_Project_Understanding.docx")
print("SUCCESS: Generated help/01_Shreyansh_Project_Understanding.docx")
