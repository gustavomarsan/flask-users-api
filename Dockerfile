# Use official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements first (better caching)
COPY requirements/base.txt .

RUN pip install --no-cache-dir -r base.txt

# Copy the rest of the application
COPY . .

# Expose the API port
EXPOSE 5000

# Start the app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]


