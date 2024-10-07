import PyPDF2

def extract_text(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

    return pdf_text

if __name__ == '__main__':
    extracted_text = extract_text('TestOCR.pdf')
    for text in extracted_text:
        print(text)