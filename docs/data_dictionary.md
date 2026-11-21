# Data Dictionary: Training Effectiveness Data Analysis (P073)

**Project Code:** P073  
**Domain:** Human Resources  
**Dataset Name:** `training_effectiveness_data_analysis.csv` (Raw) / `training_effectiveness_cleaned.csv` (Cleaned)  
**Target Audience:** HR Manager, Chief Human Resources Officer (CHRO), Learning & Development (L&D) Leads  

---

## 1. Column Specifications

| Column Name | Raw Data Type | Cleaned Data Type | Description | Allowed Values / Range | Example Value |
|:---|:---|:---|:---|:---|:---|
| `employee_id` | String | String (PK) | Unique employee identifier code | `EMP-[1001-6000]` | `EMP-1042` |
| `employee_name` | String | String | Full name of employee (Indian context) | Text (Alpha + space) | `Aarav Sharma` |
| `department` | String | Categorical | Business unit / functional department | `Engineering`, `Data Science & AI`, `Sales & Marketing`, `Human Resources`, `Finance`, `Operations`, `Customer Success` | `Engineering` |
| `job_role` | String | Categorical | Specific organizational designation | Standard job roles mapped to department | `Senior Software Engineer` |
| `gender` | String | Categorical | Reported gender identity | `Male`, `Female`, `Other` | `Female` |
| `city` | String | Categorical | Operational work location city (India) | `Bengaluru`, `Pune`, `Hyderabad`, `Gurugram`, `Noida`, `Mumbai`, `Chennai`, `Kolkata`, `Ahmedabad`, `Jaipur` | `Bengaluru` |
| `state` | String | Categorical | Operational work location state | Indian States | `Karnataka` |
| `join_date` | String | Date (YYYY-MM-DD) | Date the employee joined the company | `2024-01-01` to `2025-12-31` | `2024-03-15` |
| `exit_date` | String | Date (YYYY-MM-DD) | Date of resignation/exit (Null if active) | `2024-01-01` to `2025-12-31` or `NaN` | `2025-08-20` |
| `experience_years` | Float | Float | Total years of relevant professional experience | `0.5` to `18.0` | `4.5` |
| `salary` | Float | Integer | Annual gross remuneration in INR (₹) | ₹ 4,50,000 to ₹ 35,00,000 | ₹ 12,50,000 |
| `pre_training_rating`| Float | Float | Performance score before training cycle | `1.0` to `5.0` (1-decimal) | `3.1` |
| `training_program_name`| String | Categorical | Title of training program attended | 9 L&D programs across technical, leadership, domain, soft skills | `Full-Stack Cloud & DevOps` |
| `training_type` | String | Categorical | Classification of the training program | `Technical`, `Leadership`, `Domain`, `Soft Skills`, `Compliance` | `Technical` |
| `training_hours` | Float | Float | Total cumulative hours logged in training | `0.0` to `75.0` hrs | `42.5` |
| `training_score` | Float | Float | Assessment score achieved upon training completion | `0.0` to `100.0` | `84.5` |
| `performance_rating` | Float | Float | Post-training annual performance rating | `1.0` to `5.0` (1-decimal) | `4.2` |
| `attendance_days` | Integer | Integer | Total annual working days attended | `160` to `248` days | `224` |
| `late_arrivals` | Float | Integer | Number of recorded late clock-ins in the year | `0` to `30` | `4` |
| `manager_id` | String | String | Direct supervisor's identifier | `MGR-[1001-1120]` | `MGR-1015` |
| `hr_cost` | Integer | Integer | Total L&D and onboarding expenditure per employee (INR ₹) | ₹ 4,500 to ₹ 75,000 | ₹ 38,500 |
| `attrition_flag` | String | Binary Flag | Status whether employee has left the company | `Yes`, `No` | `No` |

---

## 2. Derived & Engineered Feature Columns

During the data cleaning and feature engineering phase, the following metrics are created:

1. `rating_improvement`: `performance_rating - pre_training_rating` (measures absolute performance uplift).
2. `rating_uplift_pct`: `(rating_improvement / pre_training_rating) * 100` (percentage performance gain).
3. `training_tier`: Grouped training participation (`Minimal (<15h)`, `Moderate (15-35h)`, `High (>35h)`).
4. `cost_per_training_hour`: `hr_cost / training_hours` (cost efficiency index).
5. `tenure_months`: Calculated from `join_date` to `exit_date` or observation cutoff (Dec 31, 2025).
6. `is_flight_risk`: Indicator flag for high-skilled, undercompensated employees prone to competitor poaching.
7. `performance_category`: Categorized rating (`Needs Improvement [1-2.4]`, `Meets Expectations [2.5-3.4]`, `Exceeds Expectations [3.5-4.4]`, `Outstanding [4.5-5.0]`).
