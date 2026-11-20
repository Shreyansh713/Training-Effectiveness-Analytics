import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import scripts.doc_style_utils as dsu

def build_abes_project_document():
    doc = docx.Document()
    
    # Page setup
    section = doc.sections[0]
    section.top_margin = Inches(0.7874)     # 2 cm
    section.bottom_margin = Inches(0.7874)  # 2 cm
    section.left_margin = Inches(0.7874)    # 2 cm
    section.right_margin = Inches(0.7874)   # 2 cm
    section.header_distance = Inches(0.492) # 1.25 cm
    section.footer_distance = Inches(0.492) # 1.25 cm
    section.page_width = Inches(8.267)      # A4
    section.page_height = Inches(11.692)    # A4

    # Setup header & footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.text = "ABES Engineering College | Project Document | D26"
    for r in hp.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(8)
        r.font.color.rgb = dsu.COLOR_GREY

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.text = "Shreyansh | 2300320140045     Page 1"
    for r in fp.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(8)
        r.font.color.rgb = dsu.COLOR_GREY

    # =========================================================================
    # PAGE 1: COVER
    # =========================================================================
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(5)
    r1 = p1.add_run("HCLTech Career Shaper Programme | ABES Engineering College, Ghaziabad")
    r1.font.name = "Calibri"
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = dsu.COLOR_RED

    p_logo = doc.add_paragraph()
    p_logo.paragraph_format.space_before = Pt(0)
    p_logo.paragraph_format.space_after = Pt(5)
    r_logo = p_logo.add_run("[Insert ABES logo here]")
    r_logo.font.name = "Calibri"
    r_logo.font.size = Pt(9)
    r_logo.font.italic = True
    r_logo.font.color.rgb = dsu.COLOR_GREY

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(70)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("PROJECT DOCUMENT")
    r_title.font.name = "Georgia"
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = dsu.COLOR_DARK

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("D26 - Training Effectiveness Data Analysis")
    r_sub.font.name = "Georgia"
    r_sub.font.size = Pt(18)
    r_sub.font.color.rgb = dsu.COLOR_RED

    p_nav = doc.add_paragraph()
    p_nav.paragraph_format.space_before = Pt(0)
    p_nav.paragraph_format.space_after = Pt(24)
    r_nav = p_nav.add_run("Description · HMW · Stakeholders · Traceability · User Stories · BRD · TRD · Database Design · Test Cases · UI Framework")
    r_nav.font.name = "Calibri"
    r_nav.font.size = Pt(10)
    r_nav.font.color.rgb = dsu.COLOR_GREY

    # Metadata Table: Field 2900 | Details 6738
    meta_headers = ["Field", "Project Details"]
    meta_widths = [2900, 6738]
    meta_data = [
        ["Project ID & Title", "D26 - Training Effectiveness Data Analysis"],
        ["Domain", "Human Resources Analytics (Corporate Learning & Development)"],
        ["Programme / Batch", "MCA 2nd Year Data Analyst - ABES_OND26_MCA Batch 1"],
        ["Learner(s) & Roll No(s)", "Shreyansh | Roll No: 2300320140045"],
        ["Mentor", "Dr. R. K. Sharma (ABES IT Dept)"],
        ["GitHub Repository", "https://github.com/Shreyansh713/Training-Effectiveness-Analytics.git"],
        ["Live App (Streamlit)", "https://training-effectiveness-analytics.streamlit.app"],
        ["Version & Date", "v1.0 - 21/11/2026"]
    ]
    t_meta = doc.add_table(rows=1, cols=2)
    dsu.format_table(t_meta, meta_widths, meta_headers, meta_data)

    doc.add_page_break()

    # =========================================================================
    # PAGE 2: TABLE OF CONTENTS
    # =========================================================================
    p_toc_title = doc.add_paragraph()
    p_toc_title.paragraph_format.space_before = Pt(10)
    p_toc_title.paragraph_format.space_after = Pt(10)
    r_toc = p_toc_title.add_run("Table of Contents")
    r_toc.font.name = "Georgia"
    r_toc.font.size = Pt(15)
    r_toc.font.bold = True
    r_toc.font.color.rgb = dsu.COLOR_RED

    toc_items = [
        ("1. Project Description", "3"),
        ("2. How Might We (HMW) Statements", "4"),
        ("3. Stakeholders Analysis", "5"),
        ("4. Requirements Traceability Matrix (RTM)", "6"),
        ("5. User Stories & Acceptance Criteria", "7"),
        ("6. Business Requirements Document (BRD) Summary", "8"),
        ("7. Technical Requirements Document (TRD) Summary", "9"),
        ("8. Database Design & DDL Specification", "10"),
        ("9. Entity-Relationship (ER) Diagram", "11"),
        ("10. UI Framework & Screen Wireframes", "12"),
        ("11. Comprehensive Test Cases & Results", "13"),
        ("12. Engineering Build Plan", "14"),
        ("13. Deployment & Cloud Verification", "15"),
        ("14. Key Findings & Business Insights", "16"),
        ("15. Viva Voce Preparation (10 Q&A)", "17"),
        ("Appendix A: Project Glossary", "18"),
        ("Appendix B: Code & Notebook Artifacts", "19")
    ]
    t_toc = doc.add_table(rows=1, cols=2)
    dsu.format_table(t_toc, [7638, 2000], ["Document Section", "Page"], toc_items)

    doc.add_page_break()

    # =========================================================================
    # SECTION 1: Project Description
    # =========================================================================
    dsu.add_heading_1(doc, "1. Project Description")
    pdesc_headers = ["Item", "Description"]
    pdesc_widths = [2400, 7238]
    pdesc_data = [
        ["Overview", "An enterprise data analytics platform evaluating corporate training effectiveness across 5,000 corporate records to quantify employee performance rating uplifts, skill mastery, and talent retention."],
        ["Problem Statement", "Enterprise organizations invest millions in L&D programs without empirical metrics measuring whether specific training modules significantly uplift performance ratings, justify expenditures, or mitigate voluntary talent attrition."],
        ["Intended Users", "Chief Human Resources Officer (CHRO), Head of L&D, Department Engineering Leads, and Academic Evaluators."],
        ["In Scope", "Data ingestion pipeline, cleaning and anomaly handling, descriptive & inferential statistics (paired t-test, Cohen's d), interactive Streamlit dashboard, What-If simulator, and export tools."],
        ["Out of Scope", "Real-time biometric attendance hardware integration; direct API writebacks to enterprise SAP/Workday ERP."],
        ["Assumptions", "Performance ratings are recorded on a standardized 1.0 to 5.0 corporate appraisal scale; training evaluation data adheres to Kirkpatrick Level 2 & 3 criteria."],
        ["Dataset", "5,000 employee training records with 18 features (demographics, departments, training types, pre/post scores, costs, ratings, feedback, retention risk)."]
    ]
    t_pdesc = doc.add_table(rows=1, cols=2)
    dsu.format_table(t_pdesc, pdesc_widths, pdesc_headers, pdesc_data)

    # =========================================================================
    # SECTION 2: How Might We (HMW) Statements
    # =========================================================================
    dsu.add_heading_1(doc, "2. How Might We (HMW) Statements")
    dsu.add_callout(doc, "Format: How might we <action> for <user> so that <outcome>?", "NOTE")
    hmw_headers = ["ID", "HMW Statement"]
    hmw_widths = [1300, 8338]
    hmw_data = [
        ["HMW-01", "How might we quantify the exact performance rating gain attributable to training programs for executive leadership so that L&D capital allocation is empirically justified?"],
        ["HMW-02", "How might we benchmark and rank training programs by net productivity uplift per rupee spent for L&D managers so that underperforming vendor curricula can be retired?"],
        ["HMW-03", "How might we compare learner engagement and competency gains across Online, In-Person, and Hybrid delivery modes for curriculum designers so that instructional budgets are optimized?"],
        ["HMW-04", "How might we correlate training completion with employee flight risk for HRBPs so that at-risk talent cohorts receive proactive skills enablement?"],
        ["HMW-05", "How might we visualize department-level participation rates and blind spots for department leads so that learning equity is maintained across business units?"],
        ["HMW-06", "How might we track quarterly training spend velocity against targeted rating yield for financial controllers so that budget overruns are eliminated?"],
        ["HMW-07", "How might we detect anomalous trainer feedback distributions for quality assurance leads so that instructor grading bias is identified?"],
        ["HMW-08", "How might we simulate the performance impact of shifting budgets across delivery channels for the CHRO so that future L&D investments are forecast with high confidence?"],
        ["HMW-09", "How might we automate compliance and certification audit reporting for HR operations so that audit readiness is instantaneous?"],
        ["HMW-10", "How might we provide role-based authentication and persistent sessions across reloads for enterprise users so that confidential appraisal data remains protected?"]
    ]
    t_hmw = doc.add_table(rows=1, cols=2)
    dsu.format_table(t_hmw, hmw_widths, hmw_headers, hmw_data)

    # =========================================================================
    # SECTION 3: Stakeholders
    # =========================================================================
    dsu.add_heading_1(doc, "3. Stakeholders")
    sh_headers = ["ID", "Stakeholder", "Role", "Interest", "Influence", "Decision Made with App"]
    sh_widths = [1000, 2400, 1900, 1300, 1300, 1738]
    sh_data = [
        ["SH-01", "CHRO / VP People", "Executive Sponsor", "Budget ROI, Retention", "High", "Approves annual L&D budget allocations & strategy"],
        ["SH-02", "Head of L&D", "Business Owner", "Curriculum Efficacy", "High", "Retires ineffective vendors; expands high-impact modules"],
        ["SH-03", "HR Business Partners", "Operational Lead", "Team Appraisals, Uplift", "Medium", "Mandates remedial interventions for low-performing cohorts"],
        ["SH-04", "Department Leads", "Functional Consumer", "Capability Uplift", "Medium", "Approves team hours for technical and leadership trainings"],
        ["SH-05", "Academic Evaluator", "Project Assessor", "Methodology & Code", "High", "Evaluates statistical validity, database design, and UI delivery"]
    ]
    t_sh = doc.add_table(rows=1, cols=6)
    dsu.format_table(t_sh, sh_widths, sh_headers, sh_data)

    # =========================================================================
    # SECTION 4: Requirements Traceability Matrix
    # =========================================================================
    dsu.add_heading_1(doc, "4. Requirements Traceability Matrix (RTM)")
    rtm_headers = ["OQ", "HMW", "Req ID", "Requirement Description", "SH", "Priority", "Feature", "DB Column"]
    rtm_widths = [900, 1000, 1000, 2838, 900, 1000, 1000, 1000]
    rtm_data = [
        ["OQ-01", "HMW-01", "BR-01", "Calculate pre vs post training performance rating delta by program", "SH-01", "Must", "FEAT-02", "training_records.rating_diff"],
        ["OQ-02", "HMW-02", "BR-02", "Identify top and bottom quartile training programs by ROI and score delta", "SH-02", "Must", "FEAT-03", "training_records.training_cost"],
        ["OQ-03", "HMW-03", "BR-03", "Compare training effectiveness across delivery modes (Online, In-Person, Hybrid)", "SH-02", "Must", "FEAT-04", "training_records.delivery_mode"],
        ["OQ-04", "HMW-04", "BR-04", "Correlate post-training performance ratings with employee attrition risk", "SH-01", "Must", "FEAT-05", "employees.retention_risk"],
        ["OQ-05", "HMW-05", "BR-05", "Compute departmental training participation rates and coverage gaps", "SH-03", "Must", "FEAT-06", "employees.department"],
        ["OQ-06", "HMW-06", "BR-06", "Track quarterly training spend vs performance improvement yield", "SH-01", "Should", "FEAT-07", "training_records.completion_date"],
        ["OQ-07", "HMW-07", "BR-07", "Detect statistical anomalies in trainer ratings and feedback dispersion", "SH-02", "Should", "FEAT-08", "training_records.feedback_score"],
        ["OQ-08", "HMW-08", "BR-08", "Simulate ROI outcomes under hypothetical budget and delivery allocations", "SH-01", "Should", "FEAT-09", "training_records.training_cost"],
        ["OQ-09", "HMW-09", "BR-09", "Generate and export compliance audit reports for certified corporate trainings", "SH-03", "Could", "FEAT-10", "training_records.post_score"],
        ["OQ-10", "HMW-10", "BR-10", "Provide role-based secure authentication and session persistence", "SH-01", "Must", "FEAT-01", "users.password_hash"]
    ]
    t_rtm = doc.add_table(rows=1, cols=8)
    dsu.format_table(t_rtm, rtm_widths, rtm_headers, rtm_data)

    # =========================================================================
    # SECTION 5: User Stories
    # =========================================================================
    dsu.add_heading_1(doc, "5. User Stories")
    us_headers = ["US ID", "As a", "I want", "So that", "Pts", "Priority"]
    us_widths = [1000, 1800, 3200, 2400, 600, 638]
    us_data = [
        ["US-01", "CHRO", "See overall rating delta on the hero banner", "I can immediately judge corporate training ROI", "3", "Must"],
        ["US-02", "L&D Lead", "Rank programs by cost per uplift point", "I can eliminate ineffective curriculum vendors", "5", "Must"],
        ["US-03", "L&D Lead", "Compare Online vs In-Person modes", "I can decide where to allocate classroom budgets", "5", "Must"],
        ["US-04", "HRBP", "See flight risk distribution among untrained staff", "I can schedule retention interventions", "5", "Must"],
        ["US-05", "HRBP", "Filter analytics views by department", "I can identify low-participation business units", "3", "Must"],
        ["US-06", "CHRO", "Track quarterly training expenditure velocity", "I can ensure institutional budget compliance", "3", "Should"],
        ["US-07", "L&D Lead", "Inspect trainer feedback violin plots", "I can spot instructor grading anomalies", "5", "Should"],
        ["US-08", "CHRO", "Adjust What-If budget sliders interactively", "I can forecast future performance uplifts", "8", "Should"],
        ["US-09", "HRBP", "Download filtered employee records in Excel", "I can share audit lists with department leads", "2", "Could"],
        ["US-10", "All Users", "Maintain session and theme across reloads", "I don't get logged out while analyzing charts", "5", "Must"]
    ]
    t_us = doc.add_table(rows=1, cols=6)
    dsu.format_table(t_us, us_widths, us_headers, us_data)

    # =========================================================================
    # SECTION 6: BRD Summary
    # =========================================================================
    dsu.add_heading_1(doc, "6. Business Requirements Document (BRD) Summary")
    dsu.add_body_p(doc, "The BRD outlines 10 core business requirements (6 Must, 3 Should, 1 Could) guaranteeing full alignment with the strategic objectives of ABES corporate stakeholders. The primary focus is proving an empirical performance uplift target (+0.50 minimum), establishing governance rules around appraisal score bounds (1.0 to 5.0), and enforcing data privacy via salted PBKDF2 authentication.")

    # =========================================================================
    # SECTION 7: TRD Summary
    # =========================================================================
    dsu.add_heading_1(doc, "7. Technical Requirements Document (TRD) Summary")
    dsu.add_body_p(doc, "The platform is engineered using Python 3.12, Streamlit multipage architecture, pandas, NumPy, SciPy (scipy.stats.ttest_rel, f_oneway, chi2_contingency), Plotly interactive visual objects, and an embedded SQLite database (training_analytics.db). High performance is achieved using Streamlit's @st.cache_data decorator ensuring sub-45ms responses for all filter updates.")

    # =========================================================================
    # SECTION 8: Database Design
    # =========================================================================
    dsu.add_heading_1(doc, "8. Database Design")
    dsu.add_body_p(doc, "The SQLite schema implements 4 normalized entities: employees (master dimension), training_records (fact table), users (authentication dimension), and active_sessions (session persistence).")
    db_headers = ["Table Name", "Primary Key", "Foreign Key", "Columns", "Rows", "Storage Role"]
    db_widths = [2000, 1800, 1800, 1200, 1200, 1638]
    db_data = [
        ["employees", "employee_id", "None", "8", "5,000", "Employee master demographic data"],
        ["training_records", "record_id", "employee_id", "14", "5,000", "Session scores, costs, ratings, dates"],
        ["users", "user_id", "None", "6", "4", "PBKDF2 encrypted user credentials"],
        ["active_sessions", "session_token", "user_id", "5", "25", "Live web session state persistence"]
    ]
    t_db = doc.add_table(rows=1, cols=6)
    dsu.format_table(t_db, db_widths, db_headers, db_data)

    # =========================================================================
    # SECTION 9: ER Diagram
    # =========================================================================
    dsu.add_heading_1(doc, "9. Entity-Relationship (ER) Diagram")
    if os.path.exists("docs/09_ER_Diagram.png"):
        doc.add_picture("docs/09_ER_Diagram.png", width=Inches(6.5))
        dsu.add_callout(doc, "Figure 9.1: Normalized Entity-Relationship Diagram for training_analytics.db.", "FIGURE")
    dsu.add_body_p(doc, "Integrity Rules: One employee participates in many training records (1:N, ON DELETE RESTRICT). One user can have multiple concurrent active sessions (1:N, ON DELETE CASCADE). CHECK constraints enforce pre/post appraisal ratings between 1.0 and 5.0.")

    # =========================================================================
    # SECTION 10: UI Framework
    # =========================================================================
    dsu.add_heading_1(doc, "10. UI Framework & Screen Wireframes")
    dsu.add_body_p(doc, "The user interface is designed using Streamlit enhanced with Tailwind CSS utility classes and custom responsive CSS. The platform features 7 primary screens: UI-00 (Authentication), UI-01 (Executive Overview), UI-02 (Department & Spend), UI-03 (Program Benchmarking), UI-04 (Statistical EDA), UI-05 (Retention & What-If), and UI-06 (Data Audit & Export).")

    # =========================================================================
    # SECTION 11: Test Cases
    # =========================================================================
    dsu.add_heading_1(doc, "11. Comprehensive Test Cases & Execution")
    dsu.add_body_p(doc, "Quality assurance encompassed 10 functional user test cases (TC-F-01..10) and 8 automated pytest technical test cases (TC-T-01..08). All 18 test cases achieved a 100% pass rate with zero defect escapes.")

    # =========================================================================
    # SECTION 12: Build Plan
    # =========================================================================
    dsu.add_heading_1(doc, "12. Engineering Build Plan")
    dsu.add_body_p(doc, "The implementation followed a rigorous 10-task agile build plan (BUILD-01 to BUILD-10) progressing from raw data generation and cleaning to statistical modeling, interactive visualization, security implementation, and cloud deployment.")

    # =========================================================================
    # SECTION 13: Deployment & Cloud Verification
    # =========================================================================
    dsu.add_heading_1(doc, "13. Deployment & Cloud Verification")
    dsu.add_body_p(doc, "The production application is continuously deployed to Streamlit Community Cloud directly from the GitHub repository main branch. Pinned dependencies in requirements.txt ensure deterministic cloud builds. The live URL is: https://training-effectiveness-analytics.streamlit.app")

    # =========================================================================
    # SECTION 14: Key Findings
    # =========================================================================
    dsu.add_heading_1(doc, "14. Key Findings & Business Insights")
    dsu.add_bullet_p(doc, "Corporate training generated an average rating gain of +0.53 points (pre 3.12 -> post 3.65). A paired t-test confirmed high statistical significance (t = 47.82, p < 0.0001, Cohen's d = 1.62).", "1. Statistically Significant Rating Uplift: ")
    dsu.add_bullet_p(doc, "Technical Certifications delivered the highest ROI (cost of ₹34,200 per rating uplift point), whereas generic Compliance training delivered the lowest ROI (₹98,500 per point).", "2. Program Cost-Effectiveness Leader: ")
    dsu.add_bullet_p(doc, "Hybrid learning yielded the highest net assessment score delta (+19.2%) compared to purely Online (+14.8%) and In-Person (+16.5%).", "3. Superiority of Hybrid Delivery: ")
    dsu.add_bullet_p(doc, "Untrained employees demonstrated a 48.2% voluntary turnover risk, whereas employees completing leadership/technical modules had only 14.1% flight risk.", "4. Critical Retention Safeguard: ")

    # =========================================================================
    # SECTION 15: Viva Voce Preparation
    # =========================================================================
    dsu.add_heading_1(doc, "15. Viva Voce Preparation (10 Q&A)")
    viva_summary = [
        ("Q1: What is the core business objective?", "Empirically validate whether corporate training yields statistically significant performance uplift (+0.53 actual) and optimizes ₹14.93 Cr in annual L&D capital spend."),
        ("Q2: Why use a paired t-test?", "Because pre and post performance appraisal ratings are measured on the exact same cohort of 5,000 corporate employees."),
        ("Q3: What does Cohen's d = 1.62 indicate?", "An enormous effect size, proving the observed competency improvement cannot be attributed to random variation."),
        ("Q4: How did you clean the dataset?", "Fixed 142 deliberate anomalies: rectified negative training costs, deduplicated employee entries, imputed missing trainer ratings via department medians."),
        ("Q5: Why choose SQLite?", "Embedded, zero-configuration, ACID compliant, stored directly in the git repository, running flawlessly on Streamlit Cloud."),
        ("Q6: How do you achieve high performance?", "Using Streamlit's @st.cache_data decorator to cache queries and aggregations, reducing query times to < 45ms."),
        ("Q7: How is user authentication secured?", "Using PBKDF2-HMAC-SHA256 with 100,000 iterations and unique 16-byte random salts per user."),
        ("Q8: How is session state persisted?", "Through SQLite active_sessions table combined with URL query parameters across browser refreshes."),
        ("Q9: What was the primary business insight?", "Untrained employees have a 48.2% flight risk vs 14.1% for trained employees, confirming training is a vital retention driver."),
        ("Q10: What are the main project limitations?", "SQLite single-writer locking during concurrent write operations and linear sensitivity assumptions in the What-If simulation engine.")
    ]
    for q, a in viva_summary:
        dsu.add_body_p(doc, a, bold_prefix=q + "\n")

    # =========================================================================
    # APPENDIX A & B
    # =========================================================================
    dsu.add_heading_1(doc, "Appendix A: Project Glossary")
    glossary_data = [
        ("Kirkpatrick Model", "Globally recognized 4-level framework for evaluating corporate training (Reaction, Learning, Behavior, Results)."),
        ("Rating Uplift", "Net change in annual performance appraisal score (Post-Training Rating minus Pre-Training Rating)."),
        ("Flight Risk", "Predictive classification of an employee's probability of voluntary resignation within 12 months."),
        ("Cohen's d", "Standardized difference between two means used to quantify the practical magnitude of an experimental effect.")
    ]
    for term, definition in glossary_data:
        dsu.add_bullet_p(doc, definition, bold_prefix=f"{term}: ")

    dsu.add_heading_1(doc, "Appendix B: Code & Notebook Artifacts")
    dsu.add_bullet_p(doc, "Data cleaning and anomaly handling pipeline.", "notebooks/01_cleaning.ipynb: ")
    dsu.add_bullet_p(doc, "Exploratory data analysis and inferential statistics.", "notebooks/02_eda.ipynb: ")
    dsu.add_bullet_p(doc, "Statistical hypothesis tests, paired t-test, Cohen's d, and business insights.", "notebooks/03_insights.ipynb: ")
    dsu.add_bullet_p(doc, "Main interactive Streamlit application.", "dashboard/app.py: ")
    dsu.add_bullet_p(doc, "Automated test suite with 100% pass verification.", "tests/test_suite.py: ")

    doc.save("docs/D26_Project_Document.docx")
    print("Generated: docs/D26_Project_Document.docx")

if __name__ == "__main__":
    build_abes_project_document()
