# sensor_producer/main_producer.py

import time
import logging
from fake_data_generator import generate_sensor_data
from kafka_sender import create_producer, send_data

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("sensor_producer")

def main():
    logger.info("Inicializando...")
    producer = create_producer()

    logger.info("Enviando dados ao Kafka...")
    while True:
        data = generate_sensor_data()
        send_data(producer, data)
        logger.info(f"Enviado: {data}")
        time.sleep(2)

if __name__ == "__main__":
    time.sleep(60)  # Espera 60 segundos antes de começar a gerar os dados
    main()
