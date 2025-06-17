import logging
from db_handler import insert_sensor_data

logger = logging.getLogger(__name__)

def process_message(data):
    """
    Processa a mensagem recebida do Kafka e insere no banco.
    """
    logger.info(f"[Consumer] Recebido: {data}")
    insert_sensor_data(data)
    logger.info("[Consumer] Dados inseridos com sucesso.")