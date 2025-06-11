FROM python:3.13-alpine
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create writable directory for SQLite
RUN mkdir -p /app/instance && chmod -R 777 /app/instance

# Copy app files
COPY . .
EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["python", "main.py"]
