from kafka_consumer import start_kafka_consumer
from consumer_utils import process_message
import time


def main():
    consumer = start_kafka_consumer()
    print("[Consumer] Aguardando mensagens no tópico...")

    try:
        for message in consumer:
            process_message(message.value)
    except KeyboardInterrupt:
        print("[Consumer] Encerrado manualmente.")
    finally:
        consumer.close()


if __name__ == "__main__":
    time.sleep(60)  # Espera 60 segundos antes de consumir os dados gerados pelo producer
    main()
