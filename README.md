# Training Effectiveness Data Analysis (D26)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![SciPy](https://img.shields.io/badge/SciPy-Statistics-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org)
[![Academic Project](https://img.shields.io/badge/ABES%20EC-MCA%202nd%20Year-orange)](https://abes.ac.in)
[![Curriculum](https://img.shields.io/badge/HCLTech-EdTech%20Track-0078D4)](https://hcltech.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade Human Resources analytics platform and interactive decision workspace built with **Python, Pandas, Plotly, SciPy, and Streamlit**. It quantifies the return on investment (ROI) of employee learning and development, proves performance rating improvements through statistical hypothesis testing, examines punctuality and attendance impacts, and exposes critical retention vulnerabilities such as the **"Trained Talent Flight"** poaching anomaly.

---

## Project Metadata

| Field | Project Details |
|:---|:---|
| **Project Code** | **D26** |
| **Project Title** | **Training Effectiveness Data Analysis** |
| **Institution** | **ABES Engineering College \| MCA 2nd Year** |
| **Track** | **Data Analyst** |
| **Curriculum Partner** | **Program Manager, EdTech, HCLTech** |
| **Domain** | **Human Resources (HR) & Talent Analytics** |
| **Primary Users** | **HR Manager, Head of L&D, Chief Human Resources Officer (CHRO)** |
| **Repository Name** | `mca2-da-training-effectiveness-data-analysis` |
| **Release Version** | `v1.0.0` (Sprint 3 Complete) |

---

## Executive Summary & Why This Project

In enterprise technology corporations, Learning & Development (L&D) budgets represent massive capital investments—over **₹ 14.92 Crores across 5,000 employees** in this study. Executive leadership demands data-backed answers to fundamental talent questions:

- **Performance Gain:** Does participation in technical and leadership training yield measurable, statistically verified performance improvements?
- **Behavioral Discipline:** Does structured training instill workplace punctuality, reducing late arrivals and attendance leakage?
- **Retention vs. Poaching:** Does upskilling employees improve talent retention, or does it trigger competitor poaching if compensation is unaligned?
- **Financial Justification:** What is the tangible monetary ROI per rupee spent on training programs?

This repository provides an end-to-end, reproducible data analytics solution: from synthetic data generation with realistic Indian context, deliberate data-cleaning pipelines, exploratory and hypothesis-testing Jupyter notebooks, up to a real-time **Streamlit Executive Dashboard with a What-If Scenario Simulator**.

---

## Key Findings at a Glance

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

## Interactive Dashboard Architecture (9 Tabs)

The application (`dashboard/app.py` or root `app.py`) provides an executive cockpit:

| Tab | Capability & Visualizations |
|:---|:---|
| **1. Executive Overview** | High-level KPI cards with deltas, pre vs. post rating migration histograms, training tier donut breakdown, and monthly onboarding trends. |
| **2. Departments & Roles** | Performance rating gain ranked across 7 departments, pre/post comparative bar charts, and a styled benchmark data table. |
| **3. Training Program ROI** | Cost vs. rating uplift bubble chart (bubble size = headcount), assessment scores vs. rating gains with OLS regression, cost-per-uplift-point metrics. |
| **4. Attendance & Discipline** | Box plots of late arrivals by training tier, attendance days by performance category, and scatter plot proving negative correlation ($r = -0.41$). |
| **5. Retention & Flight Risk** | Cohort attrition breakdown, deep-dive into the "Trained Talent Flight" anomaly, and compensation gap analysis. |
| **6. What-If ROI Simulator** | Interactive sliders adjusting training hours, participation rate, and retention adjustment budget to forecast projected rating uplift, attrition drop, and financial ROI in real time. |
| **7. Employee 360 Explorer** | Searchable employee directory, individual scorecards, pre vs. post performance delta, manager info, and automated "Flight Risk" badge. |
| **8. Statistical Lab** | Live Welch's two-sample t-test ($t = 47.82, p < 0.0001, d = 1.62$), interactive Pearson correlation heatmap, and hypothesis validation. |
| **9. Reports & Data Export** | Interactive table of filtered records, one-click CSV data export, and executive action recommendations. |

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
│   └── app.py                       # Full-featured Streamlit interactive analytics application
├── reports/
│   ├── insight_report.md            # Comprehensive corporate HR analytics and findings report
│   └── presentation.md              # Executive presentation slide deck for CHRO / Board
├── docs/
│   ├── data_dictionary.md           # Full field specifications, data types, and value bounds
│   ├── business_questions.md        # 10 core business questions & KPI formulas
│   └── sprint_reviews.md            # Sprint 1 (v0.1.0), Sprint 2 (v0.2.0), Sprint 3 (v1.0.0) notes
├── scripts/
│   ├── generate_data.py             # Realistic synthetic data generator with Indian context (seed 42)
│   ├── clean_data.py                # Standalone data cleaning and feature engineering pipeline
│   ├── build_notebooks.py           # Programmatic notebook builder
│   └── execute_notebooks.py         # Automated notebook execution engine
├── app.py                           # Root application entry point
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Git ignore configuration
└── README.md                        # Master repository documentation
```

---

## Dataset Schema & Field Descriptions

The dataset reflects realistic corporate IT and services operations across 10 major Indian technology hubs (Bengaluru, Pune, Hyderabad, Gurugram, Noida, Mumbai, Chennai, etc.):

| Column Name | Type | Description |
|:---|:---|:---|
| `employee_id` | String | Unique employee primary key (`EMP-1001` to `EMP-6000`) |
| `employee_name` | String | Employee full name (Indian context via Faker `en_IN`) |
| `department` | Categorical | Business unit (`Engineering`, `Data Science & AI`, `Sales & Marketing`, `HR`, `Finance`, `Operations`, `Customer Success`) |
| `job_role` | Categorical | Designation mapped to department |
| `gender` | Categorical | `Male`, `Female`, `Other` |
| `city` / `state` | Categorical | Work location in India |
| `join_date` / `exit_date` | Date | Date of onboarding / resignation (Null if active) |
| `salary` | Integer | Annual gross remuneration in INR (₹ 4.5L to ₹ 35L) |
| `pre_training_rating` | Float | Performance score prior to training (1.0 - 5.0) |
| `training_program_name`| Categorical | 9 specialized training programs (Technical, Leadership, Domain, Soft Skills) |
| `training_type` | Categorical | Classification (`Technical`, `Leadership`, `Domain`, `Soft Skills`, `Compliance`) |
| `training_hours` | Float | Logged cumulative training hours (0.0 - 75.0 hrs) |
| `training_score` | Float | Assessment score achieved upon training completion (0 - 100%) |
| `performance_rating` | Float | Post-training annual appraisal rating (1.0 - 5.0) |
| `attendance_days` | Integer | Annual working days attended (160 - 248 days) |
| `late_arrivals` | Integer | Annual late clock-ins (0 - 30 times) |
| `manager_id` | String | Direct supervisor identifier (`MGR-1001` to `MGR-1120`) |
| `hr_cost` | Integer | Total L&D and onboarding expenditure (₹ 4,500 - ₹ 75,000) |
| `attrition_flag` | String | Status flag (`Yes` / `No`) |
| `rating_improvement` | Float | Engineered uplift metric (`performance_rating - pre_training_rating`) |
| `training_tier` | Categorical | `Minimal (<15h)`, `Moderate (15-35h)`, `High (>35h)` |
| `is_flight_risk` | Boolean | Poaching risk indicator for undercompensated high performers |

---

## Statistical Verification (Hypothesis Testing)

### Hypothesis 1: Rating Uplift Significance
- **Null Hypothesis ($H_0$):** Training participation ($>35$ hours) yields no significant difference in performance rating compared to minimal training ($\le 15$ hours).
- **Alternative Hypothesis ($H_1$):** Trainees completing $>35$ hours achieve significantly higher ratings.
- **Test:** Welch's Two-Sample t-test (unequal variances assumed)
  - $t = 47.82$
  - $p\text{-value} = 3.14 \times 10^{-240} < 0.0001$
  - **Effect Size (Cohen's $d$):** $1.62$ (Exceptionally large positive effect)
  - **Conclusion:** Reject $H_0$. Upskilling drives statistically verified performance gains.

### Hypothesis 2: Late Clock-ins & Attendance Discipline
- **Pearson Correlation:** $r = -0.41, p < 0.0001$ between `training_hours` and `late_arrivals`.
- **Conclusion:** Employees participating in learning programs show significantly superior punctuality and work engagement.

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

### 3. Generate & Clean Data (Reproducible Pipeline)
```bash
# Generate raw synthetic data (5,050 records with anomalies)
python scripts/generate_data.py

# Execute cleaning pipeline (produces 5,000 cleaned rows)
python scripts/clean_data.py
```

### 4. Run the Interactive Streamlit Dashboard
```bash
streamlit run app.py
```
*The portal will open in your browser at `http://localhost:8501`.*

---

## Git Workflow & Sprint Milestones

The project adhered to strict Agile sprint delivery with semantic release tagging:

```
[main]          ----------------------------------------- v1.0.0 (Release)
                   \                                     /
[develop]           -- v0.1.0 (Sprint 1) -- v0.2.0 (Sprint 2)
                       \                   \
[feature/...]           -- US1.1-US1.4      -- US2.1-US2.4
```

- **Sprint 1 (`v0.1.0`):** Business questions formulation, synthetic dataset generator, data dictionary documentation, and data cleaning pipeline.
- **Sprint 2 (`v0.2.0`):** Exploratory data analysis, univariate/bivariate distributions, KPI derivations, and anomalous segment identification.
- **Sprint 3 (`v1.0.0`):** Multi-tab Streamlit dashboard, What-If ROI simulator, executive reports, slide presentation, and tagged release.

---

## Author & Academic Acknowledgements

- **Student Developer:** MCA 2nd Year, ABES Engineering College
- **Skill Track:** Data Analyst Practice
- **Curriculum & Mentorship:** Program Manager, EdTech, HCLTech
- **Reference Inspiration:** Bank Transaction Pattern Analysis Framework

---

## License
This project is open-source and released under the [MIT License](LICENSE).
