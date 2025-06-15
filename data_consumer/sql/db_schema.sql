CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(100),
    machine_id INTEGER,
    vibration FLOAT,
    oil_level FLOAT,
    rotation_speed INTEGER,
    energy_consumption FLOAT,
    temperature FLOAT,
    pressure FLOAT,
    timestamp TIMESTAMP
);
