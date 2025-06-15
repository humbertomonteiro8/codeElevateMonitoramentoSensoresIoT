from unittest.mock import patch
from data_consumer.consumer_utils import process_message


def test_process_message_calls_insert_sensor_data():
    mock_data = {
        "sensor_id": "abc-123",
        "machine_id": 4567,
        "vibration": 3.2,
        "oil_level": 75.0,
        "rotation_speed": 3200,
        "energy_consumption": 12.5,
        "temperature": 55.0,
        "pressure": 1500.0,
        "timestamp": "2025-06-15T15:00:00",
    }

    with patch("data_consumer.consumer_utils.insert_sensor_data") as mock_insert:
        process_message(mock_data)
        mock_insert.assert_called_once_with(mock_data)
