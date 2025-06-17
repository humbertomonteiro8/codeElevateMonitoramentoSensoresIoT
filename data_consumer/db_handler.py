import psycopg2
from psycopg2.extras import RealDictCursor
from data_consumer.consumer_settings import DB_SETTINGS
import logging

# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect():
    return psycopg2.connect(**DB_SETTINGS)

def insert_sensor_data(data):
    conn = connect()
    cursor = conn.cursor()
    insert_query = (
        "INSERT INTO sensor_data ("
        "sensor_id, machine_id, vibration, oil_level, rotation_speed, "
        "energy_consumption, temperature, pressure, timestamp"
        ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    )
    values = (
        data['sensor_id'],
        data['machine_id'],
        data['vibration'],
        data['oil_level'],
        data['rotation_speed'],
        data['energy_consumption'],
        data['temperature'],
        data['pressure'],
        data['timestamp'],
    )
    try:
        cursor.execute(insert_query, values)
        conn.commit()
        logger.info("Dados inseridos com sucesso para o sensor_id %s", data['sensor_id'])
    except Exception as e:
        logger.error("Erro ao inserir dados: %s", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
