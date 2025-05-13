import pytesseract
from pdf2image import convert_from_path
from docx import Document

# Paths
pdf_path = 'UNICF concept Template.pdf'
docx_path = 'output.docx'

# Convert PDF to images
pages = convert_from_path(pdf_path)

# Create a Word document
doc = Document()

# OCR each page image and add text to doc
for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page)
    doc.add_paragraph(text)
    doc.add_page_break()

# Save the Word file
doc.save(docx_path)

print(f"OCR complete. Saved as {docx_path}")
