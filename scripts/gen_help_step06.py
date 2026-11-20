import sys, os
sys.path.insert(0, os.path.abspath('.'))
import docx
from docx.shared import Inches, Pt, RGBColor
import scripts.doc_style_utils as dsu

os.makedirs('help', exist_ok=True)

doc = docx.Document()
dsu.setup_page(doc, learner="Shreyansh", roll_no="2500320140140", project_id="D26", title="Step 6 - Product Requirements Document")

# ══════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "Product Requirements Document (PRD)")
dsu.add_body_p(doc, "Project D26 — Training Effectiveness Data Analysis | Streamlit Data Analytics App")
dsu.add_callout(doc, "This PRD translates the BRD (Step 5) business requirements into concrete product features, user flows, non-functional requirements, and a sprint delivery roadmap. Written from the perspective of a senior Product Manager.", "PRODUCT MANAGEMENT")

# ══════════════════════════════════════════════════════════════
# 1. PRODUCT OVERVIEW & TARGET PERSONAS
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "1. Product Overview & Target Personas")

dsu.add_heading_2(doc, "1a. Product Overview")
dsu.add_body_p(doc, "TalentMetrics is an interactive, role-based Streamlit web analytics platform that empowers HR leadership to evaluate corporate training effectiveness using 5,000 employee training records. The platform provides descriptive KPIs, inferential statistical tests, comparative benchmarking, What-If budget simulation, and automated report generation — all accessible through an intuitive multi-tab dashboard with Plotly visualisations and Tailwind-styled UI components.")

dsu.add_heading_2(doc, "1b. Target Personas")

persona_headers = ["Persona", "Name & Profile", "Primary Goals", "Usage Frequency", "Key Screens"]
persona_widths = [1200, 2200, 2800, 1200, 2238]
persona_data = [
    ["Primary:\nExecutive CHRO", "Vikram Malhotra, 48\nVP People at a 5,000-employee enterprise", "• Justify ₹14.9 Cr L&D budget to the Board\n• Identify flight risk in untrained cohorts\n• Forecast What-If budget scenarios", "Quarterly / Monthly", "UI-01 (Overview)\nUI-05 (Simulator)"],
    ["Secondary:\nL&D Program Lead", "Pooja Sharma, 34\nHead of Corporate Learning & Development", "• Benchmark programs by cost per uplift\n• Compare Online vs In-Person vs Hybrid\n• Spot trainer feedback anomalies", "Bi-weekly", "UI-03 (Benchmark)\nUI-04 (EDA)\nUI-02 (Dept)"],
    ["Operational:\nHR Business Partner", "Rahul Verma, 29\nHRBP assigned to Engineering division", "• Monitor department participation rates\n• Identify low-performers for remediation\n• Export filtered compliance reports", "Weekly", "UI-02 (Dept)\nUI-06 (Export)"],
    ["Academic:\nProject Evaluator", "Dr. Anjali Pandey\nABES IT Department Mentor", "• Assess statistical rigour & methodology\n• Verify traceability & test coverage\n• Evaluate code quality & DB design", "One-time (review)", "All screens\n+ documentation"]
]
t_persona = doc.add_table(rows=1, cols=5)
dsu.format_table(t_persona, persona_widths, persona_headers, persona_data)

# ══════════════════════════════════════════════════════════════
# 2. MVP FEATURES TABLE
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "2. MVP Features Matrix")
dsu.add_callout(doc, "8–12 features covering: data loading/cleaning, KPIs, trends, comparisons, statistical EDA, insights, data quality, and CSV/Excel download. Every Must BR maps to ≥ 1 Feature.", "COVERAGE REQUIREMENT")

