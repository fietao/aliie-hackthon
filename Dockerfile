FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 5000

# Set environment for production
ENV FLASK_DEBUG=False
ENV PORT=5000
ENV HOST=0.0.0.0

# Run application
CMD ["python", "app.py"]
