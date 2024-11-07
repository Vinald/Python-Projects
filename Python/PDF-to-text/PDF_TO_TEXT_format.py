from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Save the extracted text in a text file
    output_file = pdf_file.replace('.pdf', '.txt')
    with open(output_file, 'w') as file:
        file.write(text)

    return text


pdf_file = 'sample.pdf'
print(extract_text_from_pdf(pdf_file))