import logging
from kafka_consumer import start_kafka_consumer
from consumer_utils import process_message
import time

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    consumer = start_kafka_consumer()
    logger.info("Aguardando mensagens no tópico...")

    try:
        for message in consumer:
            process_message(message.value)
    except KeyboardInterrupt:
        logger.info("Encerrado manualmente.")
    finally:
        consumer.close()

if __name__ == "__main__":
    time.sleep(60)  # Espera 60 segundos antes de consumir os dados gerados pelo producer
    main()
