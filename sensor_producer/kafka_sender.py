from kafka import KafkaProducer
import json
import time

from fake_data_generator import generate_sensor_data
from producer_settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

def main():
    """Inicializa o produtor Kafka e envia dados simulados de sensores."""
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    print("[Producer] Enviando dados ao Kafka...")

    while True:
        data = generate_sensor_data()
        producer.send(KAFKA_TOPIC, value=data)
        print(f"[Producer] Enviado: {data}")
        time.sleep(2)

if __name__ == "__main__":
    time.sleep(60)  # Aguarda 60 segundos antes de iniciar o envio
    main()
