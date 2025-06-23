FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies (ffmpeg, libgl1 for OpenCV)
RUN apt-get update && \
    apt-get install -y ffmpeg libgl1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn command to run Flask app
CMD ["python", "app.py"]