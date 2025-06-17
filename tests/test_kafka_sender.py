from unittest.mock import patch, MagicMock
import json

import sensor_producer.kafka_sender as kafka_sender


def test_create_producer_calls_kafka_producer():
    with patch('sensor_producer.kafka_sender.KafkaProducer') as mock_producer:
        mock_instance = mock_producer.return_value

        producer = kafka_sender.create_producer()

        mock_producer.assert_called_once()
        # Confirma que o produtor retornado é o mock
        assert producer == mock_instance

        # Checa se o value_serializer serializa para JSON corretamente
        sample_value = {'key': 'value'}
        serialized = mock_producer.call_args[1]['value_serializer'](sample_value)
        assert serialized == json.dumps(sample_value).encode('utf-8')


def test_send_data_calls_send_and_flush():
    mock_producer = MagicMock()
    data = {'sensor_id': 'abc123', 'value': 42}

    kafka_sender.send_data(mock_producer, data)

    mock_producer.send.assert_called_once_with(
        kafka_sender.KAFKA_TOPIC, value=data
    )
    mock_producer.flush.assert_called_once()
