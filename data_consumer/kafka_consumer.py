from kafka import KafkaConsumer
import json
from consumer_settings import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, KAFKA_GROUP_ID
from db_handler import insert_sensor_data

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id=KAFKA_GROUP_ID,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'
)

print("[Consumer] Aguardando mensagens no tópico...")

for message in consumer:
    data = message.value
    print(f"[Consumer] Recebido: {data}")
    insert_sensor_data(data)
