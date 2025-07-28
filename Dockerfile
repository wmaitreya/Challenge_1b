FROM --platform=linux/amd64 python:3.11

WORKDIR /app

# Copy your requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Default command to run your script
CMD ["python", "main.py"]
