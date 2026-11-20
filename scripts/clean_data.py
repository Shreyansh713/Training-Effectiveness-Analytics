"""
Data Cleaning and Feature Engineering Pipeline for Project D26
Institution: ABES Engineering College | MCA 2nd Year
Domain: Human Resources (Training Effectiveness Data Analysis)
Cleans anomalies, handles missing values, fixes inconsistent categories and invalid dates,
handles outliers, engineers derived KPIs, and saves clean output.
"""

import os
import re
import numpy as np
import pandas as pd

def clean_training_data(raw_path="data/raw/training_effectiveness_data_analysis.csv", 
                        clean_path="data/clean/training_effectiveness_cleaned.csv"):
    print("=" * 70)
    print("STARTING DATA CLEANING PIPELINE - SPRINT 1")
    print("=" * 70)
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found at {raw_path}")
        
    df = pd.read_csv(raw_path)
    initial_rows = len(df)
    print(f"Loaded raw dataset with {initial_rows} records and {len(df.columns)} columns.")

    # 1. Deduplication
    dups_count = df.duplicated().sum()
    print(f"\n[Step 1] Deduplication: Found {dups_count} duplicate rows.")
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"         Retained {len(df)} unique records.")

    # 2. Rectify Invalid Dates in join_date
    print("\n[Step 2] Cleaning Invalid Dates...")
    # Specifically fix known simulated invalid date strings
    df['join_date'] = df['join_date'].replace({
        '2025-02-31': '2025-02-28',
        '2024-13-45': '2024-12-15'
    })
    
    # Coerce any remaining invalid dates to datetime
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
    # If any NaT exists, fill with median join date
    if df['join_date'].isna().sum() > 0:
        median_date = df['join_date'].dropna().median()
        df['join_date'] = df['join_date'].fillna(median_date)
        
    df['exit_date'] = pd.to_datetime(df['exit_date'], errors='coerce')
    print("         Dates successfully converted to standard datetime format.")

    # 3. Standardize Inconsistent Categories (department)
    print("\n[Step 3] Standardizing Inconsistent Department Casing and Synonyms...")
    def standardize_department(val):
        if not isinstance(val, str):
            return "Engineering"
        val_clean = val.strip().lower()
        if "tech" in val_clean or "it" in val_clean or "engine" in val_clean:
            return "Engineering"
        elif "data" in val_clean or "ai" in val_clean or "science" in val_clean:
            return "Data Science & AI"
        elif "sale" in val_clean or "market" in val_clean:
            return "Sales & Marketing"
        elif "hr" in val_clean or "human" in val_clean or "people" in val_clean:
            return "Human Resources"
        elif "finan" in val_clean or "account" in val_clean:
            return "Finance"
        elif "operat" in val_clean or "process" in val_clean or "supply" in val_clean:
            return "Operations"
        elif "cust" in val_clean or "supp" in val_clean or "succ" in val_clean:
            return "Customer Success"
        return "Engineering"

    df['department'] = df['department'].apply(standardize_department)
    print(f"         Unique standardized departments: {list(df['department'].unique())}")

    # 4. Outlier Handling
    print("\n[Step 4] Handling Numeric Outliers (Salary & Training Hours)...")
    # Salary bounds: ₹ 3,00,000 to ₹ 45,00,000
    invalid_salary_mask = (df['salary'] < 300000) | (df['salary'] > 4500000)
    outlier_salary_count = invalid_salary_mask.sum()
    print(f"         Identified {outlier_salary_count} salary outliers (e.g. negative or ₹10 Cr). Setting to NaN for role-median imputation.")
    df.loc[invalid_salary_mask, 'salary'] = np.nan

    # Training hours bounds: 0 to 80 hours
    invalid_hours_mask = (df['training_hours'] < 0) | (df['training_hours'] > 80)
    outlier_hours_count = invalid_hours_mask.sum()
    print(f"         Identified {outlier_hours_count} training hours outliers (e.g. -15h or 999h). Setting to NaN for program-median imputation.")
    df.loc[invalid_hours_mask, 'training_hours'] = np.nan

    # 5. Missing Value Imputation
    print("\n[Step 5] Imputing Missing Values using Domain-Aligned Group Medians...")
    # Impute salary by job_role median, fallback to department median
    sal_by_role = df.groupby('job_role')['salary'].transform('median')
    df['salary'] = df['salary'].fillna(sal_by_role)
    sal_by_dept = df.groupby('department')['salary'].transform('median')
    df['salary'] = df['salary'].fillna(sal_by_dept).astype(int)

    # Impute training_hours by training_program_name median
    hours_by_prog = df.groupby('training_program_name')['training_hours'].transform('median')
    df['training_hours'] = df['training_hours'].fillna(hours_by_prog).round(1)

    # Impute late_arrivals by department median
    late_by_dept = df.groupby('department')['late_arrivals'].transform('median')
    df['late_arrivals'] = df['late_arrivals'].fillna(late_by_dept).round().astype(int)

    print("         Missing values after imputation:")
    missing_summary = df[['salary', 'training_hours', 'late_arrivals']].isnull().sum()
    for col, count in missing_summary.items():
        print(f"           - {col}: {count} missing")

    # 6. Feature Engineering
    print("\n[Step 6] Generating Derived Features and KPI Metrics...")
    
    # 6.1 Performance Improvement Metrics
    df['rating_improvement'] = (df['performance_rating'] - df['pre_training_rating']).round(2)
    df['rating_uplift_pct'] = ((df['rating_improvement'] / df['pre_training_rating']) * 100).round(1)
    
    # 6.2 Training Participation Tiers
    df['training_tier'] = pd.cut(
        df['training_hours'],
        bins=[-0.1, 15.0, 35.0, 100.0],
        labels=['Minimal (<15h)', 'Moderate (15-35h)', 'High (>35h)']
    )

    # 6.3 Performance Rating Classification
    df['performance_category'] = pd.cut(
        df['performance_rating'],
        bins=[0.0, 2.4, 3.4, 4.4, 5.0],
        labels=['Needs Improvement', 'Meets Expectations', 'Exceeds Expectations', 'Outstanding']
    )

    # 6.4 Cost Efficiency Index (Cost per Training Hour)
    df['cost_per_training_hour'] = (df['hr_cost'] / np.maximum(df['training_hours'], 1.0)).round(2)

    # 6.5 Employee Flight Risk Indicator (The Anomalous Segment)
    expected_salary = 450000 + (df['experience_years'] * 150000)
    df['is_flight_risk'] = (
        (df['training_hours'] >= 40.0) & 
        (df['performance_rating'] >= 4.0) & 
        (df['salary'] < expected_salary)
    )

    # 6.6 Formatted Date strings for clean CSV portability
    df['join_date'] = df['join_date'].dt.strftime('%Y-%m-%d')
    df['exit_date'] = df['exit_date'].dt.strftime('%Y-%m-%d')

    # Save to clean directory
    os.makedirs(os.path.dirname(clean_path), exist_ok=True)
    df.to_csv(clean_path, index=False)
    print(f"\n[Success] Cleaned dataset successfully saved to: {clean_path}")
    print(f"Final Cleaned Dataset Dimensions: {df.shape[0]} rows x {df.shape[1]} columns")
    print("=" * 70)

    return df

if __name__ == "__main__":
    clean_training_data()
