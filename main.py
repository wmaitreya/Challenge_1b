from loader import load_input_json, extract_text_chunks
from ranker import rank_chunks
from writer import write_output

def main():
    print("[INFO] Loading input...")
    input_data = load_input_json()
    documents = input_data["documents"]
    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]

    print("[INFO] Extracting text from PDFs...")
    chunks = extract_text_chunks(documents)

    print("[INFO] Ranking relevant sections...")
    top_chunks = rank_chunks(persona, job, chunks)

    print("[INFO] Writing output JSON...")
    write_output(input_data, top_chunks)

if __name__ == "__main__":
    main()
