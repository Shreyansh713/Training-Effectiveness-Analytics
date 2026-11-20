"""
Database & Authentication Engine for D26 Training Effectiveness Analytics
SQLite normalized relational backend, PBKDF2-SHA256 password hashing,
Audit logging, Role-Based Access Control (RBAC), and Dynamic HR Operations.
"""

import os
import sqlite3
import hashlib
import secrets
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "training_analytics.db")

AUTH_KEYS = {
    "CHRO-EXEC-2026": "CHRO (Admin)",
    "HR-TEAM-2026": "HR Manager",
    "LND-PORTAL-2026": "L&D Specialist",
    "DEPT-LEAD-2026": "Department Lead"
}

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str, salt: str = None) -> tuple:
    if not salt:
        salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        200000
    )
    return key.hex(), salt

def verify_password(stored_hash: str, salt: str, password_attempt: str) -> bool:
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password_attempt.encode('utf-8'),
        salt.encode('utf-8'),
        200000
    )
    return secrets.compare_digest(key.hex(), stored_hash)

def init_database():
    """Initializes tables, creates indexes, and populates data if empty."""
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        department TEXT,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        failed_attempts INTEGER DEFAULT 0,
        locked_until TEXT,
        last_login TEXT,
        created_at TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS employees (
        employee_id TEXT PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department TEXT NOT NULL,
        job_role TEXT NOT NULL,
        gender TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        join_date TEXT NOT NULL,
        exit_date TEXT,
        experience_years REAL NOT NULL,
        salary INTEGER NOT NULL,
        manager_id TEXT NOT NULL,
        attrition_flag TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS training_records (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        training_program_name TEXT NOT NULL,
        training_type TEXT NOT NULL,
        pre_training_rating REAL NOT NULL,
        training_hours REAL NOT NULL,
        training_score REAL NOT NULL,
        performance_rating REAL NOT NULL,
        attendance_days INTEGER NOT NULL,
        late_arrivals INTEGER NOT NULL,
        hr_cost INTEGER NOT NULL,
        rating_improvement REAL NOT NULL,
        rating_uplift_pct REAL NOT NULL,
        training_tier TEXT NOT NULL,
        performance_category TEXT NOT NULL,
        cost_per_training_hour REAL NOT NULL,
        is_flight_risk INTEGER NOT NULL,
        completion_date TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    );

    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        username TEXT NOT NULL,
        role TEXT NOT NULL,
        action TEXT NOT NULL,
        detail TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS interventions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        employee_name TEXT NOT NULL,
        department TEXT NOT NULL,
        action_type TEXT NOT NULL,
        salary_adjustment_pct REAL DEFAULT 0,
        new_salary INTEGER,
        details TEXT,
        requested_by TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    );

    CREATE INDEX IF NOT EXISTS idx_emp_dept ON employees(department);
    CREATE INDEX IF NOT EXISTS idx_rec_emp ON training_records(employee_id);
    """)

    conn.commit()

    # Seed Default User Accounts if not present
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        default_users = [
            ("chro_admin", "Dr. Rajeshwar Sharma", "chro@enterprise.in", "CHRO (Admin)", "All", "Admin@2026"),
            ("hr_manager", "Pooja Deshmukh", "pooja.d@enterprise.in", "HR Manager", "Human Resources", "HrManager@2026"),
            ("lnd_lead", "Arjun Srinivasan", "arjun.s@enterprise.in", "L&D Specialist", "Human Resources", "Lnd@2026"),
            ("eng_lead", "Vikram Rathore", "vikram.r@enterprise.in", "Department Lead", "Engineering", "EngLead@2026"),
            ("sales_lead", "Neha Kulkarni", "neha.k@enterprise.in", "Department Lead", "Sales & Marketing", "SalesLead@2026")
        ]
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for u, name, email, role, dept, pwd in default_users:
            pwd_hash, salt = hash_password(pwd)
            cur.execute("""
            INSERT INTO users (username, full_name, email, role, department, password_hash, salt, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (u, name, email, role, dept, pwd_hash, salt, now_str))
        
        # Log initialization
        cur.execute("""
        INSERT INTO audit_log (timestamp, username, role, action, detail)
        VALUES (?, ?, ?, ?, ?)
        """, (now_str, "SYSTEM", "System", "INIT_USERS", "Seeded default administrative and managerial user profiles"))
        conn.commit()

    # Seed Employees and Training Records from Clean CSV if empty
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] == 0:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "clean", "training_effectiveness_cleaned.csv")
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            
            # Insert into employees
            emp_cols = ['employee_id', 'employee_name', 'department', 'job_role', 'gender', 'city', 'state', 'join_date', 'exit_date', 'experience_years', 'salary', 'manager_id', 'attrition_flag']
            df_emp = df[emp_cols].copy()
            df_emp['exit_date'] = df_emp['exit_date'].fillna('')
            df_emp.to_sql('employees', conn, if_exists='append', index=False)

            # Insert into training_records
            rec_cols = [
                'employee_id', 'training_program_name', 'training_type', 'pre_training_rating',
                'training_hours', 'training_score', 'performance_rating', 'attendance_days',
                'late_arrivals', 'hr_cost', 'rating_improvement', 'rating_uplift_pct',
                'training_tier', 'performance_category', 'cost_per_training_hour', 'is_flight_risk'
            ]
            df_rec = df[rec_cols].copy()
            df_rec['is_flight_risk'] = df_rec['is_flight_risk'].astype(int)
            df_rec['completion_date'] = df['join_date'] # baseline completion
            df_rec.to_sql('training_records', conn, if_exists='append', index=False)

            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cur.execute("""
            INSERT INTO audit_log (timestamp, username, role, action, detail)
            VALUES (?, ?, ?, ?, ?)
            """, (now_str, "SYSTEM", "System", "DATA_MIGRATION", f"Imported {len(df)} initial records into SQLite relational tables"))
            conn.commit()

    conn.close()

