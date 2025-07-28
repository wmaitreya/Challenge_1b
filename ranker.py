from vectorizer import encode_text
from sklearn.metrics.pairwise import cosine_similarity

def rank_chunks(persona, job, chunks, top_k=5):
    query = f"{persona}. {job}"
    query_embedding = encode_text([query])[0]

    texts = [chunk["text"] for chunk in chunks]
    doc_embeddings = encode_text(texts)

    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

    ranked = sorted(
        zip(chunks, similarities),
        key=lambda x: x[1],
        reverse=True
    )[:top_k]

    return [item[0] for item in ranked]
