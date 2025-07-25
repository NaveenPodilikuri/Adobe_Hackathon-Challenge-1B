
# Adobe Hackathon - Challenge 1B

This project processes PDF documents across multiple collections using a Python script to extract and summarize content as specified in the challenge prompt.

##  Folder Structure

```

CHALLENGE\_2/
│
├── Collection 1/
│   ├── PDF/
│   │   ├── South of France - Cities.pdf
│   │   ├── South of France - Cuisine.pdf
│   │   └── ... (other PDFs)
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json ⬅️ Generated after running the script
│
├── Collection 2/
│   ├── PDF/
│   │   ├── Learn Acrobat - Create and Convert\_1.pdf
│   │   └── ... (other PDFs)
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json ⬅️ Generated after running the script
│
├── Collection 3/
│   ├── PDF/
│   │   └── ... (PDF files)
│   ├── challenge1b\_input.json
│   └── challenge1b\_output.json ⬅️ Generated after running the script
│
├── extract\_analyze.py ✅ Main script
└── requirements.txt ✅ Dependencies

````

---

## 🚀 How to Run

1. **Install requirements**  
   Run this once to install dependencies:
   ```bash
   pip install -r requirements.txt
````

2. **Run the main script**

   ```bash
   python extract_analyze.py
   ```

3. **Output**

   * The script reads all PDFs inside each `Collection` folder.
   * It extracts and summarizes content based on `challenge1b_input.json`.
   * It saves the result to `challenge1b_output.json` in the same folder.

---

## Script Info

* The script uses:

  * PyMuPDF or pdfplumber for reading PDFs
  * HuggingFace Transformers for summarization
* Works on CPU
* Summarizer may log messages like: Your max_length is set to 120, but your input_length is only 106...
These are just warnings and do not affect the output.

