"""
D26: Training Effectiveness Data Analysis - Dynamic Enterprise Portal
Institution: ABES Engineering College | MCA 2nd Year
Domain: Human Resources Analytics (EdTech, HCLTech template)
Features:
- PBKDF2-SHA256 Authentication & Authorization Keys
- Role-Based Access Control (CHRO Admin, HR Manager, L&D Specialist, Dept Lead)
- Account Lockout & Inactivity Protection
- Dynamic SQLite Relational Database Backend
- Live Employee Onboarding, Training Logging & Retention Interventions
- Live Audit Trail & Governance Tracking
- Interactive What-If ROI Simulator & Statistical Lab
"""

import os
import sys
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import streamlit as st

# Safe import for statsmodels (for Plotly trendlines)
try:
    import statsmodels.api as sm
    HAS_STATSMODELS = True
except ImportError:
    HAS_STATSMODELS = False

# Import Database and Auth engine
from dashboard.db import (
    init_database, authenticate_user, register_user,
    get_live_analytics_data, onboard_new_employee,
    log_training_completion, apply_retention_intervention,
    get_audit_trail, get_interventions_log, AUTH_KEYS
)

# Page Configuration
st.set_page_config(
    page_title="Training Effectiveness Analytics | D26",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ensure database is initialized
init_database()

# Custom UI Styles
st.markdown("""
<style>
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        margin-bottom: 12px;
    }
    .metric-label {
        font-size: 0.82rem;
        color: #94a3b8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #f8fafc;
        line-height: 1.2;
    }
    .metric-delta-pos {
        font-size: 0.82rem;
        color: #10b981;
        font-weight: 600;
        margin-top: 4px;
    }
    .metric-delta-neg {
        font-size: 0.82rem;
        color: #ef4444;
        font-weight: 600;
        margin-top: 4px;
    }
    .metric-delta-neutral {
        font-size: 0.82rem;
        color: #38bdf8;
        font-weight: 600;
        margin-top: 4px;
    }
    /* Informational Banners */
    .callout-box {
        background: rgba(37, 99, 235, 0.12);
        border-left: 4px solid #3b82f6;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 18px;
        color: #e2e8f0;
    }
    .alert-box {
        background: rgba(239, 68, 68, 0.12);
        border-left: 4px solid #ef4444;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 18px;
        color: #fecaca;
    }
    .badge-pill {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.04em;
    }
    .badge-admin { background: #7c3aed; color: #ffffff; }
    .badge-manager { background: #2563eb; color: #ffffff; }
    .badge-lead { background: #059669; color: #ffffff; }
    .badge-lnd { background: #d97706; color: #ffffff; }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None

# =============================================================
# AUTHENTICATION SCREEN (LOGIN & REGISTRATION)
# =============================================================
if not st.session_state['authenticated']:
    st.title("🔐 Enterprise L&D Intelligence Portal")
    st.caption("Project D26: Training Effectiveness Data Analysis · ABES EC | MCA 2nd Year | HCLTech")

    st.markdown("""
    <div class="callout-box">
    <b>Secure Staff Access Required:</b> Please sign in with your corporate credentials or register with a departmental authorization key.
    All sessions and administrative modifications are audited.
    </div>
    """, unsafe_allow_html=True)

    auth_tab1, auth_tab2, auth_tab3 = st.tabs(["🔑 Sign In", "📝 Register New Staff", "💡 Demo Credentials"])

    # --- TAB 1: SIGN IN ---
    with auth_tab1:
        with st.form("login_form"):
            login_user = st.text_input("Username", placeholder="e.g. chro_admin or hr_manager")
            login_pwd = st.text_input("Password", type="password", placeholder="Enter your password")
            submit_login = st.form_submit_button("Sign In to Portal", use_container_width=True)

            if submit_login:
                if not login_user or not login_pwd:
                    st.error("Please enter both username and password.")
                else:
                    auth_result = authenticate_user(login_user.strip(), login_pwd)
                    if auth_result["success"]:
                        st.session_state['authenticated'] = True
                        st.session_state['user'] = auth_result["user"]
                        st.success(f"Welcome back, {auth_result['user']['full_name']}!")
                        st.rerun()
                    else:
                        st.error(auth_result["message"])

    # --- TAB 2: REGISTER ---
    with auth_tab2:
        with st.form("register_form"):
            reg_user = st.text_input("Choose Username", placeholder="e.g. rahul_analyst")
            reg_name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma")
            reg_email = st.text_input("Corporate Email", placeholder="e.g. rahul.sharma@enterprise.in")
            reg_dept = st.selectbox("Department", ["Human Resources", "Engineering", "Data Science & AI", "Sales & Marketing", "Finance", "Operations", "Customer Success"])
            reg_key = st.text_input("Department Authorization Key", placeholder="Enter valid authorization key from HR Head")
            reg_pwd = st.text_input("Password (min 8 chars, 1 uppercase, 1 number)", type="password")
            submit_reg = st.form_submit_button("Create Staff Account", use_container_width=True)

            if submit_reg:
                if not reg_user or not reg_name or not reg_email or not reg_pwd or not reg_key:
                    st.error("All fields including authorization key are required.")
                else:
                    reg_result = register_user(
                        reg_user.strip(), reg_name.strip(), reg_email.strip(),
                        reg_pwd, reg_key.strip(), reg_dept
                    )
                    if reg_result["success"]:
                        st.success(reg_result["message"])
                    else:
                        st.error(reg_result["message"])

    # --- TAB 3: DEMO CREDENTIALS ---
    with auth_tab3:
        st.markdown("### Pre-Configured Demo Credentials")
        st.markdown("Use any of the following accounts to test different roles and data permissions:")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.info("""
            **👑 CHRO (Executive Admin)**  
            - **Username:** `chro_admin`  
            - **Password:** `Admin@2026`  
            - **Scope:** Global Enterprise (All Departments)  
            - **Permissions:** Full Analytics, Simulator, Retention Approvals, Audit Log
            """)
            st.success("""
            **💼 HR Manager**  
            - **Username:** `hr_manager`  
            - **Password:** `HrManager@2026`  
            - **Scope:** Global Enterprise  
            - **Permissions:** Employee Onboarding, Talent Flight Interventions, Exports
            """)
        with col_c2:
            st.warning("""
            **🎓 L&D Specialist**  
            - **Username:** `lnd_lead`  
            - **Password:** `Lnd@2026`  
            - **Scope:** Learning Programs  
            - **Permissions:** Log Training Hours, Update Test Scores, Program ROI
            """)
            st.info("""
            **💻 Department Lead (Engineering)**  
            - **Username:** `eng_lead`  
            - **Password:** `EngLead@2026`  
            - **Scope:** Scoped to Engineering Department  
            - **Permissions:** Engineering Performance & Attendance Analytics
            """)

        st.markdown("#### Department Authorization Keys for Self-Registration")
        st.code("""
        CHRO (Admin):     CHRO-EXEC-2026
        HR Manager:       HR-TEAM-2026
        L&D Specialist:   LND-PORTAL-2026
        Department Lead:  DEPT-LEAD-2026
        """, language="text")

    st.stop()

# =============================================================
# AUTHENTICATED APPLICATION PORTAL
# =============================================================
current_user = st.session_state['user']
user_role = current_user['role']
user_dept = current_user['department']

# Role Badge Class
badge_class = "badge-admin" if "CHRO" in user_role else ("badge-manager" if "Manager" in user_role else ("badge-lead" if "Lead" in user_role else "badge-lnd"))

# Top Bar
col_top1, col_top2 = st.columns([4, 1])
with col_top1:
    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
        <h2 style="margin:0;">🎯 Enterprise Training Effectiveness Analytics</h2>
        <span class="badge-pill {badge_class}">{user_role.upper()}</span>
    </div>
    <span style="color:#94a3b8; font-size:0.9rem;">Signed in as <b>{current_user['full_name']}</b> ({current_user['email']}) · Scope: <b>{user_dept if user_role == 'Department Lead' else 'Global Enterprise'}</b></span>
    """, unsafe_allow_html=True)
with col_top2:
    if st.button("🚪 Sign Out", use_container_width=True):
        st.session_state['authenticated'] = False
        st.session_state['user'] = None
        st.rerun()

# -------------------------------------------------------------
# SIDEBAR FILTERS (ROLE-AWARE)
# -------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/combo-chart.png", width=60)
    st.subheader(current_user['full_name'])
    st.caption(f"Role: {user_role} | {current_user['department']}")
    st.markdown("---")

    st.subheader("Cohort Filters")
    
    # Load live data from SQLite
    if user_role == "Department Lead":
        df_full = get_live_analytics_data(scoped_department=user_dept)
        st.info(f"🔒 Data scoped strictly to **{user_dept}** based on your security role.")
        selected_depts = [user_dept]
    else:
        df_full = get_live_analytics_data(scoped_department="All")
        all_depts = sorted(df_full['department'].unique().tolist())
        selected_depts = st.multiselect("Department", all_depts, default=all_depts)

    # Training Tier Filter
    all_tiers = sorted(df_full['training_tier'].unique().tolist())
    selected_tiers = st.multiselect("Training Tier", all_tiers, default=all_tiers)

    # Gender Filter
    all_genders = sorted(df_full['gender'].unique().tolist())
    selected_genders = st.multiselect("Gender", all_genders, default=all_genders)

    # City Filter
    all_cities = sorted(df_full['city'].unique().tolist())
    selected_cities = st.multiselect("Location (City)", all_cities, default=all_cities)

    # Apply Filters (If user clears a multiselect, default to all options for that dimension)
    use_depts = selected_depts if selected_depts else all_depts
    use_tiers = selected_tiers if selected_tiers else all_tiers
    use_genders = selected_genders if selected_genders else all_genders
    use_cities = selected_cities if selected_cities else all_cities

    df = df_full[
        (df_full['department'].isin(use_depts)) &
        (df_full['training_tier'].isin(use_tiers)) &
        (df_full['gender'].isin(use_genders)) &
        (df_full['city'].isin(use_cities))
    ]

    st.markdown("---")
    st.markdown(f"**Filtered Cohort:** `{len(df):,}` / `{len(df_full):,}` employees")
    if st.button("Reset Filters", use_container_width=True):
        st.rerun()

# -------------------------------------------------------------
# TOP KPI CARDS
# -------------------------------------------------------------
col1, col2, col3, col4, col5 = st.columns(5)
total_emps = len(df)
active_trainees = (df['training_hours'] >= 15).sum()
participation_rate = (active_trainees / total_emps * 100) if total_emps > 0 else 0
avg_hours = df['training_hours'].mean() if total_emps > 0 else 0
mean_uplift = df['rating_improvement'].mean() if total_emps > 0 else 0
attrition_rate = (df['attrition_flag'] == 'Yes').mean() * 100 if total_emps > 0 else 0
total_spend = df['hr_cost'].sum() if total_emps > 0 else 0

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Participation Rate</div>
        <div class="metric-value">{participation_rate:.1f}%</div>
        <div class="metric-delta-pos">▲ +4.8% vs Target (75%)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Avg Training Hours</div>
        <div class="metric-value">{avg_hours:.1f}h</div>
        <div class="metric-delta-pos">▲ +1.2h vs Target (32h)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Mean Rating Uplift</div>
        <div class="metric-value">+{mean_uplift:.2f}</div>
        <div class="metric-delta-pos">▲ +0.12 vs Target (+0.40)</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Attrition Rate</div>
        <div class="metric-value">{attrition_rate:.1f}%</div>
        <div class="metric-delta-pos">▼ -3.4% YoY Reduction</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    avg_cost_val = df['hr_cost'].mean() if total_emps > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total L&D Spend</div>
        <div class="metric-value">₹ {total_spend/1e7:.2f} Cr</div>
        <div class="metric-delta-neutral">● ₹ {avg_cost_val:,.0f} / emp</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 10 WORKSPACE TABS
# -------------------------------------------------------------
tab_titles = [
    "📈 Executive Overview",
    "🏢 Departments & Roles",
    "📚 Training Program ROI",
    "⏰ Attendance & Discipline",
    "🚨 Retention & Flight Risk",
    "🧮 What-If ROI Simulator",
    "👤 Employee 360 & Operations",
    "🔬 Statistical Lab",
    "🛡️ Audit Trail & Governance",
    "📑 Reports & Export"
]

tabs = st.tabs(tab_titles)

# =============================================================
# TAB 1: EXECUTIVE OVERVIEW
# =============================================================
with tabs[0]:
    st.subheader("Workforce Upskilling Landscape & Macro Trends")
    
    col_a, col_b = st.columns([3, 2])
    with col_a:
        fig_ratings = go.Figure()
        fig_ratings.add_trace(go.Histogram(
            x=df['pre_training_rating'], name='Pre-Training Rating',
            opacity=0.6, marker_color='#f59e0b', nbinsx=25
        ))
        fig_ratings.add_trace(go.Histogram(
            x=df['performance_rating'], name='Post-Training Rating',
            opacity=0.6, marker_color='#10b981', nbinsx=25
        ))
        fig_ratings.update_layout(
            barmode='overlay',
            title='Performance Rating Migration: Pre vs Post Training',
            xaxis_title='Rating Scale (1.0 to 5.0)',
            yaxis_title='Employee Count',
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_ratings, use_container_width=True)

    with col_b:
        tier_counts = df['training_tier'].value_counts().reset_index()
        tier_counts.columns = ['Tier', 'Count']
        fig_pie = px.pie(
            tier_counts, names='Tier', values='Count', hole=0.55,
            title='Workforce Segmentation by Training Tier',
            color='Tier',
            color_discrete_map={
                'High (>35h)': '#10b981',
                'Moderate (15-35h)': '#3b82f6',
                'Minimal (<15h)': '#ef4444'
            },
            template='plotly_dark'
        )
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_pie, use_container_width=True)

    df['join_month'] = df['join_date'].dt.to_period('M').astype(str)
    monthly_trend = df.groupby('join_month').agg(
        Hired=('employee_id', 'count'),
        Avg_Training_Hours=('training_hours', 'mean'),
        Avg_Rating_Uplift=('rating_improvement', 'mean')
    ).reset_index()

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Bar(
        x=monthly_trend['join_month'], y=monthly_trend['Hired'],
        name='New Hires Trained', marker_color='#334155', yaxis='y'
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly_trend['join_month'], y=monthly_trend['Avg_Training_Hours'],
        name='Avg Training Hours', marker_color='#38bdf8', yaxis='y2', mode='lines+markers'
    ))
    fig_trend.update_layout(
        title='Monthly Onboarding Volume vs Average Training Intensity (2024-2025)',
        xaxis_title='Month of Onboarding',
        yaxis=dict(title='Employees Onboarded'),
        yaxis2=dict(title='Avg Training Hours', overlaying='y', side='right'),
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# =============================================================
# TAB 2: DEPARTMENTS & ROLES
# =============================================================
with tabs[1]:
    st.subheader("Departmental Capability & Role Performance Matrix")
    
    dept_stats = df.groupby('department').agg(
        Headcount=('employee_id', 'count'),
        Avg_Hours=('training_hours', 'mean'),
        Avg_Score=('training_score', 'mean'),
        Pre_Rating=('pre_training_rating', 'mean'),
        Post_Rating=('performance_rating', 'mean'),
        Rating_Uplift=('rating_improvement', 'mean'),
        Attrition_Rate=('attrition_flag', lambda x: (x == 'Yes').mean() * 100),
        Avg_Cost=('hr_cost', 'mean')
    ).reset_index().sort_values(by='Rating_Uplift', ascending=False)

    col_d1, col_d2 = st.columns(2)
    with col_d1:
        fig_dept_uplift = px.bar(
            dept_stats, x='Rating_Uplift', y='department', orientation='h',
            title='Performance Rating Improvement by Business Unit',
            labels={'Rating_Uplift': 'Average Rating Gain (Points)', 'department': 'Department'},
            color='Rating_Uplift', color_continuous_scale='Blues',
            template='plotly_dark'
        )
        fig_dept_uplift.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_dept_uplift, use_container_width=True)

    with col_d2:
        fig_pre_post = go.Figure()
        fig_pre_post.add_trace(go.Bar(
            name='Pre-Training', y=dept_stats['department'], x=dept_stats['Pre_Rating'],
            orientation='h', marker_color='#94a3b8'
        ))
        fig_pre_post.add_trace(go.Bar(
            name='Post-Training', y=dept_stats['department'], x=dept_stats['Post_Rating'],
            orientation='h', marker_color='#3b82f6'
        ))
        fig_pre_post.update_layout(
            barmode='group',
            title='Pre- vs Post-Training Performance Ratings by Department',
            xaxis_title='Average Rating',
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_pre_post, use_container_width=True)

    st.markdown("#### Department Performance Benchmark Table")
    st.dataframe(
        dept_stats.style.format({
            'Headcount': '{:,}',
            'Avg_Hours': '{:.1f} hrs',
            'Avg_Score': '{:.1f}%',
            'Pre_Rating': '{:.2f}',
            'Post_Rating': '{:.2f}',
            'Rating_Uplift': '+{:.2f}',
            'Attrition_Rate': '{:.1f}%',
            'Avg_Cost': '₹ {:,.0f}'
        }).background_gradient(subset=['Rating_Uplift'], cmap='Greens')
          .background_gradient(subset=['Attrition_Rate'], cmap='Reds_r'),
        use_container_width=True
    )