feat_headers = ["Feature ID", "Feature Name", "Description", "Linked BR", "Linked OQ", "Priority", "Target Screen"]
feat_widths = [900, 1600, 2638, 1000, 900, 800, 1800]
feat_data = [
    ["FEAT-01", "Secure Authentication & Session", "PBKDF2-SHA256 role-based login with 4 demo roles (CHRO, HR Manager, L&D Specialist, Eng Lead) and one-click demo access. Session token persisted in SQLite across browser reloads.", "BR-12, BR-13", "OQ-10", "Must", "UI-00 (Auth Portal)"],
    ["FEAT-02", "Executive KPI Banner", "Hero cards displaying Total Learners, Net Rating Uplift (+0.53), Participation Rate (75.1%), and Total Training Spend (₹14.93 Cr). Cards update dynamically with sidebar filters.", "BR-01, BR-14", "OQ-01", "Must", "UI-01 (Overview)"],
    ["FEAT-03", "Program ROI Benchmarking", "Comparative scatter and grouped bar charts ranking training types and programs by cost-per-uplift-point. Sortable leaderboard with top/bottom quartile flags.", "BR-02", "OQ-02", "Must", "UI-03 (Benchmark)"],
    ["FEAT-04", "Delivery Mode Analytics", "Side-by-side box/violin plots comparing score delta and feedback scores across Online, In-Person, and Hybrid delivery channels. Validated with one-way ANOVA.", "BR-03", "OQ-03", "Must", "UI-02 (Dept & Trends)"],
    ["FEAT-05", "Retention & Flight Risk Hub", "Cross-tabulation heatmap of post-training ratings × retention risk levels. Chi-square test of independence between training status and flight risk category.", "BR-04, BR-09", "OQ-04, OQ-09", "Must", "UI-05 (Retention & Sim)"],
    ["FEAT-06", "Department Coverage Matrix", "Grouped bar chart of departmental participation rates with headcount denominators. Departments below 60% threshold auto-flagged with warning badges.", "BR-05", "OQ-05", "Must", "UI-02 (Dept & Trends)"],
    ["FEAT-07", "Quarterly Spend Trends", "Interactive area chart showing quarterly training expenditure (₹) overlaid with average rating uplift per quarter. Trend direction indicators (▲/▼) for each metric.", "BR-06", "OQ-06", "Should", "UI-02 (Dept & Trends)"],
    ["FEAT-08", "Trainer Feedback Distribution", "Violin/box plot of instructor feedback scores with per-trainer drill-down. Descriptive stats panel (mean, SD, skewness) and outlier detection (±2 SD flags).", "BR-07", "OQ-07", "Should", "UI-04 (Statistical EDA)"],
    ["FEAT-09", "What-If Budget Simulator", "Interactive sliders to model hypothetical budget reallocations across departments and delivery channels. Outputs projected rating uplift with confidence bands and ±5% sensitivity.", "BR-08", "OQ-08", "Should", "UI-05 (Retention & Sim)"],
    ["FEAT-10", "Data Export & Audit Log", "Filtered CSV/Excel download of employee training records. Auto-generated executive summary memo with key KPIs, timestamp, filter criteria, and row count logged.", "BR-10", "OQ-09", "Could", "UI-06 (Data & Export)"],
    ["FEAT-11", "Statistical Hypothesis Panel", "Dedicated panel displaying paired t-test results (t-statistic, p-value, CI), Cohen's d effect size, and ANOVA output. Methodology notes for academic evaluator.", "BR-01, BR-14", "OQ-01", "Must", "UI-04 (Statistical EDA)"],
    ["FEAT-12", "Data Cleaning & Quality Dashboard", "Summary of cleaning pipeline: nulls fixed, duplicates removed, outliers capped, range violations corrected. Before/after comparison statistics.", "BR-14", "OQ-01..10", "Should", "UI-06 (Data & Export)"]
]
t_feat = doc.add_table(rows=1, cols=7)
dsu.format_table(t_feat, feat_widths, feat_headers, feat_data)

