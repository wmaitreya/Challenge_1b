import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Input paths
INPUT_JSON = os.path.join(INPUT_DIR, "challenge1b_input.json")
PDF_DIR = INPUT_DIR  # PDFs are also in the input directory

# Output path
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "challenge1b_output.json")
