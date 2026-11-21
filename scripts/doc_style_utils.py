import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

COLOR_RED = RGBColor(165, 28, 48)     # #A51C30
COLOR_DARK = RGBColor(21, 21, 20)     # #151514
COLOR_GREY = RGBColor(127, 127, 127)  # #7F7F7F
HEX_RED = "A51C30"
HEX_BORDER = "BFBFBF"
HEX_LIGHT_ROW = "F9FAFB"

def setup_page(doc, learner="Shreyansh", roll_no="2500320140140", project_id="D26", title="Project Document"):
    section = doc.sections[0]
    section.top_margin = Inches(0.7874)     # 2 cm
    section.bottom_margin = Inches(0.7874)  # 2 cm
    section.left_margin = Inches(0.7874)    # 2 cm
    section.right_margin = Inches(0.7874)   # 2 cm
    section.header_distance = Inches(0.492) # 1.25 cm
    section.footer_distance = Inches(0.492) # 1.25 cm
    section.page_width = Inches(8.267)      # A4
    section.page_height = Inches(11.692)    # A4

    # Setup header
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.text = f"ABES Engineering College | {title} | {project_id}"
    for run in hp.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(8)
        run.font.color.rgb = COLOR_GREY

    # Setup footer
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.text = f"{learner} | Roll No: {roll_no}   •   ABES Engineering College"
    for run in fp.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(8)
        run.font.color.rgb = COLOR_GREY

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(7)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Georgia"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_RED
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Georgia"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Georgia"
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_RED
    return p

def add_body_p(doc, text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_DARK
    r_body = p.add_run(text)
    r_body.font.name = "Calibri"
    r_body.font.size = Pt(10)
    r_body.font.italic = italic
    r_body.font.color.rgb = COLOR_DARK
    return p

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.1
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_DARK
    r_body = p.add_run(text)
    r_body.font.name = "Calibri"
    r_body.font.size = Pt(10)
    r_body.font.color.rgb = COLOR_DARK
    return p

def add_callout(doc, text, title="NOTE"):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Inches(0.2)
    r_title = p.add_run(f"[{title}] ")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(9.5)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_RED
    r_text = p.add_run(text)
    r_text.font.name = "Calibri"
    r_text.font.size = Pt(9.5)
    r_text.font.italic = True
    r_text.font.color.rgb = COLOR_GREY
    return p

def set_cell_properties(cell, fill_hex=None, top_padding=60, bottom_padding=60, left_padding=90, right_padding=90):
    tcPr = cell._tc.get_or_add_tcPr()
    # Padding
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top_padding), ('w:bottom', bottom_padding), ('w:left', left_padding), ('w:right', right_padding)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)
    
    # Fill
    if fill_hex:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)
        
    # Borders
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>\n'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def format_table(table, col_widths_dxa, headers, rows_data):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Setup Header Row
    hdr_cells = table.rows[0].cells
    hdr_trPr = table.rows[0]._tr.get_or_add_trPr()
    hdr_trPr.append(OxmlElement('w:tblHeader'))
    hdr_trPr.append(OxmlElement('w:cantSplit'))
    
    for i, title in enumerate(headers):
        cell = hdr_cells[i]
        cell.width = col_widths_dxa[i]
        set_cell_properties(cell, fill_hex=HEX_RED, top_padding=70, bottom_padding=70)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(title)
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    # Setup Body Rows
    for r_idx, row_data in enumerate(rows_data):
        row = table.add_row()
        row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        bg_fill = HEX_LIGHT_ROW if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = col_widths_dxa[c_idx]
            set_cell_properties(cell, fill_hex=bg_fill)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.05
            run = p.add_run(str(val))
            run.font.name = "Calibri"
            run.font.size = Pt(8.5)
            run.font.color.rgb = COLOR_DARK