# -------------------------------------------------------------
# AUTHENTICATION & SESSION MANAGEMENT
# -------------------------------------------------------------
def authenticate_user(username: str, password_attempt: str) -> dict:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()

    if not user:
        conn.close()
        return {"success": False, "message": "Username not found."}

    user = dict(user)
    now = datetime.now()

    # Check lockout
    if user.get("locked_until"):
        locked_time = datetime.strptime(user["locked_until"], "%Y-%m-%d %H:%M:%S")
        if now < locked_time:
            remaining = int((locked_time - now).total_seconds() / 60) + 1
            conn.close()
            return {"success": False, "message": f"Account temporarily locked due to failed attempts. Try again in {remaining} minute(s)."}

    # Verify password
    if verify_password(user["password_hash"], user["salt"], password_attempt):
        # Reset failed attempts and update last login
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        UPDATE users 
        SET failed_attempts = 0, locked_until = NULL, last_login = ?
        WHERE username = ?
        """, (now_str, username))
        
        # Log successful sign-in
        cur.execute("""
        INSERT INTO audit_log (timestamp, username, role, action, detail)
        VALUES (?, ?, ?, ?, ?)
        """, (now_str, username, user['role'], "LOGIN_SUCCESS", "User authenticated into portal"))
        conn.commit()
        conn.close()

        return {
            "success": True,
            "user": {
                "username": user["username"],
                "full_name": user["full_name"],
                "email": user["email"],
                "role": user["role"],
                "department": user["department"]
            }
        }
    else:
        # Increment failed attempts
        failed = user["failed_attempts"] + 1
        lock_until = None
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")

        if failed >= 5:
            lock_until = (now + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
            msg = "Account locked for 5 minutes due to 5 consecutive failed attempts."
        else:
            msg = f"Invalid password. Attempt {failed} of 5."

        cur.execute("""
        UPDATE users 
        SET failed_attempts = ?, locked_until = ?
        WHERE username = ?
        """, (failed, lock_until, username))
        
        cur.execute("""
        INSERT INTO audit_log (timestamp, username, role, action, detail)
        VALUES (?, ?, ?, ?, ?)
        """, (now_str, username, user['role'], "LOGIN_FAILED", f"Invalid password attempt (Attempt {failed})"))
        conn.commit()
        conn.close()

        return {"success": False, "message": msg}

def register_user(username, full_name, email, password, auth_key, department="All"):
    # Password strength check
    if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
        return {"success": False, "message": "Password must be at least 8 characters and contain at least 1 uppercase letter and 1 number."}

    # Verify authorization key
    if auth_key not in AUTH_KEYS:
        return {"success": False, "message": "Invalid Authorization Key. Obtain a valid key from your HR Administrator."}

    role = AUTH_KEYS[auth_key]
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        conn.close()
        return {"success": False, "message": "Username already taken."}

    pwd_hash, salt = hash_password(password)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
    INSERT INTO users (username, full_name, email, role, department, password_hash, salt, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (username, full_name, email, role, department, pwd_hash, salt, now_str))

    cur.execute("""
    INSERT INTO audit_log (timestamp, username, role, action, detail)
    VALUES (?, ?, ?, ?, ?)
    """, (now_str, username, role, "USER_REGISTER", f"Self-registered with role {role}"))
    conn.commit()
    conn.close()

    return {"success": True, "message": f"Account created successfully for {full_name} ({role})! Please proceed to login."}

# -------------------------------------------------------------
# DYNAMIC DATA QUERIES & LIVE CRUD WORKFLOWS
# -------------------------------------------------------------
def get_live_analytics_data(scoped_department=None) -> pd.DataFrame:
    """Fetches joined dataset from SQLite with dynamic feature calculations."""
    conn = get_connection()
    query = """
    SELECT 
        e.employee_id, e.employee_name, e.department, e.job_role, e.gender,
        e.city, e.state, e.join_date, e.exit_date, e.experience_years, e.salary,
        e.manager_id, e.attrition_flag,
        r.training_program_name, r.training_type, r.pre_training_rating,
        r.training_hours, r.training_score, r.performance_rating,
        r.attendance_days, r.late_arrivals, r.hr_cost,
        r.rating_improvement, r.rating_uplift_pct, r.training_tier,
        r.performance_category, r.cost_per_training_hour, r.is_flight_risk
    FROM employees e
    JOIN training_records r ON e.employee_id = r.employee_id
    """
    if scoped_department and scoped_department != "All":
        query += f" WHERE e.department = '{scoped_department}'"
    
    df = pd.read_sql_query(query, conn)
    conn.close()

    df['join_date'] = pd.to_datetime(df['join_date'])
    df['exit_date'] = pd.to_datetime(df['exit_date'], errors='coerce')
    df['is_flight_risk'] = df['is_flight_risk'].astype(bool)
    return df

def onboard_new_employee(emp_data: dict, actor: dict) -> dict:
    """Adds a new employee and initializes baseline training record."""
    conn = get_connection()
    cur = conn.cursor()

    emp_id = emp_data['employee_id']
    cur.execute("SELECT employee_id FROM employees WHERE employee_id = ?", (emp_id,))
    if cur.fetchone():
        conn.close()
        return {"success": False, "message": f"Employee ID {emp_id} already exists."}

    # Insert employee
    cur.execute("""
    INSERT INTO employees (employee_id, employee_name, department, job_role, gender, city, state, join_date, experience_years, salary, manager_id, attrition_flag)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        emp_id, emp_data['employee_name'], emp_data['department'], emp_data['job_role'],
        emp_data['gender'], emp_data['city'], emp_data['state'], emp_data['join_date'],
        emp_data['experience_years'], emp_data['salary'], emp_data['manager_id'], 'No'
    ))

    # Baseline training record
    pre_rating = emp_data['pre_training_rating']
    cur.execute("""
    INSERT INTO training_records (
        employee_id, training_program_name, training_type, pre_training_rating,
        training_hours, training_score, performance_rating, attendance_days,
        late_arrivals, hr_cost, rating_improvement, rating_uplift_pct,
        training_tier, performance_category, cost_per_training_hour, is_flight_risk
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        emp_id, emp_data['training_program_name'], emp_data['training_type'],
        pre_rating, 0.0, 0.0, pre_rating, 210, 10, 5000, 0.0, 0.0,
        'Minimal (<15h)', 'Meets Expectations', 5000.0, 0
    ))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
    INSERT INTO audit_log (timestamp, username, role, action, detail)
    VALUES (?, ?, ?, ?, ?)
    """, (now_str, actor['username'], actor['role'], "ONBOARD_EMPLOYEE", f"Onboarded {emp_data['employee_name']} ({emp_id}) into {emp_data['department']}"))
    
    conn.commit()
    conn.close()
    return {"success": True, "message": f"Employee {emp_data['employee_name']} ({emp_id}) successfully onboarded!"}

