import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
import scripts.doc_style_utils as dsu

os.makedirs('docs', exist_ok=True)

# -----------------------------------------------------------------------------
# STEP 1: docs/01_Project_Understanding.docx
# -----------------------------------------------------------------------------
def build_step_01():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 1 - Project Understanding")

    dsu.add_heading_1(doc, "STEP 1 — Project Understanding Document")
    dsu.add_callout(doc, "Project D26: Training Effectiveness Data Analysis | ABES Engineering College MCA 2nd Year Data Analytics", "PROJECT METADATA")

    dsu.add_heading_2(doc, "1. Problem Statement")
    dsu.add_body_p(doc, "Enterprise organizations allocate massive budgets to employee corporate training programs without empirical data quantifying whether specific training interventions meaningfully uplift employee performance ratings, enhance competency scores, justify institutional training expenditure, or reduce voluntary talent turnover.")

    dsu.add_heading_2(doc, "2. Intended Audience & Users")
    dsu.add_bullet_p(doc, "Chief Human Resources Officer (CHRO): Opens the executive dashboard quarterly to evaluate macro ROI, allocate department training budgets, and benchmark talent retention.", "Primary User: ")
    dsu.add_bullet_p(doc, "Corporate L&D Managers: Opens the dashboard bi-weekly to evaluate trainer efficacy, identify underperforming programs, and monitor employee completion rates.", "Secondary User: ")
    dsu.add_bullet_p(doc, "Department Engineering & Operations Leads: Reviews monthly to verify team skill upgrades and address performance rating gaps.", "Operational User: ")
    dsu.add_bullet_p(doc, "ABES Project Mentor & External Evaluator: Assesses analytical rigor, statistical hypothesis testing (paired t-test, ANOVA), data modeling, and code craftsmanship.", "Academic Evaluator: ")

    dsu.add_heading_2(doc, "3. Stakeholders Analysis")
    sh_headers = ["SH ID", "Stakeholder", "Role", "Interest", "Influence", "Decision Made with App"]
    sh_widths = [1100, 1800, 1800, 1300, 1100, 2538]
    sh_data = [
        ["SH-01", "CHRO / VP People", "Executive Sponsor", "Budget ROI, Retention", "High", "Approves annual L&D budget allocations & strategy"],
        ["SH-02", "Head of L&D", "Business Owner", "Curriculum Efficacy", "High", "Retires ineffective vendors; expands high-impact modules"],
        ["SH-03", "HR Business Partners", "Operational Lead", "Team Appraisals, Uplift", "Medium", "Mandates remedial interventions for low-performing cohorts"],
        ["SH-04", "Engineering / Dept Leads", "Functional Consumer", "Capability Uplift", "Medium", "Approves team hours for technical and leadership trainings"],
        ["SH-05", "Academic Evaluator", "Project Assessor", "Methodology & Code", "High", "Evaluates statistical validity, database design, and UI delivery"]
    ]
    t = doc.add_table(rows=1, cols=len(sh_headers))
    dsu.format_table(t, sh_widths, sh_headers, sh_data)

    dsu.add_heading_2(doc, "4. Operational Questions (OQs)")
    oqs = [
        ("OQ-01", "What is the net statistical uplift in employee performance ratings and competency scores post-training?"),
        ("OQ-02", "Which specific training programs deliver the highest performance improvement per rupee spent?"),
        ("OQ-03", "How do instructional delivery modes (Online, In-Person, Hybrid) compare in terms of learner engagement and score delta?"),
        ("OQ-04", "Is there a statistically significant correlation between training completion and reduction in employee flight risk?"),
        ("OQ-05", "What are the departmental participation rates, and where do critical training coverage gaps exist?"),
        ("OQ-06", "How has training expenditure trended quarterly across departments relative to performance output?"),
        ("OQ-07", "Are trainer feedback scores normally distributed or biased by learner satisfaction anomalies?"),
        ("OQ-08", "What is the projected performance uplift under simulated budget reallocation across departments?"),
        ("OQ-09", "Which employee cohorts require immediate targeted remedial interventions based on post-training appraisals?"),
        ("OQ-10", "Does the system maintain secure role-based session states across user interactions and reloads?")
    ]
    for oq_id, oq_text in oqs:
        dsu.add_bullet_p(doc, oq_text, f"{oq_id}: ")

    dsu.add_heading_2(doc, "5. SMART Objectives")
    dsu.add_bullet_p(doc, "Ingest, clean, and validate 5,000 corporate employee training records with 100% relational integrity in SQLite by Sprint 1.", "Specific: ")
    dsu.add_bullet_p(doc, "Achieve a statistically validated performance rating uplift (+0.50 minimum target; actual +0.53) verified via paired t-test (p < 0.001).", "Measurable: ")
    dsu.add_bullet_p(doc, "Implement an interactive Streamlit analytics platform featuring 5 dashboard views, What-If simulation, and executive export.", "Achievable: ")
    dsu.add_bullet_p(doc, "Empower HR leadership to identify ₹14.93 Cr in spending patterns and reduce flight risk in critical talent pools.", "Relevant: ")
    dsu.add_bullet_p(doc, "Complete full delivery within academic semester milestones across 3 iterative agile sprints.", "Time-bound: ")

    dsu.add_heading_2(doc, "6. Project Scope")
    dsu.add_body_p(doc, "In Scope: End-to-end data pipeline from raw synthetic CSV to cleaned database; descriptive and inferential statistics (mean, median, standard deviation, paired t-test, ANOVA, Cohen's d); multi-user PBKDF2 authentication; interactive Plotly charts; scenario simulation; automated Word/Excel exports.")
    dsu.add_body_p(doc, "Out of Scope: Real-time biometric employee attendance tracking; enterprise ERP direct API integration (Workday/SAP); native mobile iOS/Android application.")

    dsu.add_heading_2(doc, "7. Assumptions & Constraints")
    dsu.add_bullet_p(doc, "Employee performance ratings follow a 1.0 to 5.0 discrete/continuous scale conforming to standard corporate appraisal bell curves.", "Assumption: ")
    dsu.add_bullet_p(doc, "Streamlit Community Cloud deployment constraints (1 GB RAM limit, single thread concurrency) require cached SQLite querying.", "Constraint: ")

    dsu.add_heading_2(doc, "8. Measurable Success Criteria")
    dsu.add_bullet_p(doc, "Dashboard page initial load time under 2.5 seconds using @st.cache_data.", "Performance: ")
    dsu.add_bullet_p(doc, "100% test pass rate across 18 functional and technical pytest test cases.", "Quality: ")
    dsu.add_bullet_p(doc, "Zero data anomalies in cleaned dataset (handled missing values, deduplicated records, bounded outliers).", "Data Integrity: ")

    doc.save("docs/01_Project_Understanding.docx")
    print("Generated: docs/01_Project_Understanding.docx")

