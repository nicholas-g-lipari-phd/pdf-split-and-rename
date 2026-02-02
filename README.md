# pdf-split-and-rename

## Requirements
 - Variables: Include variables at the top for 
   - input_pdf, 
   - num_pages (how many pages per chunk), 
   - tool_choice (either 'qpdf' or 'pdfseparate'), and 
    - value set based on environement variable PDF_TOOL. When not set, fallback to qpdf
   - an array named filenames containing the desired output names.
 - Logic: The script must calculate the total number of pages in the input PDF. It should then loop through the document, extracting a chunk of num_pages for each entry in the filenames array.
 - Validation: Ensure the number of entries in the filenames array matches the expected number of chunks (Total Pages / num_pages).
 - Commands:
   - If tool_choice is 'qpdf', use: `qpdf --empty --pages input.pdf START-END -- output.pdf`
   - If tool_choice is 'pdfseparate', use: `pdfseparate -f START -l END input.pdf output.pdf`
 - Environment: Optimize the script for a standard terminal (no GUI) and include comments explaining the range calculation logic.

# PDF Split and Rename Tool

This project provides a script to split PDF files into multiple documents and rename them according to user-defined patterns.

## Features
- Split PDF files by page ranges
- Rename output files using custom patterns
- Simple CLI usage

## Usage
1. Place your PDF file in the `input_pdfs` directory and name it `input.pdf`.
2. Run the script:
   ```bash
   python pdf_split_and_rename.py
   ```
3. The split and renamed PDFs will be saved in the `output_pdfs` directory.

## Customization
- Edit `split_ranges` and `name_pattern` in `pdf_split_and_rename.py` to change how PDFs are split and named.

## Requirements
- Python 3.7+
- PyPDF2

Install dependencies:
```bash
pip install PyPDF2
```

## Example
Splits `input.pdf` into two files:
- Pages 1-3 → `Document_1_pages_1_to_3.pdf`
- Pages 4-6 → `Document_2_pages_4_to_6.pdf`

## License
MIT
 
