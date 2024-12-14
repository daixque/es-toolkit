from pypdf import PdfReader
import os

# Extract text from pdf
# Return a string of all text in the pdf
def extract_all_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    contents = ""
    for page in reader.pages:
        contents += page.extract_text()
    return contents

# Extract text from pdf by page
# Return a list of text, each element is the text of a page
def extract_text_from_pdf_by_page(pdf_path):
    reader = PdfReader(pdf_path)
    contents = []
    for page in reader.pages:
        contents.append(page.extract_text())
    return contents

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(current_path, "../../../resources/pdf", "ja_vector_search_en.pdf")
    text = extract_all_text_from_pdf(filepath)
    print(text)