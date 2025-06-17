FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sensor_producer/ ./sensor_producer

ENV PYTHONPATH=/app

CMD ["python", "sensor_producer/main_producer.py"]