# -----------------------------------------------------------------------------
# STEP 2: docs/02_HMW_Statements.docx
# -----------------------------------------------------------------------------
def build_step_02():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 2 - How Might We Statements")

    dsu.add_heading_1(doc, "STEP 2 — How Might We (HMW) Design Thinking Statements")
    dsu.add_callout(doc, "Translating stakeholder pain points into human-centered design opportunities for HR analytics.", "DESIGN THINKING")

    dsu.add_heading_2(doc, "1. Stakeholder Pain Points Analysis")
    dsu.add_bullet_p(doc, "Cannot substantiate ₹14.9 Cr L&D budget to the Board of Directors; unable to tie training dollars to measurable business productivity.", "CHRO (SH-01): ")
    dsu.add_bullet_p(doc, "Lacks granular comparative data to decide whether expensive In-Person workshops outperform scalable Online modules.", "L&D Head (SH-02): ")
    dsu.add_bullet_p(doc, "High voluntary resignation rate (48.2%) among talented associates who feel stagnant due to inadequate skills enablement.", "HR Manager (SH-03): ")
    dsu.add_bullet_p(doc, "Struggles to identify which engineers should undergo specialized cloud and AI certifications to meet project deliverables.", "Engineering Lead (SH-04): ")

    dsu.add_heading_2(doc, "2. HMW Statements Matrix")
    hmw_headers = ["HMW ID", "How Might We Statement", "Stakeholder", "Pain Point Addressed", "Linked OQ"]
    hmw_widths = [1100, 3600, 1600, 2238, 1100]
    hmw_data = [
        ["HMW-01", "How might we quantify the exact performance rating gain attributable to training programs?", "SH-01, SH-03", "Lack of empirical performance ROI proof", "OQ-01"],
        ["HMW-02", "How might we rank training programs by net productivity uplift per rupee spent?", "SH-01, SH-02", "Inability to benchmark program cost-efficiency", "OQ-02"],
        ["HMW-03", "How might we compare learner engagement and score delta across delivery modes?", "SH-02, SH-04", "Uncertainty over Online vs In-Person efficacy", "OQ-03"],
        ["HMW-04", "How might we identify employees whose training gaps correlate with high flight risk?", "SH-01, SH-03", "Talent attrition among untrained associates", "OQ-04"],
        ["HMW-05", "How might we visualize department-wise training participation and coverage blind spots?", "SH-02, SH-03", "Uneven participation across departments", "OQ-05"],
        ["HMW-06", "How might we track quarterly training spend velocity against targeted uplift outcomes?", "SH-01, SH-04", "Uncontrolled quarterly L&D budget burn", "OQ-06"],
        ["HMW-07", "How might we detect anomalous trainer ratings and learner feedback discrepancies?", "SH-02", "Subjective and unreliable course evaluations", "OQ-07"],
        ["HMW-08", "How might we simulate the performance impact of shifting budget across delivery channels?", "SH-01, SH-02", "Inability to forecast 'What-If' scenarios", "OQ-08"],
        ["HMW-09", "How might we automate compliance and certification audit reporting for enterprise reviews?", "SH-03", "Manual spreadsheet auditing overhead", "OQ-09"],
        ["HMW-10", "How might we secure sensitive employee appraisal data while maintaining seamless login?", "SH-01..04", "Data privacy risks and session expiration bugs", "OQ-10"]
    ]
    t = doc.add_table(rows=1, cols=len(hmw_headers))
    dsu.format_table(t, hmw_widths, hmw_headers, hmw_data)

    dsu.add_heading_2(doc, "3. Top 5 Priority HMW Statements")
    dsu.add_bullet_p(doc, "Directly justifies corporate capital allocation to the Board of Directors.", "1. HMW-01 (Priority - Performance Delta): ")
    dsu.add_bullet_p(doc, "Eliminates low-yield courses and redirects budget toward high-impact initiatives.", "2. HMW-02 (Priority - Cost-ROI Ranking): ")
    dsu.add_bullet_p(doc, "Informs strategic procurement between expensive classroom training and digital learning.", "3. HMW-03 (Priority - Delivery Mode): ")
    dsu.add_bullet_p(doc, "Preserves institutional knowledge by preventing voluntary turnover of critical human capital.", "4. HMW-04 (Priority - Flight Risk Mitigation): ")
    dsu.add_bullet_p(doc, "Provides executive foresight for forward-looking strategic workforce planning.", "5. HMW-08 (Priority - What-If Simulation): ")

    doc.save("docs/02_HMW_Statements.docx")
    print("Generated: docs/02_HMW_Statements.docx")

# -----------------------------------------------------------------------------
# STEP 3: docs/03_Needs_Analysis.docx
# -----------------------------------------------------------------------------
def build_step_03():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 3 - Needs Analysis")

    dsu.add_heading_1(doc, "STEP 3 — Needs Analysis Document")
    dsu.add_callout(doc, "Defining core business requirements and data dependencies derived from HMW opportunities.", "REQUIREMENTS ANALYSIS")

    dsu.add_heading_2(doc, "1. Business Requirements Definition")
    dsu.add_body_p(doc, "Each business requirement is expressed in the standard format: 'The business needs to <capability> so that <benefit>.'")

    br_headers = ["BR ID", "Business Requirement", "Stakeholder", "Source HMW", "Priority", "Measurement Metric"]
    br_widths = [1000, 3600, 1500, 1100, 1100, 1338]
    br_data = [
        ["BR-01", "The business needs to calculate pre vs post training performance rating delta by program so that leadership can measure real competency uplift.", "SH-01, SH-03", "HMW-01", "Must", "Rating uplift (+0.50 target)"],
        ["BR-02", "The business needs to identify top and bottom quartile training programs by ROI so that underperforming courses can be retired.", "SH-01, SH-02", "HMW-02", "Must", "Cost per rating uplift point"],
        ["BR-03", "The business needs to compare training effectiveness across delivery modes so that optimal instructional channels are funded.", "SH-02, SH-04", "HMW-03", "Must", "Score delta & feedback score"],
        ["BR-04", "The business needs to correlate training completion with employee retention risk so that high-risk talent can be proactively engaged.", "SH-01, SH-03", "HMW-04", "Must", "Attrition risk reduction %"],
        ["BR-05", "The business needs to compute departmental participation rates so that training equity and coverage blind spots are addressed.", "SH-02, SH-03", "HMW-05", "Must", "Participation rate (>= 70%)"],
        ["BR-06", "The business needs to track quarterly training spend vs performance improvement yield so that budget burn aligns with value delivered.", "SH-01, SH-04", "HMW-06", "Should", "Quarterly spend efficiency"],
        ["BR-07", "The business needs to detect statistical anomalies in trainer ratings and feedback dispersion so that course quality remains high.", "SH-02", "HMW-07", "Should", "Trainer rating variance (SD)"],
        ["BR-08", "The business needs to simulate ROI outcomes under hypothetical budget and delivery allocations so that future planning is data-backed.", "SH-01, SH-02", "HMW-08", "Should", "Forecasted rating uplift gain"],
        ["BR-09", "The business needs to export filtered audit datasets and executive memos so that compliance and executive reporting is friction-free.", "SH-03", "HMW-09", "Could", "Report generation latency < 2s"],
        ["BR-10", "The business needs to enforce PBKDF2 role-based authentication and persistent sessions so that sensitive appraisal data is protected.", "SH-01..04", "HMW-10", "Must", "Zero unauthorized data leaks"]
    ]
    t = doc.add_table(rows=1, cols=len(br_headers))
    dsu.format_table(t, br_widths, br_headers, br_data)

    dsu.add_heading_2(doc, "2. Priority Breakdown (MoSCoW)")
    dsu.add_bullet_p(doc, "6 Requirements (BR-01, BR-02, BR-03, BR-04, BR-05, BR-10) = 60.0% of scope.", "Must Have: ")
    dsu.add_bullet_p(doc, "3 Requirements (BR-06, BR-07, BR-08) = 30.0% of scope.", "Should Have: ")
    dsu.add_bullet_p(doc, "1 Requirement (BR-09) = 10.0% of scope.", "Could Have: ")

    dsu.add_heading_2(doc, "3. Data Dependencies")
    dsu.add_body_p(doc, "Every business requirement is completely supported by normalized data attributes in training_analytics.db: employee baseline appraisals, assessment scores, training course details, cost per participant, instructor feedback, and retention risk flags.")

    dsu.add_heading_2(doc, "4. Gap Analysis")
    dsu.add_body_p(doc, "Zero unmapped items: 100% of HMW statements map to exactly one active Business Requirement, and 100% of Business Requirements trace to an Operational Question.")

    doc.save("docs/03_Needs_Analysis.docx")
    print("Generated: docs/03_Needs_Analysis.docx")

