# Extract Text from PDF with Python
# pip install PyPDF2

import PyPDF2

pdf_path = "anyPDFfile.pdf"

with open(pdf_path, mode="rb") as pdf:
    reader = PyPDF2.PdfReader(pdf)
    page = reader.pages[0]  # Use square brackets instead of parentheses
    text = page.extract_text()
    print(text)