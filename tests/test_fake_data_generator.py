import pytest
from sensor_producer.fake_data_generator import generate_sensor_data


def test_generate_sensor_data():
    data = generate_sensor_data()
    assert isinstance(data, dict)
    assert "temperature" in data
    assert isinstance(data["temperature"], float)