# container_setup/service_dockerfile/consumer.Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Instala dependências do sistema necessárias para o psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data_consumer/ .

CMD ["python", "main_consumer.py"]