# ══════════════════════════════════════════════════════════════
# 3. FEATURE SPECIFICATIONS (Must/Should)
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "3. Feature Specifications")
dsu.add_callout(doc, "Detailed specification for each Must and Should feature: user flow, inputs/filters, calculations/logic, visual output, and empty-filter handling.", "FEATURE SPECS")

# --- FEAT-01 ---
dsu.add_heading_2(doc, "FEAT-01: Secure Authentication & Session (Must)")
spec_headers = ["Aspect", "Specification"]
spec_widths = [2200, 7438]

feat01_spec = [
    ["User Flow", "1. User lands on auth portal (UI-00) → 2. Enters username/password OR clicks a demo role button → 3. System validates PBKDF2 hash → 4. Session token stored in SQLite + URL query param → 5. Redirected to main dashboard."],
    ["Inputs / Filters", "Username (text), Password (password field), Demo Role buttons (CHRO, HR Manager, L&D Specialist, Eng Lead)."],
    ["Calculations / Logic", "hashlib.pbkdf2_hmac('sha256', password, salt, 100000) compared against stored hash. Session token = secrets.token_hex(32). Token persisted in active_sessions table."],
    ["Visual Output", "Branded hero card with TalentMetrics logo, login form, and 4 coloured demo role cards. Light/Dark theme applied from session state."],
    ["Empty-Filter Handling", "Invalid credentials → inline error message 'Invalid username or password.' No redirect. Demo buttons always succeed."]
]
t_f01 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f01, spec_widths, spec_headers, feat01_spec)

# --- FEAT-02 ---
dsu.add_heading_2(doc, "FEAT-02: Executive KPI Banner (Must)")
feat02_spec = [
    ["User Flow", "1. Authenticated user enters Overview tab → 2. KPI cards render with global data → 3. User applies sidebar filters → 4. Cards recalculate for filtered subset."],
    ["Inputs / Filters", "Department (multiselect), Training Type (multiselect), Delivery Mode (multiselect), Date Range (date picker)."],
    ["Calculations / Logic", "Total Learners = COUNT(DISTINCT employee_id). Rating Uplift = AVG(post_rating − pre_rating). Participation = trained/total × 100. Spend = SUM(training_cost)."],
    ["Visual Output", "4 hero KPI cards in a horizontal row: each with large numeric value, label, and positive/negative delta badge (green ▲ / red ▼)."],
    ["Empty-Filter Handling", "If filters return 0 rows → cards display '—' with grey text 'No data matches current filters.' Charts show empty state placeholder."]
]
t_f02 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f02, spec_widths, spec_headers, feat02_spec)

# --- FEAT-03 ---
dsu.add_heading_2(doc, "FEAT-03: Program ROI Benchmarking (Must)")
feat03_spec = [
    ["User Flow", "1. Navigate to Benchmark tab → 2. View default scatter plot (cost vs uplift) → 3. Click table header to sort by ROI → 4. Apply training type filter."],
    ["Inputs / Filters", "Training Type (dropdown), Delivery Mode (dropdown), Minimum sample size slider (10–500)."],
    ["Calculations / Logic", "Cost per uplift = SUM(training_cost) / SUM(rating_diff) grouped by program. Top quartile: programs in top 25% by ROI. Bottom quartile: programs in bottom 25%."],
    ["Visual Output", "Plotly scatter plot (x: avg cost, y: avg uplift, size: participant count, colour: training type). Below: sortable leaderboard table with rank, program, cost/point, quartile flag."],
    ["Empty-Filter Handling", "Filters yielding < 3 programs → message 'Too few programs for meaningful comparison. Broaden your filters.' Scatter plot hidden."]
]
t_f03 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f03, spec_widths, spec_headers, feat03_spec)

