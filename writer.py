import json
from datetime import datetime
from config import OUTPUT_JSON

def write_output(input_data, top_chunks):
    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": input_data["persona"]["role"],
            "job_to_be_done": input_data["job_to_be_done"]["task"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for i, chunk in enumerate(top_chunks, 1):
        output["extracted_sections"].append({
            "document": chunk["document"],
            "section_title": chunk["title"],
            "importance_rank": i,
            "page_number": chunk["page"]
        })
        output["subsection_analysis"].append({
            "document": chunk["document"],
            "refined_text": chunk["text"],
            "page_number": chunk["page"]
        })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[INFO] Output written to {OUTPUT_JSON}")