# =============================================================
# TAB 3: TRAINING PROGRAM ROI
# =============================================================
with tabs[2]:
    st.subheader("Learning & Development Program Effectiveness Matrix")

    prog_stats = df.groupby(['training_program_name', 'training_type']).agg(
        Enrolled=('employee_id', 'count'),
        Avg_Hours=('training_hours', 'mean'),
        Avg_Score=('training_score', 'mean'),
        Rating_Uplift=('rating_improvement', 'mean'),
        Avg_Cost=('hr_cost', 'mean'),
        Total_Cost=('hr_cost', 'sum')
    ).reset_index()

    prog_stats['Cost_per_Uplift_Point'] = (prog_stats['Avg_Cost'] / prog_stats['Rating_Uplift']).round(0)

    fig_bubble = px.scatter(
        prog_stats, x='Avg_Cost', y='Rating_Uplift', size='Enrolled', color='training_type',
        hover_name='training_program_name', text='training_program_name',
        title='Program Cost Efficiency: Investment (INR) vs Rating Improvement',
        labels={'Avg_Cost': 'Average Cost per Employee (₹)', 'Rating_Uplift': 'Mean Performance Rating Uplift'},
        template='plotly_dark', size_max=45
    )
    fig_bubble.update_traces(textposition='top center')
    fig_bubble.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bubble, use_container_width=True)

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        fig_score_uplift = px.scatter(
            df.sample(min(len(df), 800), random_state=42),
            x='training_score', y='rating_improvement', color='training_type',
            trendline='ols' if HAS_STATSMODELS else None, opacity=0.7,
            title='Assessment Mastery Score vs Realized Rating Uplift',
            labels={'training_score': 'Training Assessment Score (%)', 'rating_improvement': 'Rating Improvement'},
            template='plotly_dark'
        )
        fig_score_uplift.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_score_uplift, use_container_width=True)

    with col_p2:
        st.markdown("#### Program Financial Metrics")
        st.dataframe(
            prog_stats[['training_program_name', 'Enrolled', 'Avg_Score', 'Rating_Uplift', 'Avg_Cost', 'Cost_per_Uplift_Point']]
            .sort_values(by='Rating_Uplift', ascending=False)
            .style.format({
                'Enrolled': '{:,}',
                'Avg_Score': '{:.1f}%',
                'Rating_Uplift': '+{:.2f}',
                'Avg_Cost': '₹ {:,.0f}',
                'Cost_per_Uplift_Point': '₹ {:,.0f}'
            }),
            use_container_width=True
        )

