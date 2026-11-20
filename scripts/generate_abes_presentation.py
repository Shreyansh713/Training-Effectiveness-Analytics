import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

os.makedirs('docs', exist_ok=True)

# Color Palette Definitions
C_DARK = RGBColor(21, 21, 20)       # #151514
C_RED = RGBColor(165, 28, 48)       # #A51C30
C_GREY = RGBColor(127, 127, 127)    # #7F7F7F
C_LIGHT_GREY = RGBColor(217, 217, 217) # #D9D9D9
C_CARD_BG = RGBColor(244, 241, 241) # #F4F1F1
C_WHITE = RGBColor(255, 255, 255)   # #FFFFFF
C_PINK = RGBColor(252, 232, 236)    # #FCE8EC

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(5.625)
    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Helper: Set Background
    def set_slide_background(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    # Helper: Add Standard Header & Footer
    def add_light_header_footer(slide, title_text):
        set_slide_background(slide, C_WHITE)
        # Title
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9.0), Inches(0.6))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Georgia"
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = C_RED

        # Footer Left
        f_left = slide.shapes.add_textbox(Inches(0.5), Inches(5.1), Inches(5.0), Inches(0.3))
        tf_l = f_left.text_frame
        p_l = tf_l.paragraphs[0]
        p_l.text = "D26 - Training Effectiveness Data Analysis"
        p_l.font.name = "Calibri"
        p_l.font.size = Pt(10)
        p_l.font.color.rgb = C_RED

        # Footer Right
        f_right = slide.shapes.add_textbox(Inches(5.5), Inches(5.1), Inches(4.0), Inches(0.3))
        tf_r = f_right.text_frame
        p_r = tf_r.paragraphs[0]
        p_r.text = "Shreyansh | Roll No: 2300320140045"
        p_r.alignment = PP_ALIGN.RIGHT
        p_r.font.name = "Calibri"
        p_r.font.size = Pt(10)
        p_r.font.color.rgb = C_GREY

    # Helper: Add Badge Card
    def add_badge_card(slide, x, y, w, h, badge_txt, head_txt, body_txt):
        # Card shape
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BG

        # Badge shape (circle)
        badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.2), Inches(y + 0.2), Inches(0.42), Inches(0.42))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_RED
        badge.line.fill.background()
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = badge_txt
        p_b.alignment = PP_ALIGN.CENTER
        p_b.font.name = "Calibri"
        p_b.font.size = Pt(12)
        p_b.font.bold = True
        p_b.font.color.rgb = C_WHITE

        # Head text
        head_box = slide.shapes.add_textbox(Inches(x + 0.75), Inches(y + 0.17), Inches(w - 0.9), Inches(0.45))
        tf_h = head_box.text_frame
        tf_h.word_wrap = True
        p_h = tf_h.paragraphs[0]
        p_h.text = head_txt
        p_h.font.name = "Calibri"
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = C_DARK

        # Body text
        body_box = slide.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.72), Inches(w - 0.4), Inches(h - 0.85))
        tf_bd = body_box.text_frame
        tf_bd.word_wrap = True
        p_bd = tf_bd.paragraphs[0]
        p_bd.text = body_txt
        p_bd.font.name = "Calibri"
        p_bd.font.size = Pt(11)
        p_bd.font.color.rgb = C_DARK

    # Helper: Add Plain Card
    def add_plain_card(slide, x, y, w, h, head_txt, body_txt):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BG

        head_box = slide.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.17), Inches(w - 0.35), Inches(0.45))
        tf_h = head_box.text_frame
        tf_h.word_wrap = True
        p_h = tf_h.paragraphs[0]
        p_h.text = head_txt
        p_h.font.name = "Calibri"
        p_h.font.size = Pt(14)
        p_h.font.bold = True
        p_h.font.color.rgb = C_DARK

        body_box = slide.shapes.add_textbox(Inches(x + 0.2), Inches(y + 0.72), Inches(w - 0.4), Inches(h - 0.85))
        tf_bd = body_box.text_frame
        tf_bd.word_wrap = True
        p_bd = tf_bd.paragraphs[0]
        p_bd.text = body_txt
        p_bd.font.name = "Calibri"
        p_bd.font.size = Pt(11)
        p_bd.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 1: DARK COVER
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, C_DARK)
    
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(8.4), Inches(1.5))
    tf1 = t_box.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "D26 - Training Effectiveness Data Analysis"
    p1.font.name = "Georgia"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Quantifying Workforce Competency Uplift & L&D Capital ROI"
    p1_sub.font.name = "Calibri"
    p1_sub.font.size = Pt(18)
    p1_sub.font.color.rgb = C_PINK

    b_box = s1.shapes.add_textbox(Inches(0.8), Inches(3.6), Inches(8.4), Inches(1.2))
    tf1_b = b_box.text_frame
    p1_det = tf1_b.paragraphs[0]
    p1_det.text = "Shreyansh | Roll No: 2300320140045 / MCA 2nd Year Data Analyst"
    p1_det.font.name = "Calibri"
    p1_det.font.size = Pt(14)
    p1_det.font.color.rgb = C_WHITE

    p1_men = tf1_b.add_paragraph()
    p1_men.text = "Mentor: Dr. R. K. Sharma | ABES Engineering College, Ghaziabad | November 2026"
    p1_men.font.name = "Calibri"
    p1_men.font.size = Pt(12)
    p1_men.font.color.rgb = C_PINK

    s1.notes_slide.notes_text_frame.text = "Good morning esteemed evaluators. I am Shreyansh, presenting project D26, Training Effectiveness Data Analysis. This analytics solution empowers corporate leadership to quantify real employee competency uplifts and optimize annual training investments."

    # =========================================================================
    # SLIDE 2: Problem and How Might We
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s2, "Problem and How Might We")

    add_badge_card(s2, 0.5, 1.25, 4.3, 3.7, "P", "Problem Statement", 
                   "Enterprise organizations spend over ₹14.9 Crores annually on corporate training without empirical data demonstrating whether programs improve performance appraisals, justify costs, or reduce turnover.\n\nWithout empirical validation, leadership risks funding obsolete curricula while losing top talent.")

    add_badge_card(s2, 5.2, 1.25, 4.3, 1.75, "1", "HMW-01: Performance Gain", 
                   "How might we quantify the exact performance rating gain attributable to training programs for executive leadership so that L&D capital allocation is empirically justified?")

    add_badge_card(s2, 5.2, 3.2, 4.3, 1.75, "2", "HMW-02: Program ROI Ranking", 
                   "How might we benchmark and rank training programs by net productivity uplift per rupee spent for L&D managers so that underperforming vendor curricula can be retired?")

    s2.notes_slide.notes_text_frame.text = "Organizations allocate substantial capital into employee development, yet lack quantitative verification of performance impact. Our two core HMW questions focus on proving statistical performance gains and benchmarking program ROI."

    # =========================================================================
    # SLIDE 3: Stakeholders and users
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s3, "Stakeholders and users")

    add_badge_card(s3, 0.5, 1.35, 2.85, 3.5, "1", "Primary: CHRO", 
                   "Role & Need:\nRequires macro ROI summaries, flight risk mitigation insights, and executive budget allocation intelligence.\n\nInfluence: High")

    add_badge_card(s3, 3.55, 1.35, 2.85, 3.5, "2", "Secondary: L&D Lead", 
                   "Role & Need:\nRequires curriculum efficacy benchmarking, delivery mode comparisons, and instructor feedback analysis.\n\nInfluence: High")

    add_badge_card(s3, 6.6, 1.35, 2.85, 3.5, "3", "Mentor / Evaluator", 
                   "Role & Need:\nRequires statistical hypothesis rigor (paired t-test, Cohen's d), robust data modeling, and clean Python architecture.\n\nInfluence: High")

    s3.notes_slide.notes_text_frame.text = "Our solution serves three primary personas: the executive CHRO deciding budget allocations, the L&D program manager curating high-impact curricula, and the academic mentor assessing statistical validity."

    # =========================================================================
    # SLIDE 4: Requirements and traceability
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s4, "Requirements and traceability")

    # Table: HMW | Requirement | Priority | User story | Test | Screen
    rows, cols = 5, 6
    tbl_shape = s4.shapes.add_table(rows, cols, Inches(0.5), Inches(1.3), Inches(9.0), Inches(2.8))
    table = tbl_shape.table
    widths = [Inches(1.0), Inches(3.4), Inches(1.0), Inches(1.2), Inches(1.2), Inches(1.2)]
    for i, w in enumerate(widths):
        table.columns[i].width = w

    t_headers = ["HMW", "Requirement", "Priority", "User Story", "Test", "Screen"]
    for i, h in enumerate(t_headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_RED
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    t_rows = [
        ["HMW-01", "Calculate pre vs post rating delta by program", "Must", "US-01", "TC-F-01", "UI-01"],
        ["HMW-02", "Identify top/bottom training programs by ROI", "Must", "US-02", "TC-F-02", "UI-03"],
        ["HMW-03", "Compare delivery modes (Online, In-Person, Hybrid)", "Must", "US-03", "TC-F-03", "UI-02"],
        ["HMW-04", "Correlate post-training ratings with flight risk", "Must", "US-04", "TC-F-04", "UI-05"]
    ]
    for r_idx, r_data in enumerate(t_rows, start=1):
        for c_idx, val in enumerate(r_data):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(10)
            p.font.color.rgb = C_DARK

    ref_box = s4.shapes.add_textbox(Inches(0.5), Inches(4.3), Inches(9.0), Inches(0.35))
    p_ref = ref_box.text_frame.paragraphs[0]
    p_ref.text = "Full matrix: Project Document, section 4 (100% Traceability across all 10 OQs)"
    p_ref.font.name = "Calibri"
    p_ref.font.size = Pt(11)
    p_ref.font.italic = True
    p_ref.font.color.rgb = C_GREY

    s4.notes_slide.notes_text_frame.text = "Every design thinking HMW statement traces seamlessly to an operational requirement, an agile user story, a functional test case, and an interactive UI screen, ensuring full bidirectional traceability."

    # =========================================================================
    # SLIDE 5: Data and preparation
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s5, "Data and preparation")

    stats = [
        ("5,000", "Total Corporate Records", 0.5),
        ("18", "Engineered Features", 2.8),
        ("2024-2026", "Observation Period", 5.1),
        ("142", "Quality Issues Fixed", 7.4)
    ]
    for val, lbl, x_pos in stats:
        # Value
        v_box = s5.shapes.add_textbox(Inches(x_pos), Inches(1.2), Inches(2.1), Inches(0.8))
        pv = v_box.text_frame.paragraphs[0]
        pv.text = val
        pv.alignment = PP_ALIGN.CENTER
        pv.font.name = "Cambria"
        pv.font.size = Pt(26)
        pv.font.bold = True
        pv.font.color.rgb = C_RED

        # Label
        l_box = s5.shapes.add_textbox(Inches(x_pos), Inches(1.9), Inches(2.1), Inches(0.4))
        pl = l_box.text_frame.paragraphs[0]
        pl.text = lbl
        pl.alignment = PP_ALIGN.CENTER
        pl.font.name = "Calibri"
        pl.font.size = Pt(10)
        pl.font.color.rgb = C_GREY

    add_plain_card(s5, 0.5, 2.5, 4.3, 2.4, "Source: Enterprise HR Fact Table", 
                   "Synthetic corporate dataset generated with deliberate, realistic distributions.\n\nGrain: One record per employee training course completion, capturing baseline and post-training annual appraisal ratings, exam marks, and costs.")

    add_plain_card(s5, 5.2, 2.5, 4.3, 2.4, "Cleaning: Anomaly Rectification", 
                   "Fixed 142 deliberate data defects:\n• Outlier Capping: Clamped invalid ratings outside 1.0-5.0\n• Deduplication: Removed duplicate test submissions\n• Imputation: Replaced missing trainer ratings via department medians.")

    s5.notes_slide.notes_text_frame.text = "We analyzed 5,000 corporate records across 18 features spanning 2024 to 2026. During data engineering, we cleaned 142 deliberate quality issues including out-of-bounds appraisal scores and missing values."

    # =========================================================================
    # SLIDE 6: Solution and technology
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s6, "Solution and technology")

    pipeline_steps = [
        ("Raw Data\n(CSV / xlsx)", 0.5, False),
        ("Clean & KPIs\n(Python, pandas)", 2.35, False),
        ("Store\n(SQLite app.db)", 4.2, False),
        ("Dashboard\n(Streamlit)", 6.05, True),
        ("Deploy\n(GitHub -> Cloud)", 7.9, False)
    ]
    for text, x_pos, is_active in pipeline_steps:
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x_pos), Inches(1.4), Inches(1.6), Inches(1.2))
        box.fill.solid()
        box.fill.fore_color.rgb = C_RED if is_active else C_CARD_BG
        box.line.color.rgb = C_RED if is_active else C_CARD_BG
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = text
        p.alignment = PP_ALIGN.CENTER
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE if is_active else C_DARK

    chevrons = [2.1, 3.95, 5.8, 7.65]
    for ch_x in chevrons:
        c_box = s6.shapes.add_textbox(Inches(ch_x), Inches(1.4), Inches(0.25), Inches(1.2))
        pc = c_box.text_frame.paragraphs[0]
        pc.text = ">"
        pc.alignment = PP_ALIGN.CENTER
        pc.font.name = "Calibri"
        pc.font.size = Pt(16)
        pc.font.bold = True
        pc.font.color.rgb = C_RED

    tools_box = s6.shapes.add_textbox(Inches(0.5), Inches(3.0), Inches(9.0), Inches(0.5))
    pt = tools_box.text_frame.paragraphs[0]
    pt.text = "Tools: Python 3.12 · Streamlit · pandas · NumPy · SciPy · Plotly · SQLite3 · pytest · Tailwind CSS"
    pt.font.name = "Calibri"
    pt.font.size = Pt(12)
    pt.font.bold = True
    pt.font.color.rgb = C_DARK

    run_box = s6.shapes.add_textbox(Inches(0.5), Inches(3.6), Inches(9.0), Inches(0.5))
    pr = run_box.text_frame.paragraphs[0]
    pr.text = "Run locally: streamlit run app.py  ->  Push to GitHub  ->  Continuous Deploy to Streamlit Community Cloud"
    pr.font.name = "Calibri"
    pr.font.size = Pt(11)
    pr.font.italic = True
    pr.font.color.rgb = C_GREY

    s6.notes_slide.notes_text_frame.text = "Our software stack is entirely modern and reproducible. We extract raw data, execute cleaning and statistical pipelines in pandas and SciPy, persist in SQLite, and render interactive visuals in Streamlit."

    # =========================================================================
    # SLIDE 7: Dashboard
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s7, "Dashboard")

    # Frame placeholder / screenshot
    frame = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(1.25), Inches(5.5), Inches(3.7))
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_CARD_BG
    frame.line.color.rgb = C_LIGHT_GREY

    tf_f = frame.text_frame
    pf = tf_f.paragraphs[0]
    pf.text = "[TalentMetrics Interactive Executive Dashboard]\n\nIncludes 4 KPI Cards, Grouped Bar Charts,\nRating Distribution KDE, Leaderboards, & Simulator."
    pf.alignment = PP_ALIGN.CENTER
    pf.font.name = "Calibri"
    pf.font.size = Pt(12)
    pf.font.italic = True
    pf.font.color.rgb = C_GREY

    # Right side 4 badges
    screens_list = [
        ("1", "UI-01", "Executive Overview & KPI Banner", 1.3),
        ("2", "UI-02", "Department Spend & Participation", 2.2),
        ("3", "UI-03", "Program ROI Leaderboard", 3.1),
        ("4", "UI-05", "Flight Risk & What-If Simulator", 4.0)
    ]
    for b_num, ui_code, ui_desc, y_pos in screens_list:
        badge = s7.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.5), Inches(y_pos), Inches(0.38), Inches(0.38))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_RED
        badge.line.fill.background()
        pb = badge.text_frame.paragraphs[0]
        pb.text = b_num
        pb.alignment = PP_ALIGN.CENTER
        pb.font.name = "Calibri"
        pb.font.size = Pt(11)
        pb.font.bold = True
        pb.font.color.rgb = C_WHITE

        tbox = s7.shapes.add_textbox(Inches(7.0), Inches(y_pos - 0.05), Inches(2.5), Inches(0.42))
        pt = tbox.text_frame.paragraphs[0]
        pt.text = f"{ui_code}: {ui_desc}"
        pt.font.name = "Calibri"
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = C_DARK

    s7.notes_slide.notes_text_frame.text = "Here is the TalentMetrics dashboard. It provides four synchronized analytical views: Executive KPIs, Departmental Spend Trends, Curriculum ROI Leaderboards, and an interactive What-If Simulator."

    # =========================================================================
    # SLIDE 8: Key findings
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s8, "Key findings")

    findings = [
        ("+0.53", "Rating Uplift Gain", "Statistically validated performance appraisal delta (pre 3.12 -> post 3.65).\nEvidence: t = 47.82, p < 0.0001, Cohen's d = 1.62", 0.5),
        ("₹34.2K", "Best Cost / Uplift", "Technical Certifications achieved the lowest cost per uplift point.\nEvidence: 3x more cost-effective than general soft skills.", 3.55),
        ("48.2%", "Flight Risk in Untrained", "Untrained staff have 3.4x higher voluntary resignation probability.\nEvidence: Chi-square p < 0.001 vs 14.1% in trained cohort.", 6.6)
    ]
    for num, mean_txt, evid_txt, x_pos in findings:
        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x_pos), Inches(1.3), Inches(2.85), Inches(3.6))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_CARD_BG

        # Number
        n_box = s8.shapes.add_textbox(Inches(x_pos + 0.1), Inches(1.4), Inches(2.65), Inches(0.9))
        pn = n_box.text_frame.paragraphs[0]
        pn.text = num
        pn.alignment = PP_ALIGN.CENTER
        pn.font.name = "Cambria"
        pn.font.size = Pt(32)
        pn.font.bold = True
        pn.font.color.rgb = C_RED

        # Meaning
        m_box = s8.shapes.add_textbox(Inches(x_pos + 0.2), Inches(2.3), Inches(2.45), Inches(0.7))
        pm = m_box.text_frame.paragraphs[0]
        pm.text = mean_txt
        pm.font.name = "Calibri"
        pm.font.size = Pt(13)
        pm.font.bold = True
        pm.font.color.rgb = C_DARK

        # Evidence
        e_box = s8.shapes.add_textbox(Inches(x_pos + 0.2), Inches(3.1), Inches(2.45), Inches(1.6))
        pe = e_box.text_frame.paragraphs[0]
        pe.text = evid_txt
        pe.font.name = "Calibri"
        pe.font.size = Pt(10)
        pe.font.color.rgb = C_GREY

    s8.notes_slide.notes_text_frame.text = "Our three primary findings: First, training yielded a statistically validated +0.53 rating uplift with a huge effect size of 1.62. Second, technical programs offer the highest ROI at ₹34.2K per gain point. Third, training reduces talent flight risk from 48.2% down to 14.1%."

    # =========================================================================
    # SLIDE 9: Testing and validation
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s9, "Testing and validation")

    # Score Big Box
    sc_box = s9.shapes.add_textbox(Inches(0.5), Inches(1.4), Inches(2.6), Inches(1.0))
    psc = sc_box.text_frame.paragraphs[0]
    psc.text = "18 / 18"
    psc.alignment = PP_ALIGN.CENTER
    psc.font.name = "Cambria"
    psc.font.size = Pt(44)
    psc.font.bold = True
    psc.font.color.rgb = C_RED

    lbl_sc = s9.shapes.add_textbox(Inches(0.5), Inches(2.4), Inches(2.6), Inches(0.9))
    plsc = lbl_sc.text_frame.paragraphs[0]
    plsc.text = "100% Passed\npytest: 8 / 8  •  Manual: 10 / 10\nZero Defect Escapes"
    plsc.alignment = PP_ALIGN.CENTER
    plsc.font.name = "Calibri"
    plsc.font.size = Pt(12)
    plsc.font.color.rgb = C_GREY

    # Table on right
    rows, cols = 4, 3
    t_shape = s9.shapes.add_table(rows, cols, Inches(3.4), Inches(1.35), Inches(6.1), Inches(2.6))
    tbl = t_shape.table
    tbl.columns[0].width = Inches(1.2)
    tbl.columns[1].width = Inches(3.7)
    tbl.columns[2].width = Inches(1.2)

    headers_9 = ["Test ID", "Verification Check", "Result"]
    for i, h in enumerate(headers_9):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_RED
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    t_data_9 = [
        ["TC-T-04", "Paired t-test statistical significance (t=47.82, p < 0.0001)", "Passed"],
        ["TC-T-03", "Relational foreign key integrity & zero orphaned records", "Passed"],
        ["TC-F-10", "Role-based authentication & session state persistence", "Passed"]
    ]
    for r_idx, r_data in enumerate(t_data_9, start=1):
        for c_idx, val in enumerate(r_data):
            cell = tbl.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(10)
            p.font.color.rgb = C_DARK

    s9.notes_slide.notes_text_frame.text = "Quality assurance achieved a 100% pass rate across 18 comprehensive tests. Both functional UI checks and technical automated pytest assertions confirmed statistical accuracy, relational database integrity, and authentication security."

    # =========================================================================
    # SLIDE 10: Recommendation, limitations and next steps
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_light_header_footer(s10, "Recommendation, limitations and next steps")

    add_badge_card(s10, 0.5, 1.25, 2.85, 3.7, "R", "Recommendation", 
                   "• Reallocate 25% of generic compliance budget into high-yield Technical Certifications.\n\n• Expand Hybrid delivery channels which delivered the highest test delta (+19.2%).\n\n• Mandate skills training for high flight-risk employees.")

    add_badge_card(s10, 3.58, 1.25, 2.85, 3.7, "L", "Limitations", 
                   "• SQLite single-writer lock restricts concurrent administrative write throughput.\n\n• Simulation engine assumes linear parameter elasticity.\n\n• Assessment scores evaluate Kirkpatrick Level 2 & 3, without external market sales factors.")

    add_badge_card(s10, 6.65, 1.25, 2.85, 3.7, "N", "Next Steps", 
                   "• Migrate database tier to PostgreSQL / AWS RDS for concurrent multi-tenant writes.\n\n• Integrate non-linear machine learning random forest regressors for What-If forecasting.\n\n• Connect direct webhooks to enterprise Workday HRIS.")

    s10.notes_slide.notes_text_frame.text = "In conclusion, we recommend shifting 25% of training budget to hybrid technical programs to maximize ROI. While our current system uses SQLite and linear simulation, future iterations will adopt PostgreSQL and machine learning regression models."

    # =========================================================================
    # SLIDE 11: DARK LIVE DEMO & Q&A
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, C_DARK)

    t_box11 = s11.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(8.4), Inches(1.5))
    tf11 = t_box11.text_frame
    p11 = tf11.paragraphs[0]
    p11.text = "Live Demonstration & Q&A"
    p11.font.name = "Georgia"
    p11.font.size = Pt(32)
    p11.font.bold = True
    p11.font.color.rgb = C_WHITE

    p11_sub = tf11.add_paragraph()
    p11_sub.text = "Thank you for your time and guidance."
    p11_sub.font.name = "Calibri"
    p11_sub.font.size = Pt(18)
    p11_sub.font.color.rgb = C_PINK

    b_box11 = s11.shapes.add_textbox(Inches(0.8), Inches(3.4), Inches(8.4), Inches(1.4))
    tf11_b = b_box11.text_frame
    p11_app = tf11_b.paragraphs[0]
    p11_app.text = "Live App: https://training-effectiveness-analytics.streamlit.app"
    p11_app.font.name = "Calibri"
    p11_app.font.size = Pt(13)
    p11_app.font.color.rgb = C_WHITE

    p11_code = tf11_b.add_paragraph()
    p11_code.text = "Source Code: https://github.com/Shreyansh713/Training-Effectiveness-Analytics.git"
    p11_code.font.name = "Calibri"
    p11_code.font.size = Pt(13)
    p11_code.font.color.rgb = C_PINK

    p11_dev = tf11_b.add_paragraph()
    p11_dev.text = "Shreyansh | Roll No: 2300320140045 | ABES Engineering College"
    p11_dev.font.name = "Calibri"
    p11_dev.font.size = Pt(12)
    p11_dev.font.color.rgb = C_WHITE

    s11.notes_slide.notes_text_frame.text = "I now open the floor for live demonstration of the TalentMetrics Streamlit platform and welcome any questions from the evaluators. Thank you."

    prs.save("docs/D26_Presentation.pptx")
    print("Generated: docs/D26_Presentation.pptx")

if __name__ == "__main__":
    create_presentation()
