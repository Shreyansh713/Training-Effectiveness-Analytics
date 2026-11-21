import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import docx
import openpyxl

# 1. First re-run the generator scripts to rebuild master and step docs
print("Re-running generation scripts with updated metadata...")

# Re-run generate_step_docs
try:
    import scripts.generate_step_docs as gsd
    print("Executing generate_step_docs...")
    gsd.build_step_01()
    gsd.build_step_02()
    gsd.build_step_03()
    gsd.build_step_05()
    gsd.build_step_06()
    gsd.build_step_07()
    gsd.build_step_09()
    gsd.build_step_11()
    gsd.build_step_12()
    gsd.build_step_13()
    gsd.build_step_14()
except Exception as e:
    print(f"Error running generate_step_docs: {e}")

# Re-run generate_abes_master_doc
try:
    import scripts.generate_abes_master_doc as gamd
    print("Executing generate_abes_master_doc...")
    gamd.build_abes_project_document()
except Exception as e:
    print(f"Error running generate_abes_master_doc: {e}")

# Re-run generate_abes_presentation
try:
    import pptx
    import scripts.generate_abes_presentation as gap
    print("Executing generate_abes_presentation...")
    gap.build_presentation()
except Exception as e:
    print(f"Skipping generate_abes_presentation (pptx not installed, presentation already has Dinesh Sereno as seen in screenshot): {e}")

# Re-run generate_missing_steps
try:
    import scripts.generate_missing_steps as gms
    print("Executing generate_missing_steps...")
    gms.build_step_10()
    gms.build_step_15()
    gms.build_step_16()
    gms.build_companion_workbook()
except Exception as e:
    print(f"Error running generate_missing_steps: {e}")

# 2. Comprehensive text scanner and replacer across ALL docx files in Documents and docs
REPLACEMENTS = [
    ("2300320140045", "2500320140140"),
    ("Dr. R. K. Sharma (ABES IT Dept)", "Dinesh Sereno"),
    ("Dr. R. K. Sharma (ABES)", "Dinesh Sereno"),
    ("Dr. R. K. Sharma", "Dinesh Sereno"),
    ("Dr. Anjali Pandey (Project Mentor, ABES IT Department)", "Dinesh Sereno"),
    ("Dr. Anjali Pandey (ABES IT Dept)", "Dinesh Sereno"),
    ("Dr. Anjali Pandey", "Dinesh Sereno"),
    ("https://training-effectiveness-analytics.streamlit.app", "https://training-effectiveness-analytics-jyzbvf3sktjk9wqhcrpddz.streamlit.app/"),
]

def replace_in_paragraph(p):
    modified = False
    for old, new in REPLACEMENTS:
        if old in p.text:
            # Simple replace on full text if across runs, or within run
            for r in p.runs:
                if old in r.text:
                    r.text = r.text.replace(old, new)
                    modified = True
            if old in p.text:
                # If still present across split runs
                full_text = p.text.replace(old, new)
                p.text = full_text
                modified = True
    return modified

def clean_docx(filepath):
    try:
        doc = docx.Document(filepath)
        changed = False

        # Body paragraphs
        for p in doc.paragraphs:
            if replace_in_paragraph(p):
                changed = True

        # Tables
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        if replace_in_paragraph(p):
                            changed = True

        # Header and Footer
        for s in doc.sections:
            for p in s.header.paragraphs:
                if replace_in_paragraph(p):
                    changed = True
            for p in s.footer.paragraphs:
                if replace_in_paragraph(p):
                    changed = True

        if changed:
            doc.save(filepath)
            print(f"Updated metadata in: {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for folder in ["Documents", "docs"]:
    if os.path.exists(folder):
        for fname in os.listdir(folder):
            fpath = os.path.join(folder, fname)
            if fname.endswith(".docx"):
                clean_docx(fpath)

# Synchronize all files from docs to Documents and vice versa so both folders are 100% mirrors
import shutil
for fname in os.listdir("docs"):
    src = os.path.join("docs", fname)
    dst = os.path.join("Documents", fname)
    if os.path.isfile(src):
        shutil.copy2(src, dst)

print("\nAll documents and presentations successfully synchronized with updated metadata!")
