# Use Official Python Base Image
FROM python:3.10-slim

# Set Working Directory
WORKDIR /app

# Install System Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Project Requirements & Files
COPY . /app

# Install Python Libraries from requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Web Port 8000 and Backend API Port 5000
EXPOSE 8000 5000

# Command to Run Both Server & Web App via Python
CMD ["sh", "-c", "python server.py & python -m http.server 8000"]
