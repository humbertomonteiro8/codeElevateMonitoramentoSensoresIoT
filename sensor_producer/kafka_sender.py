# sensor_producer/kafka_sender.py

from kafka import KafkaProducer
import json

from producer_settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

def create_producer():
    """Cria e retorna um KafkaProducer configurado."""
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def send_data(producer, data):
    """Envia dados para o tópico Kafka."""
    producer.send(KAFKA_TOPIC, value=data)
    producer.flush()  # força o envio imediato