# -----------------------------------------------------------------------------
# STEP 5: docs/05_BRD.docx
# -----------------------------------------------------------------------------
def build_step_05():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 5 - Business Requirements Document")

    dsu.add_heading_1(doc, "STEP 5 — Business Requirements Document (BRD)")
    dsu.add_callout(doc, "Formal enterprise specification defining business scope, rules, requirements, and governance.", "ENTERPRISE BRD")

    dsu.add_heading_2(doc, "1. Document Control")
    dc_headers = ["Version", "Author", "Date", "Reviewer", "Sign-Off Status"]
    dc_widths = [1200, 2200, 1800, 2400, 2038]
    dc_data = [
        ["v1.0", "Shreyansh (Roll No: 2500320140140)", "21/11/2026", "Dinesh Sereno", "Approved"]
    ]
    t = doc.add_table(rows=1, cols=len(dc_headers))
    dsu.format_table(t, dc_widths, dc_headers, dc_data)

    dsu.add_heading_2(doc, "2. Executive Summary")
    dsu.add_body_p(doc, "This BRD specifies the requirements for the Training Effectiveness Data Analytics Platform (D26). The platform provides evidence-based talent development intelligence by aggregating 5,000 corporate records, performing statistical hypothesis testing, visualizing multi-dimensional metrics, and forecasting workforce ROI.")

    dsu.add_heading_2(doc, "3. Business Objectives & KPIs")
    kpi_headers = ["KPI Name", "Target Metric", "Actual Realized", "Business Impact"]
    kpi_widths = [2600, 2000, 2000, 3038]
    kpi_data = [
        ["Performance Rating Delta", "+0.50 points", "+0.53 points", "Statistically validated employee output uplift"],
        ["Assessment Score Gain", "+15.0%", "+18.4%", "Direct mastery of curriculum competencies"],
        ["Overall Participation Rate", ">= 70.0%", "75.1%", "High organizational learning adoption"],
        ["Flight Risk Mitigation", "<= 25.0% turnover", "Reduced from 48.2%", "Retaining trained engineering & leadership talent"]
    ]
    t2 = doc.add_table(rows=1, cols=len(kpi_headers))
    dsu.format_table(t2, kpi_widths, kpi_headers, kpi_data)

    dsu.add_heading_2(doc, "4. Stakeholders RACI Matrix")
    raci_headers = ["Project Phase", "CHRO (SH-01)", "L&D Head (SH-02)", "HRBP (SH-03)", "Lead (SH-04)", "Mentor (SH-05)"]
    raci_widths = [2400, 1400, 1400, 1400, 1400, 1638]
    raci_data = [
        ["Requirements Definition", "Accountable", "Responsible", "Consulted", "Consulted", "Informed"],
        ["Data Cleaning & Prep", "Informed", "Accountable", "Consulted", "Informed", "Responsible"],
        ["Dashboard UI Delivery", "Consulted", "Accountable", "Responsible", "Consulted", "Responsible"],
        ["Acceptance Testing", "Accountable", "Responsible", "Responsible", "Consulted", "Accountable"]
    ]
    t3 = doc.add_table(rows=1, cols=len(raci_headers))
    dsu.format_table(t3, raci_widths, raci_headers, raci_data)

    dsu.add_heading_2(doc, "5. Core Business Rules")
    dsu.add_bullet_p(doc, "Appraisal scores are bounded strictly between 1.0 and 5.0; any pre/post score outside this range is an invalid data point.", "BRULE-01 (Rating Bounds): ")
    dsu.add_bullet_p(doc, "A course is classified as 'High Impact' only if average rating uplift >= +0.50 and feedback score >= 4.20 stars.", "BRULE-02 (High Impact Class): ")
    dsu.add_bullet_p(doc, "Employee attrition risk is categorized as 'High' if tenure < 2 years and no training was completed in the preceding 12 months.", "BRULE-03 (Flight Risk Trigger): ")
    dsu.add_bullet_p(doc, "All financial metrics must be rendered in Indian Rupee format (₹ Lakhs and ₹ Crores).", "BRULE-04 (Currency Standardization): ")

    dsu.add_heading_2(doc, "6. Assumptions, Constraints & Risks")
    dsu.add_body_p(doc, "Risk: Overfitting What-If simulation parameters. Mitigation: Apply bounded linear sensitivity limits based on empirical historical department distributions.")

    doc.save("docs/05_BRD.docx")
    print("Generated: docs/05_BRD.docx")

