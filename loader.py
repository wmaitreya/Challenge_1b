import json
import os
from PyPDF2 import PdfReader
from config import INPUT_JSON, PDF_DIR

def load_input_json():
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_text_chunks(documents):
    chunks = []
    for doc in documents:
        filename = doc["filename"]
        title = doc["title"]
        pdf_path = os.path.join(PDF_DIR, filename)

        if not os.path.exists(pdf_path):
            print(f"[WARN] Missing PDF: {pdf_path}")
            continue

        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            raw_text = page.extract_text()
            if raw_text:
                chunk = {
                    "document": filename,
                    "title": title,
                    "page": page_num + 1,
                    "text": raw_text.strip()
                }
                chunks.append(chunk)
    return chunks
