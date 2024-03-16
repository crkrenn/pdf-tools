import sys
from PyPDF2 import PdfMerger

if len(sys.argv) < 3:
    print(
        "Usage: python script.py output_file.pdf input_file1.pdf [input_file2.pdf ...]"
    )
    sys.exit(1)

output_pdf = sys.argv[1]  # The first argument is the output file
pdf_files = sys.argv[2:]  # The rest of the arguments are PDF files to merge

# Confirm execution
confirmation = input(
    f"Are you sure you want to merge {len(pdf_files)} files into '{output_pdf}'? (yes/no): "
)
if confirmation.lower() != "yes":
    print("Merge cancelled.")
    sys.exit(0)

merger = PdfMerger()

for pdf in pdf_files:
    try:
        merger.append(pdf)
        print(f"Added {pdf} to the merger.")
    except FileNotFoundError:
        print(f"Error: '{pdf}' does not exist. Skipping...")
    except Exception as e:
        print(f"An error occurred while adding '{pdf}': {e}. Skipping...")

try:
    merger.write(output_pdf)
    merger.close()
    print(f"PDF files have been merged into {output_pdf}")
except Exception as e:
    print(f"Failed to merge PDFs: {e}")
    sys.exit(1)
