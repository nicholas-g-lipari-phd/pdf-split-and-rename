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

A flexible Python script that splits PDF files into multiple documents based on configurable page chunks and renames them according to a specified array of filenames.

## Features
- Split PDF files by configurable page chunk size
- Uses external command-line tools (`qpdf` or `pdfseparate`) for reliable PDF processing
- Tool selection via environment variable (`PDF_TOOL`)
- Automatic validation of configuration (ensures filenames match expected chunks)
- Clear error messages and progress feedback

## Installation

### Python Dependencies
```bash
pip install PyPDF2
```

### External Tools
Install either `qpdf` (default) or `pdfseparate`:

**qpdf:**
- Windows: `choco install qpdf` or download from [qpdf.sourceforge.io](https://qpdf.sourceforge.io/)
- Linux: `sudo apt-get install qpdf`
- macOS: `brew install qpdf`

**pdfseparate (part of poppler-utils):**
- Windows: Download from [poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)
- Linux: `sudo apt-get install poppler-utils`
- macOS: `brew install poppler`

## Usage

1. **Configure the script** by editing variables at the top of `pdf_split_and_rename.py`:
   ```python
   input_pdf = 'input_pdfs/input.pdf'  # Path to your input PDF
   num_pages = 3                        # Pages per chunk
   filenames = [                        # Output filenames
       'output_pdfs/Document_1.pdf',
       'output_pdfs/Document_2.pdf',
       'output_pdfs/Document_3.pdf'
   ]
   ```

2. **Place your PDF** in the `input_pdfs` directory (or update `input_pdf` variable).

3. **Run the script:**
   ```bash
   python pdf_split_and_rename.py
   ```

4. **Optional: Choose tool** via environment variable:
   ```bash
   # Use qpdf (default)
   python pdf_split_and_rename.py
   
   # Use pdfseparate
   set PDF_TOOL=pdfseparate    # Windows
   export PDF_TOOL=pdfseparate # Linux/macOS
   python pdf_split_and_rename.py
   ```

## How It Works

1. **Page Calculation:** Reads the total number of pages from the input PDF
2. **Validation:** Ensures the `filenames` array length matches `total_pages / num_pages`
3. **Chunk Extraction:** Loops through the document, extracting `num_pages` per chunk
4. **Page Range Logic:**
   - Chunk `i` starts at page: `i * num_pages + 1` (1-based)
   - Chunk `i` ends at page: `min((i + 1) * num_pages, total_pages)`
5. **Tool Execution:** Calls the selected tool (`qpdf` or `pdfseparate`) to split and save

## Example

For a 9-page PDF with `num_pages = 3`:
- Total chunks: 9 ÷ 3 = 3
- Required filenames: 3 entries
- Output:
  - `Document_1.pdf` → pages 1-3
  - `Document_2.pdf` → pages 4-6
  - `Document_3.pdf` → pages 7-9

## Troubleshooting

**"Configuration mismatch" error:**
- Ensure your `filenames` array has the correct number of entries
- Expected chunks = `ceil(total_pages / num_pages)`

**"command not found" error:**
- Install the required tool (`qpdf` or `pdfseparate`)
- Ensure it's in your system PATH

## License
MIT
 