# --- FEAT-04 ---
dsu.add_heading_2(doc, "FEAT-04: Delivery Mode Analytics (Must)")
feat04_spec = [
    ["User Flow", "1. Navigate to Dept & Trends tab → 2. Scroll to delivery mode section → 3. Toggle between box plot and violin plot → 4. ANOVA result card displayed below."],
    ["Inputs / Filters", "Department (multiselect), Date range (slider), Chart type toggle (Box / Violin)."],
    ["Calculations / Logic", "Score delta grouped by delivery_mode. ANOVA: scipy.stats.f_oneway(online_deltas, inperson_deltas, hybrid_deltas). Report F-statistic, p-value, and post-hoc interpretation."],
    ["Visual Output", "Side-by-side box/violin plots (x: delivery mode, y: score delta). ANOVA summary card: F-stat, p-value, significance badge (✓ Significant / ✗ Not Significant)."],
    ["Empty-Filter Handling", "If any delivery mode has < 5 records → warning 'Insufficient data for [mode]. ANOVA may be unreliable.' Test still runs with caveat."]
]
t_f04 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f04, spec_widths, spec_headers, feat04_spec)

# --- FEAT-05 ---
dsu.add_heading_2(doc, "FEAT-05: Retention & Flight Risk Hub (Must)")
feat05_spec = [
    ["User Flow", "1. Navigate to Retention & Sim tab → 2. View heatmap of ratings × risk levels → 3. Chi-square result card renders → 4. Click on cell for drill-down list."],
    ["Inputs / Filters", "Department (multiselect), Training Status (Trained / Untrained / All), Risk Level (Low / Medium / High / All)."],
    ["Calculations / Logic", "Contingency table: training_status × retention_risk. Chi-square: scipy.stats.chi2_contingency(). Proportions: % high-risk in trained vs untrained groups."],
    ["Visual Output", "Plotly heatmap (x: training status, y: risk level, colour: count). Chi-square summary card: χ², p-value, Cramér's V. Below: filtered employee list with risk badges."],
    ["Empty-Filter Handling", "Zero records for a risk/status combination → cell shows 0 with grey styling. Chi-square still computes on available data."]
]
t_f05 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f05, spec_widths, spec_headers, feat05_spec)

# --- FEAT-06 ---
dsu.add_heading_2(doc, "FEAT-06: Department Coverage Matrix (Must)")
feat06_spec = [
    ["User Flow", "1. Navigate to Dept & Trends tab → 2. View grouped bar chart of participation by department → 3. Departments below 60% show warning badge."],
    ["Inputs / Filters", "Location (multiselect), Job Role (multiselect), Minimum headcount threshold."],
    ["Calculations / Logic", "Participation rate = COUNT(DISTINCT trained_employees) / COUNT(DISTINCT all_employees) × 100, grouped by department. Threshold flag: rate < 60% → 'Gap'."],
    ["Visual Output", "Grouped bar chart (x: department, y: participation %, colour: above/below threshold). Data table with headcount, trained count, rate, and status badge."],
    ["Empty-Filter Handling", "Department with 0 employees after filter → excluded from chart with note 'N departments excluded due to filter constraints.'"]
]
t_f06 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f06, spec_widths, spec_headers, feat06_spec)

# --- FEAT-07 ---
dsu.add_heading_2(doc, "FEAT-07: Quarterly Spend Trends (Should)")
feat07_spec = [
    ["User Flow", "1. On Dept & Trends tab → 2. Scroll to spend timeline section → 3. View area chart with spend and uplift overlay."],
    ["Inputs / Filters", "Department (multiselect), Training Type (multiselect)."],
    ["Calculations / Logic", "GROUP BY QUARTER(completion_date). Spend = SUM(training_cost). Uplift = AVG(rating_diff). Trend = current quarter vs previous quarter direction."],
    ["Visual Output", "Dual-axis Plotly area chart: left y-axis = spend (₹), right y-axis = avg uplift. Trend arrows (▲/▼) for each quarter."],
    ["Empty-Filter Handling", "Quarter with no records → gap in chart line with tooltip 'No training completed in Q[x].'"]
]
t_f07 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f07, spec_widths, spec_headers, feat07_spec)

