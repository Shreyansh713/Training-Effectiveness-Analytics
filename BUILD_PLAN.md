# BUILD PLAN & VIVA VOCE GUIDE (D26)
**Project Title:** Training Effectiveness Data Analysis  
**Institution:** ABES Engineering College, Ghaziabad  
**Learner:** Shreyansh (Roll No: 2300320140045) | **Mentor:** Dr. R. K. Sharma  
**Repository:** https://github.com/Shreyansh713/Training-Effectiveness-Analytics  
**Live App:** https://training-effectiveness-analytics.streamlit.app  

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
