import pytest
from unittest.mock import patch, MagicMock
from data_consumer.db_handler import insert_sensor_data


def sample_data():
    return {
        "sensor_id": 1,
        "machine_id": 101,
        "vibration": 0.02,
        "oil_level": 75,
        "rotation_speed": 1200,
        "energy_consumption": 150,
        "temperature": 55,
        "pressure": 5,
        "timestamp": "2025-06-15 15:00:00",
    }


@patch("data_consumer.db_handler.psycopg2.connect")
def test_insert_sensor_data(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    data = sample_data()
    insert_sensor_data(data)

    # Verifica se a conexão foi criada
    mock_connect.assert_called_once()

    # Verifica se o cursor executou a query com os valores certos
    expected_values = (
        data["sensor_id"],
        data["machine_id"],
        data["vibration"],
        data["oil_level"],
        data["rotation_speed"],
        data["energy_consumption"],
        data["temperature"],
        data["pressure"],
        data["timestamp"],
    )
    mock_cursor.execute.assert_called_once()
    args, kwargs = mock_cursor.execute.call_args
    # args[0] é o texto da query, args[1] os valores
    assert args[1] == expected_values

    # Verifica se commit, close foram chamados
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()