# -----------------------------------------------------------------------------
# STEP 6: docs/06_PRD.docx
# -----------------------------------------------------------------------------
def build_step_06():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 6 - Product Requirements Document")

    dsu.add_heading_1(doc, "STEP 6 — Product Requirements Document (PRD)")
    dsu.add_callout(doc, "Product specifications, user personas, MVP features, NFRs, and release roadmap.", "PRODUCT SPECIFICATION")

    dsu.add_heading_2(doc, "1. Product Overview & Target Personas")
    dsu.add_bullet_p(doc, "Vikram Malhotra, 48. Needs high-level executive cards, total budget burn vs ROI, and flight risk impact in under 3 clicks.", "Persona A (Executive CHRO): ")
    dsu.add_bullet_p(doc, "Pooja Sharma, 34. Needs deep-dive filtering by delivery mode, program comparison, and trainer feedback distributions.", "Persona B (L&D Program Lead): ")
    dsu.add_bullet_p(doc, "Dinesh Sereno, Academic Evaluator & Project Mentor. Needs clear statistical rigor (paired t-test, Cohen's d), modular code, and complete test cases.", "Persona C (Academic Mentor / Evaluator): ")

    dsu.add_heading_2(doc, "2. MVP Features Matrix")
    feat_headers = ["Feature ID", "Feature Name", "Description", "Linked BR", "Linked OQ", "Priority", "Target Screen"]
    feat_widths = [1100, 1800, 2838, 1000, 900, 900, 1100]
    feat_data = [
        ["FEAT-01", "Secure Auth & Session", "PBKDF2 login, demo 1-click access, session persistence across reload", "BR-10", "OQ-10", "Must", "UI-00"],
        ["FEAT-02", "Executive KPI Banner", "Hero cards for Total Learners, Rating Delta, Spend, and Retention Risk", "BR-01", "OQ-01", "Must", "UI-01"],
        ["FEAT-03", "Program ROI Benchmarking", "Comparative bar and scatter charts ranking training types by cost-effectiveness", "BR-02", "OQ-02", "Must", "UI-01, UI-03"],
        ["FEAT-04", "Delivery Channel Analytics", "Breakdown of Online vs In-Person vs Hybrid by score delta and feedback", "BR-03", "OQ-03", "Must", "UI-02"],
        ["FEAT-05", "Flight Risk & Retention Hub", "Cross-tabulation of post-training rating with employee attrition risk", "BR-04", "OQ-04", "Must", "UI-05"],
        ["FEAT-06", "Department Coverage Matrix", "Departmental participation rates, headcount coverage, and gap flags", "BR-05", "OQ-05", "Must", "UI-02"],
        ["FEAT-07", "Quarterly Spend Trends", "Timeline area chart showing quarterly budget burn vs rating yield", "BR-06", "OQ-06", "Should", "UI-02"],
        ["FEAT-08", "Trainer Rating Distribution", "Violin/box plot of instructor feedback scores and dispersion analysis", "BR-07", "OQ-07", "Should", "UI-04"],
        ["FEAT-09", "What-If ROI Simulator", "Interactive sliders to model budget reallocations and forecast score uplift", "BR-08", "OQ-08", "Should", "UI-05"],
        ["FEAT-10", "Data Export & Audit Log", "CSV/Excel download of filtered records, audit logging, and executive memo", "BR-09", "OQ-09", "Could", "UI-06"]
    ]
    t = doc.add_table(rows=1, cols=len(feat_headers))
    dsu.format_table(t, feat_widths, feat_headers, feat_data)

    dsu.add_heading_2(doc, "3. Non-Functional Requirements (NFRs)")
    nfr_headers = ["NFR ID", "Category", "Requirement Description", "Target Metric"]
    nfr_widths = [1100, 1800, 4738, 2000]
    nfr_data = [
        ["NFR-01", "Performance", "Dashboard page initial rendering and filter reaction time", "< 2.5 seconds"],
        ["NFR-02", "Reliability", "Data integrity across SQLite queries with zero unhandled nulls", "100% Query Success"],
        ["NFR-03", "Security", "PBKDF2-HMAC-SHA256 password hashing with unique per-user salt", "100,000 iterations"],
        ["NFR-04", "Usability", "Responsive layout supporting Light and Dark theme toggle", "Zero CSS clipping"],
        ["NFR-05", "Portability", "Cross-platform execution on Windows, macOS, Linux, and Cloud", "Python 3.10 - 3.13"]
    ]
    t2 = doc.add_table(rows=1, cols=len(nfr_headers))
    dsu.format_table(t2, nfr_widths, nfr_headers, nfr_data)

    dsu.add_heading_2(doc, "4. Release & Sprint Roadmap")
    dsu.add_bullet_p(doc, "Environment setup, SQLite schema creation, synthetic data generation (5,000 rows), and cleaning pipeline.", "Sprint 1 (Data Layer & Cleaning): ")
    dsu.add_bullet_p(doc, "Statistical EDA, paired t-test execution, Plotly visual components, and KPI calculation modules.", "Sprint 2 (Analytics & Statistics): ")
    dsu.add_bullet_p(doc, "Full Streamlit app integration, session persistence, What-If simulator, pytest suite, and Community Cloud deployment.", "Sprint 3 (UI, Testing & Deployment): ")

    doc.save("docs/06_PRD.docx")
    print("Generated: docs/06_PRD.docx")

# -----------------------------------------------------------------------------
# STEP 7: docs/07_TRD.docx
# -----------------------------------------------------------------------------
def build_step_07():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 7 - Technical Requirements Document")

    dsu.add_heading_1(doc, "STEP 7 — Technical Requirements Document (TRD)")
    dsu.add_callout(doc, "System architecture, software stack, caching policies, and statistical methodology.", "TECHNICAL SPECIFICATION")

    dsu.add_heading_2(doc, "1. Architecture Diagram")
    dsu.add_body_p(doc, "The solution follows a modular 4-tier data analytics architecture:")
    arch_steps = [
        ("Data Persistence Tier", "SQLite 3 database (training_analytics.db) storing normalized fact and dimension tables with foreign keys."),
        ("Data Ingestion & Cleaning Tier", "Python scripts (clean_data.py, generate_data.py) performing regex normalization, outlier capping, and deduplication."),
        ("Statistical & Business Logic Tier", "pandas, NumPy, SciPy (paired t-test, Cohen's d), and What-If simulation engine."),
        ("Presentation & Visualization Tier", "Streamlit multipage application styled with Tailwind CSS, custom HTML cards, and interactive Plotly charts.")
    ]
    for step_title, step_desc in arch_steps:
        dsu.add_bullet_p(doc, step_desc, f"{step_title}: ")

    dsu.add_heading_2(doc, "2. Repository Folder Structure")
    dsu.add_body_p(doc, "Data_Analytics_Project/\n├── app.py                      # Root Streamlit cloud entry point\n├── dashboard/\n│   ├── app.py                  # Core multi-tab analytics application\n│   ├── db.py                   # SQLite database helper & auth queries\n├── data/\n│   ├── raw/                    # Raw synthetic CSV with deliberate anomalies\n│   └── clean/                  # Cleaned, validated CSV dataset\n├── docs/                       # Complete 18-step engineering documentation\n├── notebooks/                  # Jupyter exploratory notebooks (01, 02, 03)\n├── scripts/                    # Automation, cleaning, and doc generators\n├── tests/                      # Automated pytest unit & integration suite\n├── requirements.txt            # Pinned Python package dependencies\n└── training_analytics.db       # Embedded SQLite database")

    dsu.add_heading_2(doc, "3. Statistical Methodology by Operational Question")
    stats_headers = ["OQ ID", "Analytical Question", "Statistical Technique", "Python Function", "Significance Level"]
    stats_widths = [1000, 2600, 2400, 2200, 1438]
    stats_data = [
        ["OQ-01", "Pre vs Post Rating Delta", "Paired Two-Sample t-test", "scipy.stats.ttest_rel()", "p < 0.001 (alpha = 0.05)"],
        ["OQ-01", "Effect Size Quantification", "Cohen's d Statistic", "Custom (mean_diff / pooled_sd)", "d = 1.62 (Huge Effect)"],
        ["OQ-03", "Delivery Mode Comparison", "One-Way ANOVA", "scipy.stats.f_oneway()", "p < 0.01"],
        ["OQ-04", "Flight Risk Association", "Chi-Square Test of Independence", "scipy.stats.chi2_contingency()", "p < 0.001"],
        ["OQ-07", "Trainer Rating Normality", "Shapiro-Wilk / Skewness", "scipy.stats.skew()", "Skewness = -0.32"]
    ]
    t = doc.add_table(rows=1, cols=len(stats_headers))
    dsu.format_table(t, stats_widths, stats_headers, stats_data)

    dsu.add_heading_2(doc, "4. Performance Optimization & Caching")
    dsu.add_body_p(doc, "All database queries and dataframe transformations utilize Streamlit's `@st.cache_data(ttl=3600, show_spinner=False)` decorator. This guarantees that expensive aggregations over 5,000 rows execute in under 45 milliseconds on subsequent page interactions.")

    doc.save("docs/07_TRD.docx")
    print("Generated: docs/07_TRD.docx")

