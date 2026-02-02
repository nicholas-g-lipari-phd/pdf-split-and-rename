import os
import subprocess
import sys
from PyPDF2 import PdfReader

# ===== Configuration Variables =====
# Input PDF file path
input_pdf = 'input_pdfs/input.pdf'

# Number of pages per chunk
num_pages = 3

# Tool choice: either 'qpdf' or 'pdfseparate'
# Set based on environment variable PDF_TOOL, defaults to 'qpdf' if not set
tool_choice = os.environ.get('PDF_TOOL', 'qpdf')

# Output filenames array - must match expected number of chunks
filenames = [
    'output_pdfs/Document_1.pdf',
    'output_pdfs/Document_2.pdf',
    'output_pdfs/Document_3.pdf'
]

# ===== Directory Setup =====
os.makedirs('input_pdfs', exist_ok=True)
os.makedirs('output_pdfs', exist_ok=True)


def get_total_pages(pdf_path):
    """
    Calculate the total number of pages in the input PDF.
    
    Args:
        pdf_path (str): Path to the input PDF file.
    
    Returns:
        int: Total number of pages in the PDF.
    """
    reader = PdfReader(pdf_path)
    return len(reader.pages)


def validate_configuration(total_pages, num_pages, filenames):
    """
    Validate that the number of filenames matches the expected number of chunks.
    
    Args:
        total_pages (int): Total number of pages in the PDF.
        num_pages (int): Pages per chunk.
        filenames (list): Array of output filenames.
    
    Raises:
        ValueError: If the configuration is invalid.
    """
    expected_chunks = (total_pages + num_pages - 1) // num_pages  # Ceiling division
    actual_chunks = len(filenames)
    
    if actual_chunks != expected_chunks:
        raise ValueError(
            f"Configuration mismatch: Expected {expected_chunks} chunks "
            f"({total_pages} pages / {num_pages} pages per chunk), "
            f"but got {actual_chunks} filenames."
        )


def split_pdf_qpdf(input_pdf, start_page, end_page, output_pdf):
    """
    Split PDF using qpdf command-line tool.
    
    Args:
        input_pdf (str): Path to input PDF.
        start_page (int): Starting page (1-based, inclusive).
        end_page (int): Ending page (1-based, inclusive).
        output_pdf (str): Path to output PDF.
    """
    cmd = ['qpdf', '--empty', '--pages', input_pdf, f'{start_page}-{end_page}', '--', output_pdf]
    subprocess.run(cmd, check=True)


def split_pdf_pdfseparate(input_pdf, start_page, end_page, output_pdf):
    """
    Split PDF using pdfseparate command-line tool.
    
    Args:
        input_pdf (str): Path to input PDF.
        start_page (int): Starting page (1-based, inclusive).
        end_page (int): Ending page (1-based, inclusive).
        output_pdf (str): Path to output PDF.
    """
    cmd = ['pdfseparate', '-f', str(start_page), '-l', str(end_page), input_pdf, output_pdf]
    subprocess.run(cmd, check=True)


def split_and_rename():
    """
    Main function to split PDF into chunks and rename according to filenames array.
    """
    # Check if input PDF exists
    if not os.path.exists(input_pdf):
        print(f"Error: Input PDF '{input_pdf}' not found.")
        print(f"Please place your PDF in the input_pdfs directory.")
        sys.exit(1)
    
    # Calculate total pages in the input PDF
    total_pages = get_total_pages(input_pdf)
    print(f"Total pages in input PDF: {total_pages}")
    
    # Validate configuration
    try:
        validate_configuration(total_pages, num_pages, filenames)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Select split function based on tool_choice
    if tool_choice == 'qpdf':
        split_func = split_pdf_qpdf
    elif tool_choice == 'pdfseparate':
        split_func = split_pdf_pdfseparate
    else:
        print(f"Error: Invalid tool_choice '{tool_choice}'. Must be 'qpdf' or 'pdfseparate'.")
        sys.exit(1)
    
    print(f"Using tool: {tool_choice}")
    
    # Loop through the document, extracting chunks
    for i, output_filename in enumerate(filenames):
        # Calculate page range for this chunk
        # Start page: i * num_pages + 1 (1-based indexing)
        # End page: min((i + 1) * num_pages, total_pages)
        start_page = i * num_pages + 1
        end_page = min((i + 1) * num_pages, total_pages)
        
        print(f"Creating {output_filename} (pages {start_page}-{end_page})...")
        
        try:
            split_func(input_pdf, start_page, end_page, output_filename)
            print(f"✓ Created: {output_filename}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to create {output_filename}: {e}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"✗ Error: {tool_choice} command not found. Please install {tool_choice}.")
            sys.exit(1)
    
    print(f"\nSuccessfully split {input_pdf} into {len(filenames)} files.")


if __name__ == "__main__":
    split_and_rename()
