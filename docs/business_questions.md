# Business Questions & Analytical Framework

**Project:** D26 | Training Effectiveness Data Analysis  
**Prepared For:** HR Manager, HR Head, Head of Talent Development  
**Academic Alignment:** ABES Engineering College | MCA 2nd Year  

---

## 1. Executive Problem Statement
Corporate training and development accounts for significant human capital expenditure (₹ 14.8+ Crores across 5,000 employees). Executive leadership requires quantifiable proof of return on investment (ROI), evidence of individual performance improvements, behavioral change (attendance and punctuality), and retention impact.

---

## 2. Core Business Questions Answered

### Theme 1: Training Participation & Engagement
1. **What proportion of the workforce actively engages in structured training?**
   - What is the distribution of training hours across departments, job roles, and locations?
   - Which departments lag in participation and why?
2. **Which training categories (Technical, Leadership, Domain, Soft Skills) have the highest uptake and completion rates?**

### Theme 2: Performance Improvement & Learning Effectiveness
3. **Does training participation correlate with higher performance ratings?**
   - What is the correlation coefficient between `training_hours`, `training_score`, and `performance_rating`?
   - How does the pre-training rating compare to the post-training rating across cohorts?
4. **Is there a diminishing marginal return to training hours?**
   - At what number of training hours does performance gain plateau?
5. **Which training programs generate the highest rating improvement per rupee spent?**

### Theme 3: Behavioral Impact (Attendance & Punctuality)
6. **Does training positively influence workplace discipline?**
   - Is there a measurable decrease in `late_arrivals` and an increase in `attendance_days` among highly trained employees?
   - Are certain departments showing stronger behavioral responsiveness to training?

### Theme 4: Talent Retention & Attrition Dynamics
7. **Does training investment reduce employee turnover?**
   - What is the attrition rate among employees with <15 hours vs >35 hours of training?
8. **What is the "Trained Talent Flight" anomaly?**
   - Why do certain high-performing employees with 45+ training hours exhibit an unexpectedly elevated attrition rate (48%)?
   - How does the salary-to-skill ratio influence retention of newly upskilled employees?

### Theme 5: Financial ROI & Resource Allocation
9. **What is the total and per-employee training ROI?**
   - How can HR optimize the ₹ 29,800 average HR cost per employee to maximize workforce capability?
10. **How should HR re-allocate next year's training budget across technical vs soft skills?**

---

## 3. Key Performance Indicators (KPIs) Defined

| KPI Code | KPI Name | Mathematical Formula | Target Benchmark |
|:---|:---|:---|:---|
| **KPI-01** | Training Participation Rate | `(Employees with >15 Training Hours / Total Headcount) * 100` | >= 75.0% |
| **KPI-02** | Average Training Hours per Employee | `Sum(Training Hours) / Total Headcount` | >= 32.0 Hours |
| **KPI-03** | Mean Rating Uplift (Delta Rating) | `Mean(Post_Training_Rating - Pre_Training_Rating)` | >= +0.40 points |
| **KPI-04** | Training Assessment Mastery Rate | `(Employees with Training Score >= 75 / Total Trainees) * 100` | >= 70.0% |
| **KPI-05** | Training Retention Delta | `Attrition Rate (Trained Cohort) - Attrition Rate (Untrained Cohort)` | <= -12.0% |
| **KPI-06** | Average Cost per Training Hour | `Total HR Cost / Total Training Hours` | ₹ 800 - ₹ 1,200 |
| **KPI-07** | Punctuality Improvement Rate | `(Mean Late Arrivals [Untrained] - Mean Late Arrivals [Trained]) / Mean Late Arrivals [Untrained]` | >= 35.0% Reduction |
| **KPI-08** | L&D Efficiency Ratio (ROI Proxy) | `(Performance Value Created - Total L&D Cost) / Total L&D Cost * 100` | >= 180% |

---

## 4. Statistical Hypotheses for Testing

- **Hypothesis 1 (Performance Uplift):**
  - $H_0$: There is no significant difference in post-training performance ratings between employees completing >35 hours vs <=15 hours of training.
  - $H_1$: Employees completing >35 hours have significantly higher post-training performance ratings (Welch's Two-Sample t-test, $\alpha = 0.05$).
- **Hypothesis 2 (Punctuality):**
  - $H_0$: Training hours have no correlation with late arrivals.
  - $H_1$: Training hours have a statistically significant negative correlation with late arrivals (Pearson's $r$).
- **Hypothesis 3 (Attrition Difference):**
  - $H_0$: Attrition proportion is independent of training tier.
  - $H_1$: Attrition is significantly lower among employees in the high training tier ($\chi^2$ test of independence).