# --- FEAT-08 ---
dsu.add_heading_2(doc, "FEAT-08: Trainer Feedback Distribution (Should)")
feat08_spec = [
    ["User Flow", "1. Navigate to Statistical EDA tab → 2. View overall feedback distribution → 3. Select specific trainer for drill-down → 4. Outlier flags appear."],
    ["Inputs / Filters", "Trainer/Program (dropdown), Training Type (multiselect)."],
    ["Calculations / Logic", "Per-trainer: mean, median, SD, skewness of feedback_score. Outlier = any trainer whose mean is > 2 SD from the global mean."],
    ["Visual Output", "Violin plot of feedback distribution. Stats panel: mean, SD, skewness values. Outlier trainers highlighted in red."],
    ["Empty-Filter Handling", "Trainer with < 10 ratings → note 'Insufficient sample for reliable distribution analysis.'"]
]
t_f08 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f08, spec_widths, spec_headers, feat08_spec)

# --- FEAT-09 ---
dsu.add_heading_2(doc, "FEAT-09: What-If Budget Simulator (Should)")
feat09_spec = [
    ["User Flow", "1. Navigate to Retention & Sim tab → 2. Adjust budget allocation sliders → 3. Projected uplift recalculates in real-time → 4. Compare baseline vs simulated scenario."],
    ["Inputs / Filters", "Budget reallocation sliders (% per department or delivery mode), Total budget constraint (₹)."],
    ["Calculations / Logic", "Linear sensitivity model: projected_uplift = baseline_uplift × (1 + budget_change_% × elasticity_coefficient). Elasticity estimated from historical data. Bounded within ±30%."],
    ["Visual Output", "Side-by-side comparison: baseline KPIs vs simulated KPIs. Projected uplift with ±5% confidence band. Bar chart of department-level impact."],
    ["Empty-Filter Handling", "Budget slider at 0% for all → 'Please allocate budget to at least one category.' Simulation disabled."]
]
t_f09 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f09, spec_widths, spec_headers, feat09_spec)

# --- FEAT-11 ---
dsu.add_heading_2(doc, "FEAT-11: Statistical Hypothesis Panel (Must)")
feat11_spec = [
    ["User Flow", "1. Navigate to Statistical EDA tab → 2. View pre-configured paired t-test results → 3. Toggle to ANOVA / Chi-square panels → 4. Read methodology notes."],
    ["Inputs / Filters", "Test type selector (Paired t-test / ANOVA / Chi-square), Department filter, Confidence level (90/95/99%)."],
    ["Calculations / Logic", "Paired t-test: scipy.stats.ttest_rel(pre, post). Cohen's d = mean_diff / pooled_sd. ANOVA: scipy.stats.f_oneway(). Chi-square: scipy.stats.chi2_contingency()."],
    ["Visual Output", "Statistical summary cards: t-stat, p-value, CI, Cohen's d with effect size interpretation. KDE overlay of pre vs post distributions. Methodology note panel."],
    ["Empty-Filter Handling", "Filtered sample < 30 → warning 'Sample size too small for reliable inference. Results shown with caveat.'"]
]
t_f11 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f11, spec_widths, spec_headers, feat11_spec)

# --- FEAT-12 ---
dsu.add_heading_2(doc, "FEAT-12: Data Cleaning & Quality Dashboard (Should)")
feat12_spec = [
    ["User Flow", "1. Navigate to Data & Export tab → 2. View cleaning pipeline summary → 3. Before/after statistics comparison → 4. Download cleaned dataset."],
    ["Inputs / Filters", "None (read-only summary view)."],
    ["Calculations / Logic", "Pre-clean: COUNT nulls, COUNT duplicates, COUNT out-of-range. Post-clean: all zeroes. Delta: issues fixed per category."],
    ["Visual Output", "Before/After comparison cards (nulls, duplicates, outliers). Data quality score badge (100% if zero remaining issues)."],
    ["Empty-Filter Handling", "N/A — this view always displays full pipeline summary regardless of sidebar filters."]
]
t_f12 = doc.add_table(rows=1, cols=2)
dsu.format_table(t_f12, spec_widths, spec_headers, feat12_spec)