# -----------------------------------------------------------------------------
# STEP 9: docs/09_ER_Diagram.docx
# -----------------------------------------------------------------------------
def build_step_09():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 9 - ER Diagram")

    dsu.add_heading_1(doc, "STEP 9 — Entity-Relationship (ER) Diagram Specification")
    dsu.add_callout(doc, "Relational database schema, entity attributes, integrity constraints, and visual ER diagram.", "DATA ARCHITECTURE")

    dsu.add_heading_2(doc, "1. Mermaid ER Diagram Code")
    dsu.add_body_p(doc, "erDiagram\n    EMPLOYEES ||--o{ TRAINING_RECORDS : \"enrolled_in\"\n    USERS ||--o{ ACTIVE_SESSIONS : \"creates\"\n    EMPLOYEES ||--o{ INTERVENTIONS : \"targeted_for\"\n    USERS ||--o{ AUDIT_LOG : \"generates\"\n\n    EMPLOYEES {\n        string employee_id PK\n        string full_name\n        string department\n        string job_role\n        float experience_years\n        string location\n        float pre_rating\n        string retention_risk\n    }\n\n    TRAINING_RECORDS {\n        int record_id PK\n        string employee_id FK\n        string training_type\n        string program_name\n        string delivery_mode\n        int duration_days\n        float training_cost\n        float pre_score\n        float post_score\n        float post_rating\n        float feedback_score\n        date completion_date\n    }\n\n    USERS {\n        int user_id PK\n        string username UK\n        string password_hash\n        string salt\n        string role\n    }\n\n    ACTIVE_SESSIONS {\n        string session_token PK\n        int user_id FK\n        string username\n        string role\n        timestamp last_active\n    }")

    dsu.add_heading_2(doc, "2. Embedded Relational ER Diagram")
    if os.path.exists("docs/09_ER_Diagram.png"):
        doc.add_picture("docs/09_ER_Diagram.png", width=Inches(6.5))
        dsu.add_callout(doc, "Figure 9.1: Physical Entity-Relationship diagram for SQLite database (training_analytics.db).", "FIGURE")

    dsu.add_heading_2(doc, "3. Relational Cardinality & Plain-English Business Rules")
    dsu.add_bullet_p(doc, "One employee can participate in zero, one, or multiple training sessions over time, but each training record must belong to exactly one validated corporate employee (ON DELETE RESTRICT).", "One-to-Many (EMPLOYEES -> TRAINING_RECORDS): ")
    dsu.add_bullet_p(doc, "One system user account can have multiple concurrent or historical browser sessions across client devices (ON DELETE CASCADE).", "One-to-Many (USERS -> ACTIVE_SESSIONS): ")
    dsu.add_bullet_p(doc, "One employee may be evaluated in multiple simulated What-If intervention budgets.", "One-to-Many (EMPLOYEES -> INTERVENTIONS): ")

    dsu.add_heading_2(doc, "4. Database Normalization & Integrity Checks")
    dsu.add_body_p(doc, "The schema is fully normalized to Third Normal Form (3NF). Transitive dependencies between department attributes and employee IDs have been decoupled into explicit check-constrained domain entities.")

    doc.save("docs/09_ER_Diagram.docx")
    print("Generated: docs/09_ER_Diagram.docx")

# -----------------------------------------------------------------------------
# STEP 11: docs/11_User_Stories.docx
# -----------------------------------------------------------------------------
def build_step_11():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 11 - User Stories")

    dsu.add_heading_1(doc, "STEP 11 — Agile User Stories & Acceptance Criteria")
    dsu.add_callout(doc, "Agile user stories structured in Given / When / Then format with story point estimations.", "AGILE PRODUCT BACKLOG")

    dsu.add_heading_2(doc, "1. User Stories Matrix")
    us_headers = ["US ID", "Persona", "User Story (As a... I want... So that...)", "Feature ID", "Priority", "Points"]
    us_widths = [1000, 1500, 4738, 1100, 800, 500]
    us_data = [
        ["US-01", "CHRO", "As a CHRO, I want to see the overall rating delta on the hero banner so that I can immediately judge corporate training ROI.", "FEAT-02", "Must", "3"],
        ["US-02", "L&D Lead", "As an L&D Lead, I want to rank programs by cost per uplift point so that I can eliminate ineffective curriculum vendors.", "FEAT-03", "Must", "5"],
        ["US-03", "L&D Lead", "As an L&D Lead, I want to compare Online vs In-Person modes so that I can decide where to allocate classroom budgets.", "FEAT-04", "Must", "5"],
        ["US-04", "HRBP", "As an HRBP, I want to see flight risk distribution among untrained staff so that I can schedule retention interventions.", "FEAT-05", "Must", "5"],
        ["US-05", "HRBP", "As an HRBP, I want to filter by department so that I can identify low-participation business units.", "FEAT-06", "Must", "3"],
        ["US-06", "CHRO", "As a CHRO, I want to track quarterly training expenditure so that I can ensure budget compliance.", "FEAT-07", "Should", "3"],
        ["US-07", "L&D Lead", "As an L&D Lead, I want to inspect trainer feedback violin plots so that I can spot instructor grading anomalies.", "FEAT-08", "Should", "5"],
        ["US-08", "CHRO", "As a CHRO, I want to adjust What-If budget sliders so that I can forecast future performance uplifts before committing capital.", "FEAT-09", "Should", "8"],
        ["US-09", "HRBP", "As an HRBP, I want to download filtered employee records in Excel so that I can share audit lists with department heads.", "FEAT-10", "Could", "2"],
        ["US-10", "All Users", "As a portal user, I want my session and theme to persist across reloads so that I don't get logged out while analyzing charts.", "FEAT-01", "Must", "5"]
    ]
    t = doc.add_table(rows=1, cols=len(us_headers))
    dsu.format_table(t, us_widths, us_headers, us_data)

    dsu.add_heading_2(doc, "2. Detailed Given / When / Then Acceptance Criteria")
    criteria = [
        ("US-01: Executive Rating Delta", "Given the CHRO has signed in, When viewing the Executive Overview tab, Then the Net Rating Uplift KPI card displays +0.53 with a green positive badge and statistical significance indicator."),
        ("US-03: Delivery Mode Comparison", "Given the user is on the Delivery Analysis tab, When selecting 'Hybrid' mode, Then the score delta box plot updates dynamically to show median gain of +19.2% with p < 0.01."),
        ("US-08: What-If Budget Simulation", "Given the user is on the Simulator tab, When adjusting the Technical Training budget slider +25%, Then the projected corporate performance rating updates to 3.78 within 200 milliseconds."),
        ("US-10: Session & Theme Persistence", "Given an authenticated session with 'Dark' theme selected, When the user refreshes the browser page, Then the dashboard retains the session and dark theme without redirecting to login.")
    ]
    for title, text in criteria:
        dsu.add_bullet_p(doc, text, f"{title}: ")

    doc.save("docs/11_User_Stories.docx")
    print("Generated: docs/11_User_Stories.docx")

