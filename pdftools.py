from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# import sys
# from PyPDF2 import PdfWriter, PdfReader

PAGE_NUMBER_X_OFFSET_IN_INCHES = 8.5 - 1
PAGE_NUMBER_Y_OFFSET_IN_INCHES = 0.2

PAGE_NUMBER_X_OFFSET_IN_POINTS = PAGE_NUMBER_X_OFFSET_IN_INCHES * 72
PAGE_NUMBER_Y_OFFSET_IN_POINTS = (PAGE_NUMBER_Y_OFFSET_IN_INCHES) * 72

LABEL_X_OFFSET_IN_INCHES = 6
LABEL_Y_OFFSET_IN_INCHES = 11 - 0.5

LABEL_X_OFFSET_IN_POINTS = LABEL_X_OFFSET_IN_INCHES * 72
LABEL_Y_OFFSET_IN_POINTS = (LABEL_Y_OFFSET_IN_INCHES) * 72


def create_page_numbers_pdf(num_pages, output_filename):
    """Create a PDF with page numbers."""
    c = canvas.Canvas(output_filename, pagesize=letter)
    for page_num in range(1, num_pages + 1):
        c.drawString(
            PAGE_NUMBER_X_OFFSET_IN_POINTS,
            PAGE_NUMBER_Y_OFFSET_IN_POINTS,
            f"page {page_num}",
        )  # Adjust positioning as needed
        c.showPage()
    c.save()


def create_labels_pdf(num_pages, label, output_filename):
    """Create a PDF with page numbers."""
    c = canvas.Canvas(output_filename, pagesize=letter)
    for _ in range(1, num_pages + 1):
        c.drawString(
            LABEL_X_OFFSET_IN_POINTS,
            LABEL_Y_OFFSET_IN_POINTS,
            label,
        )  # Adjust positioning as needed
        c.showPage()
    c.save()


def add_page_numbers_to_pdf(original_pdf_path, page_numbers_pdf_path, output_pdf_path):
    """Overlay page numbers onto the original PDF."""
    original_pdf = PdfReader(original_pdf_path)
    page_numbers_pdf = PdfReader(page_numbers_pdf_path)

    writer = PdfWriter()

    for page_num in range(len(original_pdf.pages)):
        page = original_pdf.pages[page_num]
        page_number_page = page_numbers_pdf.pages[page_num]
        page.merge_page(page_number_page)
        writer.add_page(page)

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Added page numbers to '{original_pdf_path}'. Result: '{output_pdf_path}'")
