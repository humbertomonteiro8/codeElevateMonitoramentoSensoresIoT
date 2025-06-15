KAFKA_TOPIC = "iot_sensors"
KAFKA_BOOTSTRAP_SERVERS = ["kafka:9092"]
KAFKA_GROUP_ID = "sensor_group"

DB_SETTINGS = {
    "host": "postgres",
    "database": "iot_data",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}
