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
 