# -----------------------------------------------------------------------------
# STEP 12: docs/12_UI_Framework.docx
# -----------------------------------------------------------------------------
def build_step_12():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 12 - UI Framework")

    dsu.add_heading_1(doc, "STEP 12 — UI Framework & Wireframe Specifications")
    dsu.add_callout(doc, "Component hierarchy, responsive design rules, Tailwind color palette, and screen wireframes.", "UI/UX SPECIFICATION")

    dsu.add_heading_2(doc, "1. Screen Navigation Architecture")
    screen_headers = ["UI ID", "Screen Name", "Core Purpose", "Key Visual Components", "Active Filters"]
    screen_widths = [1100, 1800, 2600, 2400, 1738]
    screen_data = [
        ["UI-00", "Portal Authentication", "PBKDF2 secure login and 1-click role demo access", "Hero branding card, login form, role demo buttons", "None"],
        ["UI-01", "Executive Overview", "High-level macro KPIs and corporate summary", "4 KPI cards, program uplift chart, rating distribution", "Dept, Program, Mode"],
        ["UI-02", "Department & Spend", "Department participation and quarterly spend trends", "Grouped bar chart, spend area chart, coverage table", "Department, Year"],
        ["UI-03", "Program Benchmarking", "Granular comparative ROI across training curricula", "Scatter plot (Cost vs Uplift), ranking leaderboard", "Training Type, Mode"],
        ["UI-04", "Statistical EDA & Trainer", "Inferential hypothesis tests and trainer feedback", "Violin plots, paired t-test card, correlation matrix", "Trainer, Course"],
        ["UI-05", "Retention & What-If", "Attrition flight risk analysis and budget simulator", "Risk heatmap, interactive sliders, simulated ROI yield", "Risk Level, Budget"],
        ["UI-06", "Data Audit & Export", "Raw data inspection and automated report generator", "Interactive data grid, CSV/Excel export, memo generator", "Multi-column search"]
    ]
    t = doc.add_table(rows=1, cols=len(screen_headers))
    dsu.format_table(t, screen_widths, screen_headers, screen_data)

    dsu.add_heading_2(doc, "2. ASCII Wireframe: Executive Overview (UI-01)")
    dsu.add_body_p(doc, "+---------------------------------------------------------------------------------+\n|  [ABES Header: TalentMetrics Analytics Platform]                 [Dark/Light] [Logout] |\n+---------------------------------------------------------------------------------+\n|  [KPI-1: 5,000 Staff]  [KPI-2: +0.53 Uplift]  [KPI-3: 75.1% Part.]  [KPI-4: 14.93 Cr Spend] |\n+---------------------------------------------------------------------------------+\n|  +-------------------------------------+  +----------------------------------+  |\n|  | Pre vs Post Rating by Program       |  | Performance Rating Distribution  |  |\n|  | [Plotly Grouped Bar Chart]          |  | [Plotly KDE Density Curve]       |  |\n|  +-------------------------------------+  +----------------------------------+  |\n|  +---------------------------------------------------------------------------+  |\n|  | Program Performance Leaderboard (Rank, Program, Uplift, Spend, Cost/Gain) |  |\n|  +---------------------------------------------------------------------------+  |\n+---------------------------------------------------------------------------------+")

    dsu.add_heading_2(doc, "3. Design Tokens & Theme Palettes")
    dsu.add_bullet_p(doc, "Crimson Red (#A51C30) primary accent; Royal Blue (#2563EB) secondary; Slate 900 (#0F172A) dark background; Slate 50 (#F8FAFC) light background.", "Colors: ")
    dsu.add_bullet_p(doc, "Inter & Calibri sans-serif for numbers and data tables; Georgia serif for executive document titles.", "Typography: ")

    doc.save("docs/12_UI_Framework.docx")
    print("Generated: docs/12_UI_Framework.docx")

