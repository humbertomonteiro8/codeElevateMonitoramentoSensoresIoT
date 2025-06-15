# data_consumer/kafka_consumer.py

from kafka import KafkaConsumer
import json
import logging
from data_consumer.consumer_settings import (
    KAFKA_TOPIC,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_GROUP_ID,
)

# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_kafka_consumer():
    """
    Cria e retorna um KafkaConsumer configurado para o tópico definido.
    """
    logger.info("Iniciando KafkaConsumer para o tópico '%s'", KAFKA_TOPIC)
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_GROUP_ID,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )
    logger.info("KafkaConsumer iniciado com sucesso.")
    return consumer