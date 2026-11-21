# Training Effectiveness Data Analysis (P073)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![SQLite](https://img.shields.io/badge/SQLite-Relational_DB-003B57?logo=sqlite&logoColor=white)](https://sqlite.org)
[![Security: PBKDF2](https://img.shields.io/badge/Security-PBKDF2--SHA256-4CAF50?logo=security&logoColor=white)](https://en.wikipedia.org/wiki/PBKDF2)
[![Academic Project](https://img.shields.io/badge/ABES%20EC-MCA%202nd%20Year-orange)](https://abes.ac.in)
[![Curriculum](https://img.shields.io/badge/HCLTech-EdTech%20Track-0078D4)](https://hcltech.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade, dynamic Human Resources analytics platform and decision intelligence workspace built with **Python, SQLite, Pandas, Plotly, SciPy, and Streamlit**. It quantifies the return on investment (ROI) of employee learning and development, proves performance rating improvements through statistical hypothesis testing, examines punctuality and attendance impacts, and exposes critical retention vulnerabilities such as the **"Trained Talent Flight"** poaching anomaly.

The application features full end-to-end operational capabilities: **PBKDF2-SHA256 authentication**, role-based data isolation, department authorization keys, live employee onboarding, training completion logging, retention salary interventions, and immutable audit logs backed by a normalized SQLite database.

---

## Project Metadata

| Field | Project Details |
|:---|:---|
| **Project Code** | **P073** |
| **Project Title** | **Training Effectiveness Data Analysis** |
| **Institution** | **ABES Engineering College \| MCA 2nd Year** |
| **Programme / Batch** | **ABES_OND26_MCA 2nd Year_Data Analytics_Batch 01** |
| **Learner** | **Shreyansh \| Roll No: 2500320140140** |
| **Mentor** | **Dinesh Sereno** |
| **Track** | **Data Analyst** |
| **Curriculum Partner** | **Program Manager, EdTech, HCLTech** |
| **Domain** | **Human Resources (HR) & Talent Analytics** |
| **Primary Users** | **HR Manager, Head of L&D, Chief Human Resources Officer (CHRO), Department Leads** |
| **GitHub Repository** | `https://github.com/Shreyansh713/Training-Effectiveness-Analytics.git` |
| **Live App (Streamlit)** | [Live Dashboard Application](https://training-effectiveness-analytics-jyzbvf3sktjk9wqhcrpddz.streamlit.app/) |
| **Release Version** | `v1.0.0` (Sprint 3 Complete) |

---

## Security & Access Control

- **PBKDF2-SHA256 Password Security:** Passwords hashed with unique random 16-byte salts and 200,000 hashing rounds.
- **Department Authorization Keys:** Self-registration is gated by organization keys, preventing unauthorized access.
- **Account Lockout:** 5 consecutive failed password attempts triggers an automatic 5-minute security lockout.
- **Role-Based Data Scoping (RBAC):**
  - **CHRO (Admin):** Full enterprise-wide access, What-If simulator, retention authorizer, audit log.
  - **HR Manager:** Global employee onboarding, flight risk intervention, cohort analytics.
  - **L&D Specialist:** Training management, logging hours and test scores, program ROI metrics.
  - **Department Lead:** Automatically scoped to view only their department's personnel and performance data.
- **Immutable Audit Trail:** Every login, onboarding event, training log, and compensation adjustment is permanently recorded in SQLite.

---

## Demo Credentials & Authorization Keys

| Role | Username | Password | Scope | Permissions |
|:---|:---|:---|:---|:---|
| **CHRO (Admin)** | `chro_admin` | `Admin@2026` | Global Enterprise | Full Access, What-If Simulator, Retention, Audit Log |
| **HR Manager** | `hr_manager` | `HrManager@2026` | Global Enterprise | Onboarding, Flight Risk Mitigation, Analytics, Exports |
| **L&D Specialist** | `lnd_lead` | `Lnd@2026` | Learning Programs | Log Training Hours, Update Test Scores, Program ROI |
| **Engineering Lead** | `eng_lead` | `EngLead@2026` | Engineering Dept | Department Scoped Analytics & Attendance |
| **Sales Lead** | `sales_lead` | `SalesLead@2026` | Sales & Marketing | Department Scoped Analytics & Attrition |

### Department Authorization Keys for Self-Registration

| Role Target | Authorization Key |
|:---|:---|
| **CHRO (Admin)** | `CHRO-EXEC-2026` |
| **HR Manager** | `HR-TEAM-2026` |
| **L&D Specialist** | `LND-PORTAL-2026` |
| **Department Lead** | `DEPT-LEAD-2026` |

---

## Executive Scorecard & Key Findings

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             ENTERPRISE L&D SCORECARD                             │
├────────────────────────────────┬─────────────────┬──────────────┬────────────────┤
│ Strategic Metric               │ Untrained Cohort│ Trained Cohort│ Impact / Delta │
├────────────────────────────────┼─────────────────┼──────────────┼────────────────┤
│ Mean Performance Rating        │ 3.09 / 5.0      │ 3.90 / 5.0   │ +0.81 Rating ▲ │
│ Annual Late Clock-ins          │ 12.8 Times      │ 4.6 Times    │ -64.1% Drops ▼ │
│ Annual Attendance Days         │ 208 Days        │ 224 Days     │ +16 Days Gain ▲│
│ Voluntary Attrition Rate       │ 24.6%           │ 8.4%         │ -16.2% Retained│
│ Enterprise Training ROI        │ —               │ 199.8%       │ ₹ 29.8 Cr Value│
└────────────────────────────────┴─────────────────┴──────────────┴────────────────┘
```

> **The "Trained Talent Flight" Anomaly:** High performers who logged $>40$ hours of training and earned $\ge 4.0$ ratings experienced an alarming **48.2% attrition rate** if their compensation fell below market benchmark. Training without concurrent compensation benchmarking converts your training budget into a competitor recruitment subsidy.

---

## Interactive Dashboard Architecture (10 Workspace Tabs)

| Tab | Capability & Interactive Operations |
|:---|:---|
| **1. Executive Overview** | High-level KPI cards with deltas, pre vs. post rating migration histograms, training tier donut breakdown, and monthly onboarding trends. |
| **2. Departments & Roles** | Performance rating gain ranked across 7 departments, pre/post comparative bar charts, and a styled benchmark data table. |
| **3. Training Program ROI** | Cost vs. rating uplift bubble chart (bubble size = headcount), assessment scores vs. rating gains with OLS regression, cost-per-uplift-point metrics. |
| **4. Attendance & Discipline** | Box plots of late arrivals by training tier, attendance days by performance category, and scatter plot proving negative correlation ($r = -0.41$). |
| **5. Retention & Flight Risk** | Cohort attrition breakdown, deep-dive into the "Trained Talent Flight" anomaly, and compensation gap analysis. |
| **6. What-If ROI Simulator** | Interactive sliders adjusting training hours, participation rate, and retention adjustment budget to forecast projected rating uplift, attrition drop, and financial ROI in real time. |
| **7. Employee 360 & Operations Desk** | **Searchable scorecards**, plus live dynamic workflows: **Log Training Completion** (L&D), **Authorize Retention Intervention** (HR/CHRO), and **Onboard New Employee** (HR). Updates SQLite live! |
| **8. Statistical Lab** | Live Welch's two-sample t-test ($t = 47.82, p < 0.0001, d = 1.62$), interactive Pearson correlation heatmap, and hypothesis validation. |
| **9. Audit Trail & Governance** | Live SQLite audit log of every sign-in, onboarding, training completion, and retention intervention with timestamps, username, and role. |
| **10. Reports & Data Export** | Interactive table of filtered records, one-click CSV data export, and executive action recommendations. |

---

## Database Schema (Normalised SQLite Relational Model)

```
employees (employee_id PK, employee_name, department, job_role, gender,
           city, state, join_date, exit_date, experience_years, salary,
           manager_id, attrition_flag)

training_records (record_id PK, employee_id FK, training_program_name,
                  training_type, pre_training_rating, training_hours,
                  training_score, performance_rating, attendance_days,
                  late_arrivals, hr_cost, rating_improvement,
                  rating_uplift_pct, training_tier, performance_category,
                  cost_per_training_hour, is_flight_risk, completion_date)

users (username PK, full_name, email, role, department, password_hash,
       salt, failed_attempts, locked_until, last_login, created_at)

audit_log (id PK, timestamp, username, role, action, detail)

interventions (id PK, employee_id FK, employee_name, department, action_type,
               salary_adjustment_pct, new_salary, details, requested_by,
               status, timestamp)
```

---

## Repository Structure

```
.
├── .streamlit/
│   └── config.toml                  # Streamlit dark/light theme & server configuration
├── data/
│   ├── raw/
│   │   └── training_effectiveness_data_analysis.csv  # 5,050 raw rows with deliberate anomalies
│   └── clean/
│       └── training_effectiveness_cleaned.csv        # 5,000 cleaned, feature-engineered records
├── notebooks/
│   ├── 01_cleaning.ipynb            # Deduplication, invalid date fixes, casing, outlier imputation
│   ├── 02_eda.ipynb                 # Univariate/bivariate analysis, department trends, correlation heatmap
│   └── 03_insights.ipynb            # Welch's t-test, Cohen's d, hypothesis testing, ROI financial model
├── dashboard/
│   ├── app.py                       # Full-featured Streamlit interactive portal with RBAC & Auth
│   └── db.py                        # SQLite engine, PBKDF2 hashing, live CRUD workflows & audit trail
├── reports/
│   ├── insight_report.md            # Comprehensive corporate HR analytics and findings report
│   └── presentation.md              # Executive presentation slide deck for CHRO / Board
├── docs/                            # Markdown project docs and engineering deliverables
│   ├── data_dictionary.md           # Full field specifications, data types, and value bounds
│   ├── business_questions.md        # 10 core business questions & KPI formulas
│   ├── sprint_reviews.md            # Sprint 1 (v0.1.0), Sprint 2 (v0.2.0), Sprint 3 (v1.0.0) notes
│   └── ...                          # 18-step engineering documentation files (.docx, .xlsx, .pptx)
├── Documents/                       # Academic 18-Step Deliverables Suite (Word, Excel, PowerPoint)
│   ├── 01_Project_Understanding.docx
│   ├── 02_HMW_Statements.docx
│   ├── 03_Needs_Analysis.docx
│   ├── 04_Traceability_Matrix.xlsx
│   ├── 05_BRD.docx
│   ├── 06_PRD.docx
│   ├── 07_TRD.docx
│   ├── 08_Database_Design.xlsx
│   ├── 09_ER_Diagram.docx / .png
│   ├── 10_Data_Dictionary.docx
│   ├── 11_User_Stories.docx
│   ├── 12_UI_Framework.docx
│   ├── 13_Test_Cases.docx
│   ├── 14_BUILD_PLAN.docx
│   ├── 15_Application_Build_Integration.docx
│   ├── 16_Cloud_Deployment_Guide.docx
│   ├── D26_Project_Document.docx
│   ├── D26_Presentation.pptx
│   └── Epics_User_Stories_Deliverables.xlsx
├── scripts/
│   ├── generate_data.py             # Realistic synthetic data generator with Indian context (seed 42)
│   ├── clean_data.py                # Standalone data cleaning and feature engineering pipeline
│   ├── build_notebooks.py           # Programmatic notebook builder
│   └── execute_notebooks.py         # Automated notebook execution engine
├── app.py                           # Root application entry point
├── training_analytics.db            # Persistent normalized SQLite relational database
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Git ignore configuration
└── README.md                        # Master repository documentation
```

---

## Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/rahul/mca2-da-training-effectiveness-data-analysis.git
cd Data_Analytics_Project
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Dynamic Streamlit Portal
```bash
streamlit run app.py
```
*The portal opens in your browser at `http://localhost:8501`. Sign in with `chro_admin` / `Admin@2026` or create a new account using any authorization key listed above.*

---

## Author & Academic Acknowledgements

- **Student Developer:** MCA 2nd Year, ABES Engineering College
- **Skill Track:** Data Analyst Practice
- **Curriculum & Mentorship:** Program Manager, EdTech, HCLTech
- **Reference Inspiration:** Bank Transaction Pattern Analysis Framework

---

## License
This project is open-source and released under the [MIT License](LICENSE).
