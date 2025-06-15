# sensor_producer/main_producer.py

import time
from fake_data_generator import generate_sensor_data
from kafka_sender import create_producer, send_data


def main():
    print("[Producer] Inicializando...")
    producer = create_producer()

    print("[Producer] Enviando dados ao Kafka...")
    while True:
        data = generate_sensor_data()
        send_data(producer, data)
        print(f"[Producer] Enviado: {data}")
        time.sleep(2)


if __name__ == "__main__":
    time.sleep(60)  # Espera 60 segundos antes de começar a gerar os dados
    main()
