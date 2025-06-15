from db_handler import insert_sensor_data

def process_message(data):
    """
    Processa a mensagem recebida do Kafka e insere no banco.
    """
    print(f"[Consumer] Recebido: {data}")
    insert_sensor_data(data)
    print("[Consumer] Dados inseridos com sucesso.")