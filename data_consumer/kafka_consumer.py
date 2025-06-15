# data_consumer/kafka_consumer.py

from kafka import KafkaConsumer
import json
from data_consumer.consumer_settings import (
    KAFKA_TOPIC,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_GROUP_ID,
)


def start_kafka_consumer():
    """
    Cria e retorna um KafkaConsumer configurado para o tópico definido.
    """
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )
    return consumer