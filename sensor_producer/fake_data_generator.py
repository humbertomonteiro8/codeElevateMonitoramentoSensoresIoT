# sensor_producer/fake_data_generator.py

from faker import Faker
import random

fake = Faker()


def generate_sensor_data():
    """Gera dados simulados de sensores industriais."""
    return {
        "sensor_id": fake.uuid4(),
        "machine_id": fake.random_int(min=1000, max=9999),
        "vibration": round(random.uniform(0.1, 10.0), 2),  # Hz
        "oil_level": round(random.uniform(0, 100), 2),  # %
        "rotation_speed": random.randint(500, 5000),  # RPM
        "energy_consumption": round(random.uniform(0.5, 50.0), 2),  # kWh
        "temperature": round(random.uniform(20.0, 80.0), 2),  # °C
        "pressure": round(random.uniform(500, 3000), 2),  # Pa
        "timestamp": fake.iso8601()
    }
