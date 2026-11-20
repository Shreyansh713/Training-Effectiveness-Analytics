# Sprint Reviews & Agile Release Notes

**Project:** D26 | Training Effectiveness Data Analysis  
**Institution:** ABES Engineering College | MCA 2nd Year  
**Prepared by:** EdTech Team / Lead Data Analyst  
**Repository:** `mca2-da-training-effectiveness-data-analysis`  

---

## Sprint 1 Review: Data Ingestion, Cleaning & Data Dictionary
**Sprint Tag:** `v0.1.0`  
**Duration:** 14 Hours  
**Focus:** Dataset Creation, Ingestion, Quality Auditing, Cleaning Pipeline & Data Dictionary  

### Stories Completed:
- **US1.1 (Data Generation & Ingestion):** Generated 5,000 synthetic records with realistic Indian context (cities, INR amounts, seasonal hiring dates, Indian names), 22 columns including pre/post training ratings, L&D metrics, attendance, and HR costs.
- **US1.2 (Data Quality Auditing):** Identified and cataloged deliberate quality anomalies:
  - 3-5% missing values in `salary` (201 rows), `training_hours` (190 rows), and `late_arrivals` (212 rows).
  - 50 duplicate rows (appended ~1%).
  - Inconsistent casing and naming conventions in `department` (e.g. `IT / Tech`, `HR`, `sales`, `SALES`, `data science`).
  - Extreme outliers: ₹ 9.99 Crore salary, ₹ -45,000 negative salary, 999.0 training hours, -15.0 training hours.
  - Exactly 2 invalid dates (`2025-02-31` and `2024-13-45`).
- **US1.3 (Data Cleaning & Imputation):** Implemented reproducible cleaning notebook (`01_cleaning.ipynb`):
  - Deduplicated rows (dropped 50 duplicates, restoring 5,000 clean records).
  - Imputed missing values using domain-aligned median by role and department.
  - Rectified string casing and mapped category codes to standard names.
  - Repaired invalid date entries and cast columns to optimal types.
  - Capped outliers using IQR and domain-valid logical bounds.
  - Saved clean dataset to `data/clean/training_effectiveness_cleaned.csv`.
- **US1.4 (Data Dictionary):** Created comprehensive data dictionary documentation in `docs/data_dictionary.md`.

---

## Sprint 2 Review: Exploratory Analysis, KPIs & Statistical Insights
**Sprint Tag:** `v0.2.0`  
**Duration:** 14 Hours  
**Focus:** Exploratory Data Analysis, KPI Derivation, Hypothesis Testing & Segment Discovery  

### Stories Completed:
- **US2.1 (Exploratory Data Analysis):** Built `02_eda.ipynb` analyzing univariate, bivariate, and multivariate distributions. Visualized distributions of salaries, training hours, and rating uplifts across departments.
- **US2.2 (KPI Derivation):** Derived 8 enterprise HR KPIs: Training Participation Rate (79.8%), Average Training Hours (33.2 hrs), Mean Rating Uplift (+0.52 points), Assessment Mastery Rate (74.2%), and Training Retention Delta (-15.4%).
- **US2.3 (Statistical Hypothesis Testing):** Built `03_insights.ipynb` testing 3 hypotheses:
  - Conducted Welch's two-sample t-test ($p < 0.001$), rejecting $H_0$ and proving statistically significant rating uplift from high training hours.
  - Computed Pearson correlation matrix confirming positive correlation between `training_hours` and `performance_rating` ($r = 0.58$) and negative correlation with `late_arrivals` ($r = -0.41$).
- **US2.4 (Anomalous Segment Identification):** Uncovered the "Trained Talent Flight" segment: employees with >40 training hours and high ratings who were undercompensated experienced 48% attrition, identifying a critical retention vulnerability for HR.

---

## Sprint 3 Review: Interactive Dashboard, Executive Reports & Release
**Sprint Tag:** `v1.0.0`  
**Duration:** 12 Hours  
**Focus:** Streamlit Multi-Tab Executive Dashboard, Executive Reports, Presentation & Final Release  

### Stories Completed:
- **US3.1 (Interactive Streamlit Dashboard):** Built comprehensive executive dashboard (`dashboard/app.py` & `app.py`) featuring:
  - Multi-tab navigation with custom dark/light theme and responsive CSS styling.
  - Interactive Plotly charts, global filters (Department, Gender, Location, Training Tier).
  - Training ROI What-If simulator for executive workforce planning.
  - Employee 360 search and individual scorecard viewer.
- **US3.2 (Comprehensive Insight Report):** Authored `reports/insight_report.md` providing in-depth analysis, findings, and strategic recommendations for HR leadership.
- **US3.3 (Executive Presentation Deck):** Formatted executive presentation in `reports/presentation.md`.
- **US3.4 (Project Delivery & Git Release):** Completed repository packaging with complete `README.md`, `.gitignore`, `requirements.txt`, clean notebooks, and tagged release `v1.0.0`.
