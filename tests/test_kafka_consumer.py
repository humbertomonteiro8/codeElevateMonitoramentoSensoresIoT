import pytest
from unittest.mock import patch, MagicMock
from data_consumer.kafka_consumer import start_kafka_consumer
from data_consumer.consumer_settings import (
    KAFKA_TOPIC,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_GROUP_ID,
)


@patch("data_consumer.kafka_consumer.KafkaConsumer")
def test_start_kafka_consumer(mock_kafka_consumer):
    mock_consumer_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_consumer_instance

    consumer = start_kafka_consumer()

    # Verifica se KafkaConsumer foi chamado uma vez
    mock_kafka_consumer.assert_called_once()

    # Captura os argumentos passados ao KafkaConsumer
    args, kwargs = mock_kafka_consumer.call_args

    # O tópico é passado como primeiro argumento posicional
    assert args[0] == KAFKA_TOPIC

    # Verifica parâmetros no kwargs
    assert kwargs["bootstrap_servers"] == KAFKA_BOOTSTRAP_SERVERS
    assert kwargs["group_id"] == KAFKA_GROUP_ID
    assert kwargs["auto_offset_reset"] == "earliest"
    assert kwargs["enable_auto_commit"] is True

    # Verifica se o value_deserializer está definido e funciona corretamente
    sample_json = b'{"key":"value"}'
    deserialized = kwargs["value_deserializer"](sample_json)
    assert deserialized == {"key": "value"}

    # Confirma que a função retornou a instância criada
    assert consumer == mock_consumer_instance
