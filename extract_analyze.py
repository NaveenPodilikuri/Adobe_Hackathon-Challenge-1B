import os
import json
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# Load models
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def load_input_json(input_path):
    with open(input_path, 'r') as f:
        return json.load(f)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        sections.append((page_num + 1, text.strip()))
    return sections

def compute_similarity(texts, query):
    embeddings = embedding_model.encode(texts + [query], convert_to_tensor=True)
    similarities = util.cos_sim(embeddings[:-1], embeddings[-1])
    scores = similarities.squeeze(1).tolist()
    return scores

def summarize_text(text):
    if len(text.split()) < 50:
        return text
    return summarizer(text, max_length=120, min_length=40, do_sample=False)[0]['summary_text']

def analyze_collection(base_dir):
    input_path = os.path.join(base_dir, 'challenge1b_input.json')
    input_data = load_input_json(input_path)

    persona = input_data['persona']['role']
    task = input_data['job_to_be_done']['task']
    job_query = f"{persona}: {task}"

    extracted_sections = []
    subsection_analysis = []

    for doc in input_data['documents']:
        filename = doc['filename']
        full_path = os.path.join(base_dir, "PDFs", filename)
        sections = extract_text_from_pdf(full_path)

        texts = [text for _, text in sections]
        scores = compute_similarity(texts, job_query)

        sorted_items = sorted(zip(sections, scores), key=lambda x: x[1], reverse=True)
        for rank, ((page_num, text), score) in enumerate(sorted_items[:3], start=1):
            extracted_sections.append({
                "document": filename,
                "section_title": f"Page {page_num}",
                "importance_rank": rank,
                "page_number": page_num
            })
            refined = summarize_text(text)
            subsection_analysis.append({
                "document": filename,
                "refined_text": refined,
                "page_number": page_num
            })

    output = {
        "metadata": {
            "input_documents": [doc['filename'] for doc in input_data['documents']],
            "persona": persona,
            "job_to_be_done": task
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    output_path = os.path.join(base_dir, 'challenge1b_output.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"Output written to {output_path}")

if __name__ == "__main__":
    for i in range(1, 4):
        base = f"Collection {i}"
        print(f"\nProcessing {base}")
        analyze_collection(base)