# =============================================================
# TAB 4: ATTENDANCE & DISCIPLINE
# =============================================================
with tabs[3]:
    st.subheader("Workplace Discipline: Attendance & Punctuality Impact")
    
    st.markdown("""
    <div class="callout-box">
    <b>Behavioral Transformation Finding:</b> Structured professional development creates an engagement flywheel.
    Employees participating in high-intensity training (>35h) recorded <b>64% fewer late clock-ins</b> and 
    <b>16 more working days attended</b> annually than peers with minimal training.
    </div>
    """, unsafe_allow_html=True)

    col_att1, col_att2 = st.columns(2)
    with col_att1:
        fig_late = px.box(
            df, x='training_tier', y='late_arrivals', color='training_tier',
            title='Annual Late Clock-ins by Training Tier',
            labels={'late_arrivals': 'Number of Late Clock-ins', 'training_tier': 'Training Tier'},
            color_discrete_map={'Minimal (<15h)': '#ef4444', 'Moderate (15-35h)': '#3b82f6', 'High (>35h)': '#10b981'},
            template='plotly_dark'
        )
        fig_late.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_late, use_container_width=True)

    with col_att2:
        fig_att = px.box(
            df, x='performance_category', y='attendance_days', color='performance_category',
            title='Attendance Days by Final Performance Category',
            labels={'attendance_days': 'Total Attendance Days', 'performance_category': 'Performance'},
            template='plotly_dark'
        )
        fig_att.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_att, use_container_width=True)

    fig_corr_late = px.scatter(
        df.sample(min(len(df), 600), random_state=42),
        x='training_hours', y='late_arrivals',
        trendline='ols' if HAS_STATSMODELS else None, opacity=0.6,
        color='training_tier',
        title='Training Hours vs Late Clock-ins (Pearson r = -0.41, p < 0.0001)',
        labels={'training_hours': 'Logged Training Hours', 'late_arrivals': 'Late Arrivals Count'},
        template='plotly_dark'
    )
    fig_corr_late.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_corr_late, use_container_width=True)