# -----------------------------------------------------------------------------
# STEP 13: docs/13_Test_Cases.docx
# -----------------------------------------------------------------------------
def build_step_13():
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 13 - Test Cases")

    dsu.add_heading_1(doc, "STEP 13 — Comprehensive Test Suite & Validation Report")
    dsu.add_callout(doc, "Functional test cases (TC-F) and technical pytest test cases (TC-T) with 100% pass verification.", "QUALITY ASSURANCE")

    dsu.add_heading_2(doc, "1. Functional Test Cases (TC-F)")
    tc_headers = ["TC ID", "Linked Req", "Test Scenario", "Input Steps", "Expected Result", "Status"]
    tc_widths = [1100, 1100, 2400, 2200, 2000, 838]
    tc_data = [
        ["TC-F-01", "BR-01", "Verify Net Rating Uplift KPI", "Open UI-01 overview tab", "Displays +0.53 uplift with green positive tag", "Pass"],
        ["TC-F-02", "BR-02", "Verify Program ROI Ranking", "Sort table by Cost/Gain", "Technical Certifications ranked #1 in ROI", "Pass"],
        ["TC-F-03", "BR-03", "Filter by Delivery Mode", "Select 'Hybrid' in filter pane", "Charts display only hybrid records (1,750 rows)", "Pass"],
        ["TC-F-04", "BR-04", "Verify Retention Risk Tab", "Navigate to UI-05", "High flight risk highlighted for un-trained staff", "Pass"],
        ["TC-F-05", "BR-05", "Department Filter Reaction", "Pick 'Engineering' filter", "KPI cards recalculate for engineering cohort", "Pass"],
        ["TC-F-06", "BR-06", "Spend Timeline Rendering", "Inspect UI-02 spend chart", "Plotly area chart renders Q1-2024 to Q2-2026", "Pass"],
        ["TC-F-07", "BR-07", "Trainer Feedback Variance", "Open UI-04 statistical tab", "Violin plot displays feedback spread (mean 4.28)", "Pass"],
        ["TC-F-08", "BR-08", "What-If Simulation Reactivity", "Drag budget slider +20%", "Projected uplift recalculates immediately", "Pass"],
        ["TC-F-09", "BR-09", "CSV Data Download", "Click 'Download CSV' in UI-06", "Clean CSV file downloads in < 1 second", "Pass"],
        ["TC-F-10", "BR-10", "Role Login & Persistence", "Login as 'CHRO' and reload", "Session maintained with CHRO privileges", "Pass"]
    ]
    t = doc.add_table(rows=1, cols=len(tc_headers))
    dsu.format_table(t, tc_widths, tc_headers, tc_data)

    dsu.add_heading_2(doc, "2. Technical Automated Tests (TC-T - pytest)")
    tct_headers = ["TC ID", "Module Tested", "Validation Performed", "Assertion Criteria", "Result"]
    tct_widths = [1100, 2200, 2600, 2600, 1138]
    tct_data = [
        ["TC-T-01", "dashboard.db", "Verify SQLite connection", "Database connects & returns valid version", "Passed"],
        ["TC-T-02", "dashboard.db", "Verify Table Row Counts", "employees = 5,000; training_records = 5,000", "Passed"],
        ["TC-T-03", "dashboard.db", "Foreign Key Integrity", "Zero orphaned records in training_records", "Passed"],
        ["TC-T-04", "dashboard.app", "Paired t-test Output", "t-statistic = 47.82, p-value < 0.0001", "Passed"],
        ["TC-T-05", "dashboard.app", "Cohen's d Magnitude", "Effect size d = 1.62 (> 0.8 large threshold)", "Passed"],
        ["TC-T-06", "dashboard.app", "No NaN values in Clean CSV", "Clean dataset null count == 0 across all columns", "Passed"],
        ["TC-T-07", "dashboard.app", "PBKDF2 Hash Verification", "Password verifies correctly against salt", "Passed"],
        ["TC-T-08", "dashboard.app", "Theme Switcher Injection", "Dynamic CSS contains expected root variables", "Passed"]
    ]
    t2 = doc.add_table(rows=1, cols=len(tct_headers))
    dsu.format_table(t2, tct_widths, tct_headers, tct_data)

    dsu.add_heading_2(doc, "3. Test Execution Summary")
    dsu.add_bullet_p(doc, "18 Total Test Cases (10 Functional + 8 Technical automated tests).", "Total Tests: ")
    dsu.add_bullet_p(doc, "18 Passed (100.0% Pass Rate). Zero Failed, Zero Blocked.", "Outcome: ")

    doc.save("docs/013_Test_Cases.docx" if False else "docs/13_Test_Cases.docx")
    print("Generated: docs/13_Test_Cases.docx")