# ══════════════════════════════════════════════════════════════
# 4. NON-FUNCTIONAL REQUIREMENTS
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "4. Non-Functional Requirements (NFRs)")

nfr_headers = ["NFR ID", "Category", "Requirement Description", "Target Metric"]
nfr_widths = [900, 1600, 4938, 2200]
nfr_data = [
    ["NFR-01", "Performance", "Dashboard page initial rendering and filter reaction time must be fast enough for interactive exploration.", "< 3.0 seconds initial load; < 500ms filter reaction"],
    ["NFR-02", "Data Accuracy", "All statistical calculations must produce results identical to SciPy reference implementations within floating-point precision.", "Results match scipy output to 4 decimal places"],
    ["NFR-03", "Reliability", "Data integrity across SQLite queries with zero unhandled null values or query failures during normal operation.", "100% query success rate; zero runtime exceptions"],
    ["NFR-04", "Security", "User passwords must be protected using industry-standard key derivation with sufficient computational cost to resist brute-force attacks.", "PBKDF2-HMAC-SHA256, 100,000 iterations, 16-byte random salt"],
    ["NFR-05", "Usability", "Dashboard must render correctly in both Light and Dark themes with no text clipping, overflow, or contrast accessibility issues.", "Zero CSS clipping issues; WCAG AA contrast on all text"],
    ["NFR-06", "Responsiveness", "Layout must adapt gracefully to screen widths from 1024px (laptop) to 1920px (desktop) without horizontal scrolling.", "No horizontal scroll on 1024px+ viewport"],
    ["NFR-07", "Portability", "Application must run identically on Windows, macOS, and Linux, and deploy without modification to Streamlit Community Cloud.", "Python 3.10 – 3.13 compatibility; zero OS-specific code"],
    ["NFR-08", "Maintainability", "Codebase must be modular with clear separation between data layer (db.py), business logic, and presentation (app.py).", "≤ 3 primary source files; functions < 50 lines each"]
]
t_nfr = doc.add_table(rows=1, cols=4)
dsu.format_table(t_nfr, nfr_widths, nfr_headers, nfr_data)

# ══════════════════════════════════════════════════════════════
# 5. OUT OF SCOPE FOR v1.0
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "5. Out of Scope for v1.0 (Deferred Features)")

deferred_headers = ["Deferred Feature", "Reason for Deferral", "Target Version"]
deferred_widths = [3200, 4200, 2238]
deferred_data = [
    ["ML Predictive Models (Random Forest, XGBoost)", "Requires model training infrastructure and validation framework beyond current semester scope.", "v2.0"],
    ["Real-time ERP API Integration (Workday, SAP)", "Requires enterprise API credentials and OAuth flows not available for academic projects.", "v2.0"],
    ["Multi-tenant SaaS with Per-Org DB Isolation", "Requires PostgreSQL/cloud DB infrastructure and tenant management; beyond single-user analytics scope.", "v3.0"],
    ["Native Mobile App (iOS / Android)", "Flutter/React Native development requires separate skill set and app store deployment.", "v3.0"],
    ["Email/Slack Alert Notifications", "Requires webhook integration and notification service; not critical for dashboard analytics.", "v2.0"],
    ["Advanced NLP on Feedback Comments", "Free-text sentiment analysis requires NLP pipeline (spaCy/transformers); no text data in current schema.", "v2.0"]
]
t_defer = doc.add_table(rows=1, cols=3)
dsu.format_table(t_defer, deferred_widths, deferred_headers, deferred_data)

# ══════════════════════════════════════════════════════════════
# 6. RELEASE & SPRINT ROADMAP
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "6. Release & Sprint Roadmap")