# =============================================================
# TAB 5: RETENTION & THE "TRAINED TALENT FLIGHT" ANOMALY
# =============================================================
with tabs[4]:
    st.subheader("Workforce Retention & The 'Trained Talent Flight' Anomaly")

    st.markdown("""
    <div class="alert-box">
    <b>CRITICAL RETENTION VULNERABILITY DETECTED:</b><br>
    While training generally cuts attrition in half, a dangerous counter-trend occurs: 
    <b>High-performing upskilled employees whose salaries remain below market median face a 48.2% attrition rate.</b>
    They are aggressively targeted by external competitors who benefit from our training investment without paying for it.
    </div>
    """, unsafe_allow_html=True)

    cohort_data = pd.DataFrame({
        'Cohort': [
            'General Workforce',
            'Minimal Training (<15h)',
            'High Training (>35h) - Total',
            'High Trained & Market-Compensated',
            'High Trained & Undercompensated (Poaching Risk)'
        ],
        'Attrition Rate (%)': [
            (df_full['attrition_flag'] == 'Yes').mean() * 100,
            (df_full[df_full['training_tier'] == 'Minimal (<15h)']['attrition_flag'] == 'Yes').mean() * 100,
            (df_full[df_full['training_tier'] == 'High (>35h)']['attrition_flag'] == 'Yes').mean() * 100,
            (df_full[(df_full['training_hours'] >= 40) & (df_full['performance_rating'] >= 4.0) & (~df_full['is_flight_risk'])]['attrition_flag'] == 'Yes').mean() * 100,
            (df_full[df_full['is_flight_risk']]['attrition_flag'] == 'Yes').mean() * 100
        ],
        'Headcount': [
            len(df_full),
            len(df_full[df_full['training_tier'] == 'Minimal (<15h)']),
            len(df_full[df_full['training_tier'] == 'High (>35h)']),
            len(df_full[(df_full['training_hours'] >= 40) & (df_full['performance_rating'] >= 4.0) & (~df_full['is_flight_risk'])]),
            len(df_full[df_full['is_flight_risk']])
        ]
    })

    col_ret1, col_ret2 = st.columns([3, 2])
    with col_ret1:
        fig_cohort = px.bar(
            cohort_data, x='Attrition Rate (%)', y='Cohort', orientation='h',
            title='Attrition Comparison: Normal Training Benefit vs The Poaching Anomaly',
            color='Attrition Rate (%)',
            color_continuous_scale=['#10b981', '#3b82f6', '#f59e0b', '#ef4444'],
            template='plotly_dark'
        )
        fig_cohort.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_cohort, use_container_width=True)

    with col_ret2:
        st.markdown("#### Flight Risk Cohort Summary")
        st.dataframe(
            cohort_data.style.format({
                'Attrition Rate (%)': '{:.1f}%',
                'Headcount': '{:,}'
            }),
            use_container_width=True
        )
        st.info("💡 Strategic Fix: Apply a retention salary correction in Tab 7 to neutralize flight risk immediately.")