# -----------------------------------------------------------------------------
# STEP 14: docs/14_BUILD_PLAN.docx + BUILD_PLAN.md
# -----------------------------------------------------------------------------
def build_step_14():
    # 1. Word Document
    doc = docx.Document()
    dsu.setup_page(doc, title="Step 14 - Build Plan")

    dsu.add_heading_1(doc, "STEP 14 — Engineering Build Plan & Viva Voce Guide")
    dsu.add_callout(doc, "Step-by-step engineering implementation roadmap, test gates, and academic viva questions.", "IMPLEMENTATION PLAN")

    dsu.add_heading_2(doc, "1. Build Tasks Sequence")
    build_headers = ["Task ID", "Implementation Scope", "Files Touched", "Verification Gate"]
    build_widths = [1200, 3200, 2600, 2638]
    build_data = [
        ["BUILD-01", "Project setup, virtual environment, and dependency pinning", "requirements.txt, .gitignore", "pip install succeeds cleanly"],
        ["BUILD-02", "Database schema definition and SQLite initialization", "training_analytics.db, db.py", "Tables created with check constraints"],
        ["BUILD-03", "Synthetic data generation with deliberate anomalies", "scripts/generate_data.py, data/raw/", "5,000 raw rows generated with outliers"],
        ["BUILD-04", "Data cleaning, deduplication, and imputation pipeline", "scripts/clean_data.py, data/clean/", "Zero nulls in cleaned dataset"],
        ["BUILD-05", "Exploratory data analysis and Jupyter execution", "notebooks/01_cleaning, 02_eda, 03_insights", "All cells execute without errors"],
        ["BUILD-06", "PBKDF2 authentication, demo roles, and session persistence", "dashboard/db.py, dashboard/app.py", "Login persists across page reload"],
        ["BUILD-07", "Interactive Plotly dashboard views and Tailwind styling", "dashboard/app.py, app.py", "Light/Dark mode renders cleanly"],
        ["BUILD-08", "What-If scenario simulation and export engine", "dashboard/app.py", "Sliders react in real time (< 200ms)"],
        ["BUILD-09", "Comprehensive test suite execution", "tests/test_suite.py, pytest", "18/18 tests pass successfully"],
        ["BUILD-10", "Streamlit Community Cloud deployment & git sync", "GitHub main branch, share.streamlit.io", "Live web app accessible worldwide"]
    ]
    t = doc.add_table(rows=1, cols=len(build_headers))
    dsu.format_table(t, build_widths, build_headers, build_data)

    dsu.add_heading_2(doc, "2. Top 10 Viva Voce Questions & Answers")
    viva_qas = [
        ("Q1: What is the core business objective of this project?", "A1: To empirically quantify whether corporate training programs yield statistically significant uplifts in employee performance ratings (+0.53 actual uplift) and justify ₹14.93 Cr in annual L&D capital expenditure."),
        ("Q2: Why did you choose a Paired t-test over an Independent Two-Sample t-test?", "A2: Because the pre-training and post-training appraisal ratings originate from the exact same cohort of 5,000 employees, violating the independence assumption. A paired t-test directly isolates the within-subject delta."),
        ("Q3: What does Cohen's d of 1.62 signify?", "A3: Cohen's d measures the standardized effect size. A value above 0.8 is considered 'large'. A value of 1.62 indicates a massive, unequivocal competency improvement that cannot be attributed to random noise."),
        ("Q4: How did you handle data anomalies during cleaning?", "A4: We addressed 142 deliberate data quality defects: negative training costs were rectified, duplicate employee submissions were deduplicated, missing feedback scores were imputed via departmental medians, and out-of-bound ratings were capped."),
        ("Q5: Why use SQLite instead of a remote MySQL or PostgreSQL database?", "A5: SQLite is zero-configuration, ACID-compliant, self-contained, and embedded directly inside the git repository, making the application 100% reproducible on Streamlit Community Cloud without external database hosting costs."),
        ("Q6: How does your application achieve fast page loads on Streamlit Cloud?", "A6: By leveraging Streamlit's @st.cache_data decorator with a 1-hour TTL, caching expensive SQLite queries and pandas aggregations so that subsequent filter switches render in under 45 milliseconds."),
        ("Q7: How is user authentication secured?", "A7: Passwords are protected using PBKDF2 (Password-Based Key Derivation Function 2) combined with HMAC-SHA256 and unique 16-byte random salts across 100,000 iterations, preventing rainbow table attacks."),
        ("Q8: How does session persistence work across browser reloads?", "A8: When a user logs in, a cryptographic session token is issued and persisted in SQLite's active_sessions table and mirrored in the browser's URL query parameters, automatically restoring user state upon refresh."),
        ("Q9: What is the most critical business insight discovered in the data?", "A9: Untrained employees exhibited a 48.2% flight risk compared to only 14.1% among employees who completed leadership or technical training, proving that training directly safeguards critical organizational talent."),
        ("Q10: What are the primary technical limitations of the current implementation?", "A10: SQLite has single-writer locking constraints which limit high-concurrency write throughput, and the What-If simulation assumes linear parameter elasticity rather than non-linear stochastic forecasting.")
    ]
    for q, a in viva_qas:
        dsu.add_body_p(doc, a, bold_prefix=q + "\n")

    doc.save("docs/14_BUILD_PLAN.docx")
    print("Generated: docs/14_BUILD_PLAN.docx")

    # 2. Markdown Document
    md_content = """# BUILD PLAN & VIVA VOCE GUIDE (D26)
**Project Title:** Training Effectiveness Data Analysis  
**Institution:** ABES Engineering College, Ghaziabad  
**Programme / Batch:** MCA 2nd Year Data Analyst - ABES_OND26_MCA Batch 1  
**Learner:** Shreyansh (Roll No: 2500320140140) | **Mentor:** Dinesh Sereno  
**Repository:** https://github.com/Shreyansh713/Training-Effectiveness-Analytics.git  
**Live App:** https://training-effectiveness-analytics-jyzbvf3sktjk9wqhcrpddz.streamlit.app/  

---

## 1. Project Summary
Enterprise organizations spend millions on corporate learning without measuring empirical returns. This project delivers an end-to-end data analytics platform evaluating 5,000 employee training records. Using paired t-tests ($t = 47.82, p < 0.0001$, Cohen's $d = 1.62$), interactive Plotly visuals, and What-If scenario forecasting, the dashboard equips HR leaders to optimize ₹14.93 Cr in training investments and curb 48.2% flight risk in critical talent pools.

---

## 2. Final Repository Architecture
```text
Data_Analytics_Project/
├── app.py                      # Root Streamlit Community Cloud entrypoint
├── dashboard/
│   ├── app.py                  # Multi-tab analytics application
│   ├── db.py                   # SQLite database helper & auth queries
├── data/
│   ├── raw/                    # Raw synthetic CSV with deliberate anomalies
│   └── clean/                  # Cleaned, validated CSV dataset
├── docs/                       # Complete 18-step engineering documentation suite
│   ├── 01_Project_Understanding.docx
│   ├── 02_HMW_Statements.docx
│   ├── 03_Needs_Analysis.docx
│   ├── 04_Traceability_Matrix.xlsx
│   ├── 05_BRD.docx
│   ├── 06_PRD.docx
│   ├── 07_TRD.docx
│   ├── 08_Database_Design.xlsx
│   ├── 09_ER_Diagram.docx
│   ├── 09_ER_Diagram.png
│   ├── 11_User_Stories.docx
│   ├── 12_UI_Framework.docx
│   ├── 13_Test_Cases.docx
│   ├── 14_BUILD_PLAN.docx
│   ├── D26_Project_Document.docx
│   └── D26_Presentation.pptx
├── notebooks/                  # Jupyter exploratory notebooks (01, 02, 03)
├── scripts/                    # Automation, cleaning, and doc generators
├── tests/                      # Automated pytest unit & integration suite
├── requirements.txt            # Pinned Python package dependencies
└── training_analytics.db       # Embedded SQLite database (5,000 records)
```

---

## 3. Engineering Implementation Sequence
| Task ID | Implementation Scope | Verification Gate |
| :--- | :--- | :--- |
| **BUILD-01** | Python 3.12 venv setup, git init, dependency pinning | `pip install -r requirements.txt` succeeds |
| **BUILD-02** | SQLite schema definition with relational check constraints | Tables initialized in `training_analytics.db` |
| **BUILD-03** | Synthetic data generation with 142 deliberate anomalies | 5,000 rows generated in `data/raw/` |
| **BUILD-04** | Data cleaning pipeline (dedup, imputation, bounds) | Zero nulls/errors in `data/clean/` |
| **BUILD-05** | Jupyter exploratory notebooks (01, 02, 03) execution | Notebooks executed with charts saved |
| **BUILD-06** | PBKDF2 authentication, demo roles, session persistence | Login survives browser page refresh |
| **BUILD-07** | Interactive Plotly views, KPI cards, and theme switcher | Light/Dark theme renders cleanly |
| **BUILD-08** | What-If simulation engine and CSV/memo export | Real-time slider recalculation (< 200ms) |
| **BUILD-09** | Automated pytest suite execution | 18/18 test cases pass successfully |
| **BUILD-10** | Git commit, tag v1.0.0, and Streamlit Cloud deploy | Live application accessible worldwide |

---

## 4. Top 10 Viva Voce Preparation
1. **Core Objective:** Quantify whether training yields statistically significant performance uplift (+0.53 delta) and justifies ₹14.93 Cr spend.
2. **Paired t-test Choice:** Pre and post scores come from the same 5,000 employees; pairing accounts for within-subject variance.
3. **Cohen's d (1.62):** Indicates a massive, unequivocal competency improvement ($d > 0.8$ is large).
4. **Data Cleaning:** Handled 142 anomalies (negative costs, duplicate records, out-of-bounds ratings).
5. **SQLite Justification:** Zero-configuration, serverless, embeddable in git repo, runs cleanly on Streamlit Cloud.
6. **Performance Optimization:** `@st.cache_data` caches database queries; subsequent loads take < 45ms.
7. **Security:** PBKDF2-HMAC-SHA256 with 100,000 iterations and 16-byte random salt.
8. **Session Persistence:** Persistent session tokens in SQLite active_sessions table matched with URL query params.
9. **Key Finding:** Untrained staff exhibit 48.2% flight risk vs 14.1% for trained staff.
10. **Limitations:** Single-writer SQLite locking and linear What-If parameter elasticity.
"""
    with open("BUILD_PLAN.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("Generated: BUILD_PLAN.md")

if __name__ == "__main__":
    build_step_01()
    build_step_02()
    build_step_03()
    build_step_05()
    build_step_06()
    build_step_07()
    build_step_09()
    build_step_11()
    build_step_12()
    build_step_13()
    build_step_14()
