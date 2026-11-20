"""
Dataset Generator for Project D26: Training Effectiveness Data Analysis
Institution: ABES Engineering College | MCA 2nd Year
Domain: Human Resources (EdTech, HCLTech template)
Generates 5,000 synthetic rows with realistic Indian context, built-in trends,
correlations, a unique behavioural segment, and deliberate data-quality anomalies.
"""

import os
import random
import numpy as np
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Set random seeds for exact reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)
fake = Faker('en_IN')
Faker.seed(RANDOM_SEED)

def generate_training_effectiveness_dataset(num_records=5000):
    print(f"Generating {num_records} employee records for Training Effectiveness Analysis...")

    # Reference lists
    departments = [
        "Engineering", "Data Science & AI", "Sales & Marketing", 
        "Human Resources", "Finance", "Operations", "Customer Success"
    ]
    
    roles_by_dept = {
        "Engineering": ["Software Engineer", "Senior Software Engineer", "DevOps Engineer", "QA Engineer", "Engineering Manager"],
        "Data Science & AI": ["Data Analyst", "Data Scientist", "ML Engineer", "BI Specialist", "Data Architect"],
        "Sales & Marketing": ["Sales Executive", "Account Manager", "Digital Marketing Specialist", "Sales Lead", "Product Marketer"],
        "Human Resources": ["HR Associate", "Talent Acquisition Specialist", "HR Business Partner", "L&D Specialist"],
        "Finance": ["Financial Analyst", "Accounts Specialist", "Risk Analyst", "Finance Manager"],
        "Operations": ["Operations Associate", "Process Lead", "Supply Chain Analyst", "Operations Manager"],
        "Customer Success": ["Support Engineer", "Customer Success Specialist", "Technical Support Lead"]
    }

    locations = [
        ("Bengaluru", "Karnataka"),
        ("Pune", "Maharashtra"),
        ("Hyderabad", "Telangana"),
        ("Gurugram", "Haryana"),
        ("Noida", "Uttar Pradesh"),
        ("Mumbai", "Maharashtra"),
        ("Chennai", "Tamil Nadu"),
        ("Kolkata", "West Bengal"),
        ("Ahmedabad", "Gujarat"),
        ("Jaipur", "Rajasthan")
    ]

    training_programs = [
        ("Full-Stack Cloud & DevOps", "Technical", 48, 45000),
        ("Advanced Data Analytics & Power BI", "Technical", 40, 38000),
        ("Generative AI & LLM Applications", "Technical", 45, 52000),
        ("Strategic Leadership & Agile Management", "Leadership", 36, 42000),
        ("Enterprise Consultative Selling", "Domain", 32, 28000),
        ("Financial Modeling & Risk Management", "Domain", 30, 30000),
        ("Business Communication & Negotiation", "Soft Skills", 20, 18000),
        ("Design Thinking & Innovation", "Soft Skills", 24, 22000),
        ("Corporate Governance & POSH Compliance", "Compliance", 16, 12000)
    ]

    # Pre-generate 120 manager IDs
    manager_ids = [f"MGR-{1000 + i}" for i in range(1, 121)]

    records = []
    
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_range_days = (end_date - start_date).days

    for i in range(1, num_records + 1):
        emp_id = f"EMP-{1000 + i}"
        
        # Gender & Name
        gender = np.random.choice(["Male", "Female", "Other"], p=[0.56, 0.42, 0.02])
        if gender == "Male":
            name = fake.first_name_male() + " " + fake.last_name()
        elif gender == "Female":
            name = fake.first_name_female() + " " + fake.last_name()
        else:
            name = fake.first_name() + " " + fake.last_name()
            
        # Department & Role
        dept = np.random.choice(departments, p=[0.28, 0.16, 0.18, 0.10, 0.10, 0.10, 0.08])
        job_role = np.random.choice(roles_by_dept[dept])
        
        # Location
        city_tuple = locations[np.random.choice(len(locations), p=[0.24, 0.16, 0.16, 0.12, 0.10, 0.08, 0.06, 0.03, 0.03, 0.02])]
        city, state = city_tuple[0], city_tuple[1]
        
        # Join Date with seasonal pattern (Diwali / fiscal year start peak)
        random_days = np.random.randint(0, date_range_days)
        join_dt = start_date + timedelta(days=random_days)
        join_date_str = join_dt.strftime("%Y-%m-%d")

        # Base Experience (1 to 15 years)
        experience_years = np.round(np.random.gamma(shape=3.0, scale=1.5), 1)
        experience_years = min(max(experience_years, 0.5), 18.0)

        # Baseline Salary (INR 4.5 LPA to 32 LPA based on role and experience)
        base_salary = 450000 + (experience_years * 140000) + np.random.normal(0, 75000)
        if dept in ["Engineering", "Data Science & AI"]:
            base_salary *= 1.25
        elif dept == "Leadership":
            base_salary *= 1.4
        salary = int(np.round(base_salary, -3))
        
        # Pre-training Performance Rating (Normal distribution around 2.8 - 3.2 on 1-5 scale)
        pre_training_rating = float(np.clip(np.random.normal(3.05, 0.65), 1.0, 5.0))
        pre_training_rating = round(pre_training_rating, 1)

        # Training Program Assignment
        prog_info = random.choice(training_programs)
        prog_name, prog_type, nominal_hours, nominal_cost = prog_info
        
        # Training Participation Level (Some attend extra, some drop out or do minimal)
        # 78% participate actively, 22% low/minimal participation
        is_active_trainee = np.random.choice([True, False], p=[0.80, 0.20])
        
        if is_active_trainee:
            training_hours = float(np.clip(np.random.normal(nominal_hours, 6.0), 12.0, 75.0))
            training_score = float(np.clip(np.random.normal(78.0, 10.0), 45.0, 100.0))
        else:
            training_hours = float(np.clip(np.random.normal(6.0, 4.0), 0.0, 15.0))
            training_score = float(np.clip(np.random.normal(48.0, 14.0), 20.0, 68.0))
            
        training_hours = round(training_hours, 1)
        training_score = round(training_score, 1)

        # Training & HR Cost (in INR)
        hr_cost = int(nominal_cost * (training_hours / max(nominal_hours, 1)) + np.random.normal(3000, 500))
        hr_cost = max(hr_cost, 4500)

        # BUILT-IN RELATIONSHIP 1 & CORRELATION 1:
        # Performance Uplift strongly tied to training hours and training score
        # Rating uplift ranges from -0.2 (stagnant/poor) to +1.8
        score_factor = (training_score - 50.0) / 40.0 # -0.5 to 1.25
        hours_factor = (training_hours - 15.0) / 30.0 # -0.5 to 1.5
        rating_uplift = (0.35 * hours_factor) + (0.45 * score_factor) + np.random.normal(0.15, 0.25)
        
        # Cap uplift realistically
        rating_uplift = float(np.clip(rating_uplift, -0.4, 1.8))
        post_training_rating = float(np.clip(pre_training_rating + rating_uplift, 1.0, 5.0))
        post_training_rating = round(post_training_rating, 1)
        performance_rating = post_training_rating

        # Attendance & Late arrivals (Built-in relationship 3)
        # High training engagement leads to better discipline (higher attendance, lower late arrivals)
        base_attendance = int(np.clip(np.random.normal(210, 12) + (training_hours * 0.35), 160, 248))
        base_late = int(np.clip(np.random.normal(12, 4) - (training_hours * 0.15) + np.random.normal(0, 1.5), 0, 32))
        attendance_days = base_attendance
        late_arrivals = base_late

        # Manager ID
        manager_id = np.random.choice(manager_ids)

        # BUILT-IN RELATIONSHIP 2 & THE SPECIAL ANOMALOUS SEGMENT:
        # Normal relationship: Training & High Performance reduces attrition
        base_attrition_prob = 0.22 - (training_hours * 0.0035) - ((performance_rating - 3.0) * 0.04)
        base_attrition_prob = np.clip(base_attrition_prob, 0.04, 0.45)
        
        # SPECIAL SEGMENT ("Trained Talent Flight" Anomaly):
        # High performers with >45 hours training and rating >= 4.0 who have below-average salary for their experience
        # face HIGH attrition (poached by competitors because company trained them up but underpays them)
        is_special_segment = False
        if training_hours >= 40.0 and performance_rating >= 4.0:
            expected_sal = 450000 + (experience_years * 150000)
            if salary < expected_sal:
                is_special_segment = True
                base_attrition_prob = 0.48 # Elevated attrition due to poaching

        attrition_event = np.random.choice([1, 0], p=[base_attrition_prob, 1.0 - base_attrition_prob])
        attrition_flag = "Yes" if attrition_event == 1 else "No"

        # Exit date for employees who attrited
        if attrition_flag == "Yes":
            # Exit occurs 90 to 300 days after join date, within 2024-2025
            exit_offset = np.random.randint(90, 450)
            exit_dt = join_dt + timedelta(days=exit_offset)
            if exit_dt > end_date:
                exit_dt = end_date - timedelta(days=np.random.randint(1, 45))
            exit_date_str = exit_dt.strftime("%Y-%m-%d")
        else:
            exit_date_str = None

        record = {
            "employee_id": emp_id,
            "employee_name": name,
            "department": dept,
            "job_role": job_role,
            "gender": gender,
            "city": city,
            "state": state,
            "join_date": join_date_str,
            "exit_date": exit_date_str,
            "experience_years": experience_years,
            "salary": salary,
            "pre_training_rating": pre_training_rating,
            "training_program_name": prog_name,
            "training_type": prog_type,
            "training_hours": training_hours,
            "training_score": training_score,
            "performance_rating": performance_rating,
            "attendance_days": attendance_days,
            "late_arrivals": late_arrivals,
            "manager_id": manager_id,
            "hr_cost": hr_cost,
            "attrition_flag": attrition_flag
        }
        records.append(record)

    df = pd.DataFrame(records)

    # -------------------------------------------------------------
    # INTENTIONAL DATA-QUALITY ISSUES FOR CLEANING SPRINT:
    # -------------------------------------------------------------
    print("Introducing intentional data-quality problems for Sprint 1 data cleaning...")
    
    # 1. 3% to 5% Missing values in 3 columns: salary (4%), training_hours (3.8%), late_arrivals (4.2%)
    missing_salary_idx = np.random.choice(df.index, size=int(0.040 * num_records), replace=False)
    df.loc[missing_salary_idx, "salary"] = np.nan

    missing_thours_idx = np.random.choice(df.index, size=int(0.038 * num_records), replace=False)
    df.loc[missing_thours_idx, "training_hours"] = np.nan

    missing_late_idx = np.random.choice(df.index, size=int(0.042 * num_records), replace=False)
    df.loc[missing_late_idx, "late_arrivals"] = np.nan

    # 2. Inconsistent text casing and spelling in 'department'
    inconsistent_indices = np.random.choice(df.index, size=250, replace=False)
    for idx in inconsistent_indices:
        val = df.loc[idx, "department"]
        variant = np.random.choice([
            val.lower(),
            val.upper(),
            val.replace("Engineering", "IT / Tech"),
            val.replace("Human Resources", "HR"),
            val.replace("Sales & Marketing", "sales"),
            val.replace("Data Science & AI", "data science")
        ])
        df.loc[idx, "department"] = variant

    # 3. Exactly 2 invalid dates
    invalid_date_idx_1 = 142
    invalid_date_idx_2 = 2895
    df.loc[invalid_date_idx_1, "join_date"] = "2025-02-31"  # Invalid day in Feb
    df.loc[invalid_date_idx_2, "join_date"] = "2024-13-45"  # Non-existent month 13, day 45

    # 4. Outliers in salary and training_hours
    outlier_salary_1 = 312
    outlier_salary_2 = 1845
    df.loc[outlier_salary_1, "salary"] = 99999999  # Extreme ₹9.99 Crore outlier
    df.loc[outlier_salary_2, "salary"] = -45000    # Negative salary outlier

    outlier_hours_1 = 780
    outlier_hours_2 = 2410
    df.loc[outlier_hours_1, "training_hours"] = 999.0  # Absurdly high training hours
    df.loc[outlier_hours_2, "training_hours"] = -15.0  # Negative training hours

    # 5. ~1% duplicate rows (50 duplicate rows appended)
    dup_indices = np.random.choice(df.index, size=50, replace=False)
    duplicates = df.loc[dup_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # Save to data/raw/
    os.makedirs("data/raw", exist_ok=True)
    raw_path = os.path.join("data", "raw", "training_effectiveness_data_analysis.csv")
    df.to_csv(raw_path, index=False)
    print(f"\nDataset successfully generated and saved to: {raw_path}")
    print(f"Total rows (with duplicates): {len(df)}")
    
    print("\n--- df.info() ---")
    df.info()

    print("\n--- df.describe() ---")
    print(df.describe())

    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())

    return df

if __name__ == "__main__":
    generate_training_effectiveness_dataset(5000)