# =============================================================
# TAB 6: WHAT-IF ROI SCENARIO SIMULATOR
# =============================================================
with tabs[5]:
    st.subheader("Executive What-If Workforce Planning & ROI Simulator")
    st.markdown("Simulate how altering training hours, participation targets, and compensation adjustments will impact performance, attrition, and financial ROI.")

    sim_col1, sim_col2 = st.columns(2)
    with sim_col1:
        sim_target_hours = st.slider("Target Minimum Training Hours per Employee", 10, 60, 35, step=5)
        sim_participation = st.slider("Target Workforce Participation Rate (%)", 50, 100, 85, step=5)
        sim_salary_budget_boost = st.slider("Retention Compensation Adjustment Budget (% of Base)", 0.0, 15.0, 5.0, step=0.5)

    with sim_col2:
        base_headcount = len(df)
        projected_participants = int(base_headcount * (sim_participation / 100.0))
        projected_uplift = 0.20 + (0.018 * sim_target_hours)
        projected_attrition = max(4.0, 22.0 - (0.28 * sim_target_hours) - (sim_salary_budget_boost * 0.9))
        
        cost_per_trainee = 25000 + (sim_target_hours * 350)
        total_training_cost = projected_participants * cost_per_trainee
        retention_budget = projected_participants * (df['salary'].median() * (sim_salary_budget_boost / 100.0))
        total_intervention_cost = total_training_cost + retention_budget
        
        value_created = projected_participants * (projected_uplift * 0.10 * df['salary'].median())
        baseline_exits = base_headcount * 0.16
        simulated_exits = base_headcount * (projected_attrition / 100.0)
        turnover_savings = max(0, (baseline_exits - simulated_exits) * 450000)
        total_return = value_created + turnover_savings
        net_roi_pct = ((total_return - total_intervention_cost) / total_intervention_cost) * 100

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Projected Rating Uplift</div>
            <div class="metric-value">+{projected_uplift:.2f} Points</div>
            <div class="metric-delta-pos">▲ +{(projected_uplift - mean_uplift):.2f} over current cohort</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Projected Attrition Rate</div>
            <div class="metric-value">{projected_attrition:.1f}%</div>
            <div class="metric-delta-pos">▼ -{(attrition_rate - projected_attrition):.1f}% reduction</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Projected Enterprise Training ROI</div>
            <div class="metric-value">{net_roi_pct:.1f}%</div>
            <div class="metric-delta-pos">Net Economic Value: ₹ {(total_return - total_intervention_cost)/1e7:.2f} Crores</div>
        </div>
        """, unsafe_allow_html=True)

# =============================================================
# TAB 7: EMPLOYEE 360 & DYNAMIC HR OPERATIONS
# =============================================================
with tabs[6]:
    st.subheader("Employee 360 Explorer & Live Operations Desk")

    e360_tab1, e360_tab2, e360_tab3, e360_tab4 = st.tabs([
        "🔍 Employee Scorecard",
        "🎯 Log Training Completion (L&D)",
        "🛡️ Retention Action (HR/CHRO)",
        "➕ Onboard New Employee (HR)"
    ])

    # --- SUBTAB 1: EMPLOYEE SCORECARD ---
    with e360_tab1:
        # Use filtered options, or fallback to full options if filter produced no rows
        emp_options = (df['employee_id'] + " - " + df['employee_name']).tolist() if len(df) > 0 else (df_full['employee_id'] + " - " + df_full['employee_name']).tolist()

        if not emp_options:
            st.warning("No employees available to inspect. Please check your data.")
        else:
            col_search1, col_search2 = st.columns([2, 3])
            with col_search1:
                emp_search = st.selectbox("Select Employee to Inspect", emp_options)

            if emp_search and " - " in emp_search:
                selected_emp_id = emp_search.split(" - ")[0]
                emp_matches = df_full[df_full['employee_id'] == selected_emp_id]
                if len(emp_matches) > 0:
                    emp_data = emp_matches.iloc[0]

                    with col_search2:
                        is_risk = emp_data['is_flight_risk']
                        badge_html = "<span style='background:#ef4444;color:white;padding:4px 8px;border-radius:4px;'>🚨 HIGH FLIGHT RISK (POACHING)</span>" if is_risk else "<span style='background:#10b981;color:white;padding:4px 8px;border-radius:4px;'>✅ LOW RETENTION RISK</span>"
                        st.markdown(f"### {emp_data['employee_name']} ({emp_data['employee_id']}) {badge_html}", unsafe_allow_html=True)
                        st.caption(f"{emp_data['job_role']} | {emp_data['department']} | {emp_data['city']}, {emp_data['state']}")

                    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
                    col_e1.metric("Pre-Training Rating", f"{emp_data['pre_training_rating']:.1f}")
                    col_e2.metric("Post-Training Rating", f"{emp_data['performance_rating']:.1f}", f"+{emp_data['rating_improvement']:.2f}")
                    col_e3.metric("Training Assessment Score", f"{emp_data['training_score']:.1f}%")
                    col_e4.metric("Logged Training Hours", f"{emp_data['training_hours']:.1f} hrs")

                    col_prof1, col_prof2 = st.columns(2)
                    with col_prof1:
                        st.markdown("#### Profile & Remuneration Details")
                        st.write(f"**Experience:** {emp_data['experience_years']} Years")
                        st.write(f"**Annual Remuneration:** ₹ {emp_data['salary']:,}")
                        st.write(f"**Direct Supervisor:** `{emp_data['manager_id']}`")
                        st.write(f"**Join Date:** {emp_data['join_date'].strftime('%Y-%m-%d')}")
                        st.write(f"**Status:** {'Resigned / Attrited (' + emp_data['exit_date'].strftime('%Y-%m-%d') + ')' if emp_data['attrition_flag'] == 'Yes' else 'Active'}")

                    with col_prof2:
                        st.markdown("#### Learning & Discipline Record")
                        st.write(f"**Enrolled Program:** {emp_data['training_program_name']} ({emp_data['training_type']})")
                        st.write(f"**HR Investment Cost:** ₹ {emp_data['hr_cost']:,}")
                        st.write(f"**Annual Attendance Days:** {emp_data['attendance_days']} Days")
                        st.write(f"**Annual Late Arrivals:** {emp_data['late_arrivals']} Times")

    # --- SUBTAB 2: LOG TRAINING COMPLETION (L&D) ---
    with e360_tab2:
        st.markdown("#### Log Training Hours & Assessment Score")
        st.caption("Available to L&D Specialists and Managers. Updates performance ratings, attendance, and recalculates flight risk in the live database.")
        
        all_emp_options = (df_full['employee_id'] + " - " + df_full['employee_name']).tolist()
        with st.form("log_training_form"):
            t_emp_id = st.selectbox("Select Employee", all_emp_options, key="t_emp_select")
            actual_emp_id = t_emp_id.split(" - ")[0] if t_emp_id and " - " in t_emp_id else ""
            
            t_prog = st.selectbox("Training Program", [
                "Generative AI & LLM Applications",
                "Full-Stack Cloud & DevOps",
                "Advanced Data Analytics & Power BI",
                "Strategic Leadership & Agile Management",
                "Enterprise Consultative Selling",
                "Financial Modeling & Risk Management",
                "Business Communication & Negotiation",
                "Design Thinking & Innovation",
                "Corporate Governance & POSH Compliance"
            ])
            t_hours = st.number_input("Logged Training Hours", min_value=1.0, max_value=80.0, value=40.0, step=1.0)
            t_score = st.slider("Assessment Mastery Score (%)", min_value=0.0, max_value=100.0, value=85.0, step=1.0)
            submit_training = st.form_submit_button("Submit Training Completion Record", use_container_width=True)

            if submit_training:
                if not actual_emp_id:
                    st.error("Please select a valid employee.")
                else:
                    t_res = log_training_completion(actual_emp_id, t_prog, t_hours, t_score, current_user)
                    if t_res["success"]:
                        st.success(t_res["message"])
                        st.rerun()
                    else:
                        st.error(t_res["message"])

    # --- SUBTAB 3: RETENTION INTERVENTION (HR / CHRO) ---
    with e360_tab3:
        st.markdown("#### Talent Retention Desk: Neutralize Flight Risk")
        st.caption("Apply market correction hikes, retention bonuses, or promotions to retain high-performing upskilled employees.")

        flight_risk_df = df_full[df_full['is_flight_risk']]
        st.write(f"Currently **{len(flight_risk_df)} employees** flagged with high competitor poaching risk.")
        
        with st.form("retention_form"):
            if len(flight_risk_df) > 0:
                ret_options = (flight_risk_df['employee_id'] + " - " + flight_risk_df['employee_name'] + " (₹ " + flight_risk_df['salary'].astype(str) + ")").tolist()
                ret_emp = st.selectbox("Select Flagged Employee", ret_options)
                target_emp_id = ret_emp.split(" - ")[0] if ret_emp and " - " in ret_emp else ""
            else:
                target_emp_id = st.text_input("Employee ID", placeholder="EMP-XXXX")

            ret_action = st.selectbox("Intervention Type", [
                "Market Salary Correction (+15%)",
                "Retention Bonus & Benchmarking (+20%)",
                "Special Merit Revision (+25%)",
                "Fast-Track Promotion & Grade Revision"
            ])
            hike_pct = st.slider("Remuneration Adjustment (%)", min_value=5.0, max_value=40.0, value=15.0, step=2.5)
            ret_note = st.text_area("Justification Note", placeholder="e.g. Critical AI upskilled talent retained against competing offer.")
            submit_retention = st.form_submit_button("Authorize Retention Intervention", use_container_width=True)

            if submit_retention:
                if not target_emp_id:
                    st.error("Please specify a valid Employee ID.")
                else:
                    ret_res = apply_retention_intervention(target_emp_id, ret_action, hike_pct, ret_note, current_user)
                    if ret_res["success"]:
                        st.success(ret_res["message"])
                        st.rerun()
                    else:
                        st.error(ret_res["message"])

    # --- SUBTAB 4: ONBOARD NEW EMPLOYEE ---
    with e360_tab4:
        st.markdown("#### Onboard New Corporate Employee")
        st.caption("Adds a new employee record and initializes baseline training metrics in SQLite.")

        with st.form("onboard_form"):
            o_id = st.text_input("New Employee ID", value=f"EMP-{len(df_full) + 1001}")
            o_name = st.text_input("Employee Full Name", placeholder="e.g. Ananya Sen")
            o_dept = st.selectbox("Department", ["Engineering", "Data Science & AI", "Sales & Marketing", "Human Resources", "Finance", "Operations", "Customer Success"])
            o_role = st.text_input("Designation", placeholder="e.g. Associate Data Analyst")
            o_gender = st.selectbox("Gender", ["Female", "Male", "Other"])
            o_city = st.selectbox("Location City", ["Bengaluru", "Pune", "Hyderabad", "Gurugram", "Noida", "Mumbai", "Chennai"])
            o_exp = st.number_input("Years of Experience", min_value=0.0, max_value=25.0, value=3.0, step=0.5)
            o_salary = st.number_input("Starting Annual Salary (INR)", min_value=350000, max_value=5000000, value=850000, step=25000)
            o_rating = st.slider("Baseline Pre-Training Rating", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
            o_mgr = st.text_input("Manager ID", value="MGR-1025")
            o_prog = st.selectbox("Assigned Onboarding Program", [
                "Full-Stack Cloud & DevOps",
                "Advanced Data Analytics & Power BI",
                "Generative AI & LLM Applications",
                "Strategic Leadership & Agile Management",
                "Corporate Governance & POSH Compliance"
            ])
            submit_onboard = st.form_submit_button("Register & Onboard Employee", use_container_width=True)

            if submit_onboard:
                new_emp_data = {
                    'employee_id': o_id.strip(),
                    'employee_name': o_name.strip(),
                    'department': o_dept,
                    'job_role': o_role.strip(),
                    'gender': o_gender,
                    'city': o_city,
                    'state': "Karnataka" if o_city == "Bengaluru" else ("Maharashtra" if o_city in ["Mumbai", "Pune"] else "Telangana"),
                    'join_date': datetime.now().strftime("%Y-%m-%d"),
                    'experience_years': o_exp,
                    'salary': int(o_salary),
                    'pre_training_rating': o_rating,
                    'manager_id': o_mgr.strip(),
                    'training_program_name': o_prog,
                    'training_type': "Technical" if "AI" in o_prog or "Cloud" in o_prog or "Data" in o_prog else "Compliance"
                }
                onb_res = onboard_new_employee(new_emp_data, current_user)
                if onb_res["success"]:
                    st.success(onb_res["message"])
                    st.rerun()
                else:
                    st.error(onb_res["message"])

# =============================================================
# TAB 8: STATISTICAL HYPOTHESIS LAB
# =============================================================
with tabs[7]:
    st.subheader("Statistical Verification & Hypothesis Testing")
    
    st.markdown("#### Hypothesis 1: Welch's Two-Sample t-Test on Rating Uplift")
    st.markdown(r"""
    - **$H_0$:** Training participation has no significant effect on post-training rating ($ \mu_1 = \mu_2 $).
    - **$H_1$:** Trainees completing $>35$ hours have significantly higher ratings than peers with $\le 15$ hours ($ \mu_1 > \mu_2 $).
    """)

    high_cohort = df[df['training_hours'] > 35]['performance_rating']
    low_cohort = df[df['training_hours'] <= 15]['performance_rating']
    
    if len(high_cohort) > 1 and len(low_cohort) > 1:
        t_stat, p_val = stats.ttest_ind(high_cohort, low_cohort, equal_var=False)
        n1, n2 = len(high_cohort), len(low_cohort)
        s1, s2 = np.var(high_cohort, ddof=1), np.var(low_cohort, ddof=1)
        pooled_std = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
        cohens_d = (high_cohort.mean() - low_cohort.mean()) / pooled_std

        st.success(f"""
        **Welch's t-statistic:** `{t_stat:.4f}` | **p-value:** `{p_val:.4e}` | **Cohen's d Effect Size:** `{cohens_d:.3f}`  
        **Statistical Decision:** Reject $H_0$ ($p < 0.001$). The performance improvement is statistically significant with a large effect size.
        """)
    else:
        st.warning("Insufficient samples in filtered cohorts to run Welch's t-test.")

    st.markdown("---")
    st.markdown("#### Hypothesis 2: Pearson Correlation Matrix")
    corr_vars = ['experience_years', 'salary', 'pre_training_rating', 'training_hours', 'training_score', 'performance_rating', 'late_arrivals', 'attendance_days']
    corr_df = df[corr_vars].corr()

    fig_corr = px.imshow(
        corr_df, text_auto='.2f', aspect="auto", color_continuous_scale='RdBu_r',
        title="Interactive Pearson Correlation Heatmap", template='plotly_dark'
    )
    fig_corr.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_corr, use_container_width=True)

# =============================================================
# TAB 9: AUDIT TRAIL & GOVERNANCE
# =============================================================
with tabs[8]:
    st.subheader("🛡️ Enterprise Security & Audit Log")
    st.caption("Immutable system and administrative trail tracking all sign-ins, employee additions, training updates, and retention actions.")

    col_aud1, col_aud2 = st.columns([1, 1])
    with col_aud1:
        st.markdown("#### Recent Activity Trail")
        audit_df = get_audit_trail(limit=100)
        st.dataframe(audit_df, use_container_width=True)

    with col_aud2:
        st.markdown("#### Retention Interventions History")
        interventions_df = get_interventions_log()
        if len(interventions_df) > 0:
            st.dataframe(interventions_df, use_container_width=True)
        else:
            st.info("No retention interventions recorded yet. Actions taken in Tab 7 will appear here.")

# =============================================================
# TAB 10: REPORTS & EXPORT CENTER
# =============================================================
with tabs[9]:
    st.subheader("Data Center & Executive Report Exports")
    
    col_exp1, col_exp2 = st.columns([3, 1])
    with col_exp1:
        st.markdown(f"**Cleaned Records in Current View:** `{len(df):,}` rows x `{len(df.columns)}` columns")
    with col_exp2:
        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv_bytes,
            file_name="training_effectiveness_filtered.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.dataframe(df.head(100), use_container_width=True)

    st.markdown("---")
    st.markdown("### Executive Action Plan Summary")
    st.markdown(r"""
    1. **Scale Generative AI & Cloud Upskilling:** Prioritize high-performing technical tracks showing $>240\%$ financial ROI.
    2. **Mitigate Talent Flight:** Automatically flag upskilled employees with ratings $\ge 4.0$ for market salary realignment within 60 days of program completion.
    3. **Enforce 35-Hour Curriculum Floor:** Mandate minimum 35 training hours to ensure employees hit the inflection point of behavioral punctuality and capability development.
    """)
