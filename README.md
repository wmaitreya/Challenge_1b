# 🧠 Challenge 1B – Adobe India Hackathon 2025  
## Semantic Relevance Ranking System for PDF Documents  

---

## 📌 Overview

This repository contains the solution for **Challenge 1B** of the Adobe India Hackathon 2025.  
The goal is to rank PDF paragraphs based on their **semantic relevance** to a given query, using a modular pipeline with sentence embeddings and vector similarity techniques.

---

## ⚙️ System Requirements

- **Python**: >3.9  
- **Docker**: Compatible with `linux/amd64` architecture  
- **No GPU** required  
- **RAM**: ≤ 16GB  
- **Model size**: ≤ 200MB  
- **No Internet access during execution**  

---

## 📁 Project Structure


---

## 🧠 How It Works

### 1. Load Inputs
`loader.py` reads:
- PDFs from the `PDFs/` directory
- Queries from the `challenge1b_input.json` file

### 2. Vectorize Text
`vectorizer.py` uses a small-size [SentenceTransformer](https://www.sbert.net/) to embed:
- Paragraphs from the PDFs
- User queries

### 3. Rank Results
`ranker.py` computes **cosine similarity** between query embeddings and paragraph embeddings, ranking them accordingly.

### 4. Output Result
`writer.py` stores the top-k ranked paragraphs (with scores and metadata) into `challenge1b_output.json`.

---

## 🚀 Running Locally (Without Docker)

> Recommended during development

```bash
# Step 1: Create virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the pipeline
python main.py
