#!/usr/bin/env python3
"""Generate a formatted PDF of التربة السوداء for competition submission."""

import markdown
from weasyprint import HTML

# Read the markdown file
with open("التربة_السوداء_النسخة_النهائية.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown to HTML
html_body = markdown.markdown(md_content, extensions=["extra"])

# Full HTML with CSS for Arabic RTL formatting
html_full = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<style>
@page {{
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @bottom-center {{
        content: counter(page);
        font-size: 10pt;
        color: #666;
    }}
}}

body {{
    font-family: FreeSerif, DejaVu Sans, serif;
    font-size: 14pt;
    line-height: 2;
    direction: rtl;
    text-align: justify;
    color: #1a1a1a;
}}

h1 {{
    font-size: 28pt;
    text-align: center;
    margin-top: 8cm;
    margin-bottom: 0.5cm;
    color: #000;
    page-break-after: avoid;
}}

h2 {{
    font-size: 18pt;
    text-align: center;
    margin-bottom: 4cm;
    color: #333;
    font-weight: normal;
}}

hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 2cm auto;
    width: 30%;
    page-break-after: always;
}}

p {{
    text-indent: 1cm;
    margin: 0.3cm 0;
    orphans: 3;
    widows: 3;
}}

/* Section markers */
p:first-of-type {{
    text-indent: 0;
}}

/* Style for section numbers like · ١ · */
p {{
    break-inside: avoid-orphan;
}}

/* Make the title page centered */
h1 + h2 {{
    page-break-after: always;
}}

/* Ensure good paragraph spacing */
p + p {{
    margin-top: 0.2cm;
}}

/* Style dialogue and emphasis */
em {{
    font-style: normal;
    border-bottom: 1px dotted #999;
}}

strong {{
    font-weight: bold;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

# Generate PDF
HTML(string=html_full).write_pdf("التربة_السوداء.pdf")
print("تم إنشاء الملف: التربة_السوداء.pdf")
