import os
from PyPDF2 import PdfReader, PdfWriter

# Configuration: input/output directories
INPUT_DIR = 'input_pdfs'
OUTPUT_DIR = 'output_pdfs'

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_and_rename(pdf_path, split_ranges, name_pattern):
    """
    Splits a PDF into multiple files and renames them.
    Args:
        pdf_path (str): Path to the input PDF file.
        split_ranges (list of tuples): List of (start, end) page ranges (1-based, inclusive).
        name_pattern (str): Output file naming pattern, e.g. 'Document_{i}.pdf'.
    """
    reader = PdfReader(pdf_path)
    for i, (start, end) in enumerate(split_ranges, 1):
        writer = PdfWriter()
        for page_num in range(start-1, end):
            writer.add_page(reader.pages[page_num])
        output_name = name_pattern.format(i=i, start=start, end=end)
        output_path = os.path.join(OUTPUT_DIR, output_name)
        with open(output_path, 'wb') as f:
            writer.write(f)
        print(f"Created: {output_path}")

if __name__ == "__main__":
    # Example usage: split input.pdf into two documents, pages 1-3 and 4-6
    input_pdf = os.path.join(INPUT_DIR, 'input.pdf')
    split_ranges = [(1, 3), (4, 6)]
    name_pattern = 'Document_{i}_pages_{start}_to_{end}.pdf'
    if os.path.exists(input_pdf):
        split_and_rename(input_pdf, split_ranges, name_pattern)
    else:
        print(f"Place your PDF in {INPUT_DIR} as 'input.pdf' and rerun.")