def log_training_completion(emp_id: str, program_name: str, hours_logged: float, test_score: float, actor: dict) -> dict:
    """Updates training record, calculates rating uplift, attendance gains, and recalculates flight risk."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT e.experience_years, e.salary, r.* 
    FROM employees e 
    JOIN training_records r ON e.employee_id = r.employee_id
    WHERE e.employee_id = ?
    """, (emp_id,))
    row = cur.fetchone()

    if not row:
        conn.close()
        return {"success": False, "message": f"Employee {emp_id} not found."}

    row = dict(row)
    pre_rating = row['pre_training_rating']
    
    # Calculate performance uplift based on hours & score
    score_factor = (test_score - 50.0) / 40.0
    hours_factor = (hours_logged - 15.0) / 30.0
    rating_uplift = round(float(np.clip((0.35 * hours_factor) + (0.45 * score_factor) + 0.15, -0.3, 1.8)), 2)
    post_rating = round(float(np.clip(pre_rating + rating_uplift, 1.0, 5.0)), 1)
    uplift_pct = round((rating_uplift / pre_rating) * 100, 1)

    # Attendance & late arrival updates
    attendance_days = int(np.clip(210 + int(hours_logged * 0.35), 180, 248))
    late_arrivals = int(np.clip(12 - int(hours_logged * 0.15), 0, 25))
    
    # Tier & Category
    tier = 'High (>35h)' if hours_logged > 35 else ('Moderate (15-35h)' if hours_logged >= 15 else 'Minimal (<15h)')
    cat = 'Outstanding' if post_rating >= 4.5 else ('Exceeds Expectations' if post_rating >= 3.5 else ('Meets Expectations' if post_rating >= 2.5 else 'Needs Improvement'))
    
    # Program cost addition
    hr_cost = int(row['hr_cost'] + (hours_logged * 850))
    cost_per_hr = round(hr_cost / max(hours_logged, 1.0), 2)

    # Flight risk check
    expected_sal = 450000 + (row['experience_years'] * 150000)
    is_flight_risk = 1 if (hours_logged >= 40.0 and post_rating >= 4.0 and row['salary'] < expected_sal) else 0

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
    UPDATE training_records
    SET training_program_name = ?, training_hours = ?, training_score = ?,
        performance_rating = ?, rating_improvement = ?, rating_uplift_pct = ?,
        attendance_days = ?, late_arrivals = ?, hr_cost = ?,
        training_tier = ?, performance_category = ?, cost_per_training_hour = ?,
        is_flight_risk = ?, completion_date = ?
    WHERE employee_id = ?
    """, (
        program_name, hours_logged, test_score, post_rating, rating_uplift, uplift_pct,
        attendance_days, late_arrivals, hr_cost, tier, cat, cost_per_hr, is_flight_risk,
        now_str, emp_id
    ))

    cur.execute("""
    INSERT INTO audit_log (timestamp, username, role, action, detail)
    VALUES (?, ?, ?, ?, ?)
    """, (now_str, actor['username'], actor['role'], "LOG_TRAINING", f"Updated {emp_id}: {hours_logged}h in {program_name}, Score: {test_score}%, New Rating: {post_rating}"))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "message": f"Successfully updated training record for {emp_id}! New Rating: {post_rating} (+{rating_uplift}), Tier: {tier}."
    }

def apply_retention_intervention(emp_id: str, action_type: str, hike_pct: float, note: str, actor: dict) -> dict:
    """Executes salary adjustment / bonus for talent retention, clearing poaching flight risk."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT employee_name, department, salary FROM employees WHERE employee_id = ?", (emp_id,))
    emp = cur.fetchone()
    if not emp:
        conn.close()
        return {"success": False, "message": "Employee not found."}

    old_salary = emp['salary']
    new_salary = int(old_salary * (1.0 + (hike_pct / 100.0))) if hike_pct > 0 else old_salary

    # Update employee salary
    cur.execute("UPDATE employees SET salary = ? WHERE employee_id = ?", (new_salary, emp_id))

    # Clear flight risk flag in training records
    cur.execute("UPDATE training_records SET is_flight_risk = 0 WHERE employee_id = ?", (emp_id,))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Record intervention
    cur.execute("""
    INSERT INTO interventions (employee_id, employee_name, department, action_type, salary_adjustment_pct, new_salary, details, requested_by, status, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (emp_id, emp['employee_name'], emp['department'], action_type, hike_pct, new_salary, note, actor['username'], 'Approved & Executed', now_str))

    # Audit log
    cur.execute("""
    INSERT INTO audit_log (timestamp, username, role, action, detail)
    VALUES (?, ?, ?, ?, ?)
    """, (now_str, actor['username'], actor['role'], "RETENTION_INTERVENTION", f"Applied {action_type} for {emp_id} ({emp['employee_name']}): Salary updated ₹ {old_salary:,} -> ₹ {new_salary:,} (+{hike_pct}%)"))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "message": f"Retention action applied for {emp['employee_name']} ({emp_id})! New remuneration: ₹ {new_salary:,}. Flight risk neutralized."
    }

def get_audit_trail(limit=100) -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query(f"SELECT * FROM audit_log ORDER BY id DESC LIMIT {limit}", conn)
    conn.close()
    return df

def get_interventions_log() -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM interventions ORDER BY id DESC", conn)
    conn.close()
    return df
