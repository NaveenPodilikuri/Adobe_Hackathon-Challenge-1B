
# adobe_hackathon
# Adobe Hackathon 2025 – Challenge 1B: PDF Collection Analyzer

Welcome to the solution for Challenge 1B of the Adobe India Hackathon 2025!  
This challenge focuses on analyzing a set of PDF documents based on prompts defined in structured JSON input files. The goal is to extract meaningful insights and answers from the content and output them in a clean, organized JSON format.

This tool is built entirely using Python and can process multiple collections efficiently using pretrained NLP models.

---

##  What It Does

For each collection, the system:
- Extracts text from all PDFs in the folder.
- Reads a structured JSON file with prompt-based questions.
- Uses Sentence Transformers to embed and match content.
- Outputs summarized answers for each query into a JSON file.

---

##  Input &  Output

 Input:
- Each Collection folder should contain:
  - A PDFs/ subfolder containing relevant PDFs.
  - challenge1b_input.json with the query list.

 Output:
- For each collection, the script generates:
  - challenge1b_output.json with extracted answers.

 Sample input.json format:
```json
{
  "queries": [
    { "query": "What are the main cities to visit?", "type": "extractive" },
    { "query": "Give a summary of cultural attractions.", "type": "summary" }
  ]
}
````

 Sample output.json format:

```json
{
  "responses": [
    { "query": "What are the main cities to visit?", "response": "Paris, Lyon, Nice." },
    { "query": "Give a summary of cultural attractions.", "response": "The South of France is rich in cultural experiences..." }
  ]
}
```

---

##  How to Use

 Prerequisites

* Python 3.10 or higher
* Install required Python libraries:

```bash
pip install -r requirements.txt
```

 Run the Script

```bash
python extract_analyze.py
```

The script will process each Collection folder in the directory, read the PDFs, parse the input JSON, and generate output JSON.

---

##  Project Structure

```
.
├── extract_analyze.py              # Main Python script
├── requirements.txt                # Python dependencies
├── Collection 1/
│   ├── PDFs/
│   │   └── *.pdf                   # Input PDFs
│   ├── challenge1b_input.json      # Input prompts
│   └── challenge1b_output.json     # Output responses
├── Collection 2/
│   └── ...                         # Same structure as above
└── Collection 3/
    └── ...                         # More collections if any
```

---

##  Dependencies

* PyMuPDF (for reading PDFs)
* sentence-transformers (for embeddings)
* transformers (for summarization)
* torch

Manual install:

bash
pip install pymupdf sentence-transformers transformers torch


 Notes

* Device defaults to CPU (modify extract\_analyze.py to enable GPU if available).
* Make sure all PDF file names in input match actual files in PDFs/ folder.
* Outputs are written in the same Collection folder as the input.

