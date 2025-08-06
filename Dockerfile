# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency files
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port (default for Streamlit is 8501, or your app’s port)
EXPOSE 8501

# Set environment variables if needed
ENV PYTHONUNBUFFERED=1

# Run your app (adjust command if your entrypoint differs)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
