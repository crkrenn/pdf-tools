from PyPDF2 import PdfReader
import os

from pdftools import create_labels_pdf, add_page_numbers_to_pdf


def main(original_pdf_path):
    # Determine the number of pages in the original PDF
    original_pdf = PdfReader(original_pdf_path)
    num_pages = len(original_pdf.pages)

    # Create a PDF with labels
    temp_pdf_path = "temp_labels.pdf"
    create_labels_pdf(num_pages, f'document {original_pdf_path}', temp_pdf_path)

    # Merge the original PDF with the labels PDF
    output_pdf_path = "labelled_" + os.path.basename(original_pdf_path)
    add_page_numbers_to_pdf(original_pdf_path, temp_pdf_path, output_pdf_path)

    # Clean up the temporary labels PDF
    os.remove(temp_pdf_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <paths_to_pdf>")
        sys.exit(1)
    for original_pdf_path in sys.argv[1:]:
        main(original_pdf_path)

