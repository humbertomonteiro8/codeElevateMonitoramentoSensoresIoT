import psycopg2
from psycopg2.extras import RealDictCursor
from data_consumer.consumer_settings import DB_SETTINGS


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
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()