sprint_headers = ["Sprint", "Duration", "Theme", "Key Deliverables", "Features Delivered", "Exit Criteria"]
sprint_widths = [900, 1200, 1800, 2400, 1600, 1738]
sprint_data = [
    ["Sprint 1", "Week 1–2", "Data Layer & Cleaning",
     "• SQLite schema creation (DDL)\n• Synthetic data generation (5,000 rows)\n• Data cleaning pipeline\n• Raw → Clean CSV validation",
     "FEAT-12 (partial)", "Zero nulls in clean data; FK integrity check passes; 5,000 rows validated"],

    ["Sprint 2", "Week 3–4", "Analytics, Statistics & KPIs",
     "• Paired t-test, ANOVA, Chi-square\n• KPI calculation modules\n• Plotly chart components\n• Initial dashboard views",
     "FEAT-02, FEAT-03, FEAT-04, FEAT-06, FEAT-07, FEAT-08, FEAT-11",
     "All statistical tests produce valid output; KPI cards render correctly; charts interactive"],

    ["Sprint 3", "Week 5–6", "Integration, Security, Testing & Deploy",
     "• PBKDF2 auth + session persistence\n• What-If simulator integration\n• Full pytest suite (18 tests)\n• Streamlit Cloud deployment\n• Documentation suite generation",
     "FEAT-01, FEAT-05, FEAT-09, FEAT-10, FEAT-12 (complete)",
     "18/18 tests pass; live URL accessible; all docs generated; login persists across reload"]
]
t_sprint = doc.add_table(rows=1, cols=6)
dsu.format_table(t_sprint, sprint_widths, sprint_headers, sprint_data)

# ══════════════════════════════════════════════════════════════
# BR → FEATURE COVERAGE VERIFICATION
# ══════════════════════════════════════════════════════════════
dsu.add_heading_1(doc, "7. BR → Feature Coverage Verification")
dsu.add_callout(doc, "Every Must-priority BR must map to ≥ 1 Feature. This table confirms full coverage.", "COVERAGE CHECK")

cov_headers = ["BR ID", "Priority", "Mapped Feature(s)", "Coverage"]
cov_widths = [1200, 1200, 4000, 3238]
cov_data = [
    ["BR-01", "Must", "FEAT-02, FEAT-11", "✓ Covered"],
    ["BR-02", "Must", "FEAT-03", "✓ Covered"],
    ["BR-03", "Must", "FEAT-04", "✓ Covered"],
    ["BR-04", "Must", "FEAT-05", "✓ Covered"],
    ["BR-05", "Must", "FEAT-06", "✓ Covered"],
    ["BR-06", "Should", "FEAT-07", "✓ Covered"],
    ["BR-07", "Should", "FEAT-08", "✓ Covered"],
    ["BR-08", "Should", "FEAT-09", "✓ Covered"],
    ["BR-09", "Must", "FEAT-05", "✓ Covered"],
    ["BR-10", "Could", "FEAT-10", "✓ Covered"],
    ["BR-11", "Should", "FEAT-03, FEAT-11", "✓ Covered"],
    ["BR-12", "Must", "FEAT-01", "✓ Covered"],
    ["BR-13", "Must", "FEAT-01", "✓ Covered"],
    ["BR-14", "Must", "FEAT-02..12 (all views)", "✓ Covered"]
]
t_cov = doc.add_table(rows=1, cols=4)
dsu.format_table(t_cov, cov_widths, cov_headers, cov_data)

dsu.add_callout(doc, "Result: 14/14 BRs covered. All 9 Must-priority BRs map to ≥ 1 Feature. Zero gaps. The RTM (Step 4) has been updated with the Feature ID column.", "VERIFICATION PASSED ✓")

doc.save("help/06_Shreyansh_PRD.docx")
print("SUCCESS: Generated help/06_Shreyansh_PRD.docx")
