# codeElevateMonitoramentoSensoresIoT

Este projeto monitora dados sensoriais de uma fábrica ao longo do tempo, coletando **timestamp**, **temperatura**, **pressão** e **vibração**. Ele processa e analisa essas informações para geração de insights através de um consumidor de dados e um dashboard visual.

## 📁 Estrutura do Projeto
codeElevateMonitoramentoSensoresIoT/
│
├── container_setup/               # Configuração dos containers Docker
│   ├── service_dockerfile/
│
├── dashboard/                     # Aplicação para visualização dos dados
│   ├── __init__.py
│   ├── app.py                      # Código principal do dashboard
│
├── data_consumer/                  # Consumo e processamento dos dados do Kafka
│   ├── __init__.py
|   ├── sql/
│   ├── consumer_settings.py
│   ├── consumer_utils.py
│   ├── db_handler.py
│   ├── kafka_consumer.py
│   ├── main_consumer.py
│
├── sensor_producer/                # Geração e envio de dados ao Kafka
│   ├── __init__.py
│   ├── fake_data_generator.py
│   ├── kafka_sender.py
│   ├── main_producer.py
│   ├── producer_settings.py
│
├── tests/                          # Testes do sistema
│   ├── .pytest_cache/
│   ├── test_consumer_utils.py
│   ├── test_db_handler.py
│   ├── test_fake_data_generator.py
│   ├── test_kafka_consumer.py
│   ├── test_kafka_sender.py
│
├── .gitignore                      # Arquivo de ignorados do Git
├── docker-compose.yml              # Configuração do Docker
├── README.md                        # Documento explicativo do projeto
├── requirements.txt                 # Dependências do projeto


## 🚀 Como Executar

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

2. **Inicie os serviços com Docker**:

    bash
    docker-compose up --build

    Acesse o Dashboard:

2. **Se houver um front-end implementado, ele deve estar disponível em**:
    http://localhost:XXXX.

3. 📊 Visualização dos Dados
    - Os dados sensoriais são coletados e armazenados no PostgreSQL.
    - Um Kafka Consumer processa as mensagens em tempo real.
    - O Dashboard exibe gráficos interativos com:
        - Gráfico de Linha para evolução temporal dos sensores.
        - Scatter Plot para correlação entre variáveis.
        - Heatmap para identificar padrões sazonais.

🔍 **Testes e Validação**
    Para rodar os testes:

    pytest tests/        