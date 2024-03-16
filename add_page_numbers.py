from PyPDF2 import PdfReader
import os

from pdftools import create_page_numbers_pdf, add_page_numbers_to_pdf


def main(original_pdf_path):
    # Determine the number of pages in the original PDF
    original_pdf = PdfReader(original_pdf_path)
    num_pages = len(original_pdf.pages)

    # Create a PDF with page numbers
    temp_pdf_path = "temp_page_numbers.pdf"
    create_page_numbers_pdf(num_pages, temp_pdf_path)

    # Merge the original PDF with the page numbers PDF
    output_pdf_path = "numbered_" + os.path.basename(original_pdf_path)
    add_page_numbers_to_pdf(original_pdf_path, temp_pdf_path, output_pdf_path)

    # Clean up the temporary page numbers PDF
    os.remove(temp_pdf_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pdf>")
    else:
        original_pdf_path = sys.argv[1]
        main(original_pdf_path)
