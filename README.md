# 🛰️ Monitoramento de Sensores IoT com Kafka
Este projeto tem como objetivo criar um sistema de monitoramento de sensores IoT que envia dados em tempo real para um tópico Kafka (Producer) e consome esses dados para processamento e armazenamento (Consumer).

---

## 📌 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Estrutura de Diretórios](#estrutura-de-diretórios)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Como Rodar o Projeto](#como-rodar-o-projeto)
5. [Testes](#testes)
6. [Autores](#autores)

---

## 📝 Sobre o Projeto

O projeto consiste em duas partes principais:

# Producer
- Objetivo: Gerar dados falsos de sensores IoT e enviá-los para um tópico Kafka.
- Tecnologia: Python com a biblioteca faker para geração de dados simulados.

# Consumer
- Objetivo: Consumir os dados do tópico Kafka, processá-los e armazená-los em um banco de dados.
- Tecnologia: Python com bibliotecas adequadas para consumo de Kafka e interação com banco de dados.

---

  ## 📂 Estrutura de Diretórios
```plaintext
📦 codeElevateMonitoramentoSensoresIoT
├── 📁 container_setup
│   └── 📄 service_dockerfile
├── 📁 dashboard
│   └── 📄 app.py
├── 📁 data_consumer
│   ├── 📄 __init__.py
│   ├── 📄 consumer_settings.py
│   ├── 📄 consumer_utils.py
│   ├── 📄 db_handler.py
│   ├── 📄 kafka_consumer.py
│   └── 📄 main_consumer.py
├── 📁 sensor_producer
│   ├── 📄 __init__.py
│   ├── 📄 fake_data_generator.py
│   ├── 📄 kafka_sender.py
│   └── 📄 main_producer.py
├── 📁 tests
│   ├── 📄 test_consumer_utils.py
│   ├── 📄 test_db_handler.py
│   ├── 📄 test_fake_data_generator.py
│   ├── 📄 test_kafka_consumer.py
│   └── 📄 test_kafka_sender.py
├── 📄 docker-compose.yml
├── 📄 .gitignore
└── 📄 requirements.txt
```
---

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- Kafka (para mensageria)
- Postgres
- Dash
- Faker (para geração de dados simulados)
- Bibliotecas de consumo Kafka (como confluent-kafka ou kafka-python)
- Bibliotecas de banco de dados (como psycopg2 para PostgreSQL ou pyodbc para SQL Server)
- Docker (para containerização do ambiente)

### Instalação / Configuração / Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/humbertomonteiro8/codeElevateMonitoramentoSensoresIoT.git
   cd codeElevateMonitoramentoSensoresIoT
   
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Subir os containers com Docker Compose.
   ```bash
   docker compose up -d

✅ Testes
1. Os testes estão localizados na pasta tests e podem ser executados utilizando o pytest:
    ```bash
    pytest testes/

👨‍💻 Autor
Humberto Monteiro da Cruz - Desenvolvedor Principal - [humbertomonteiro8](https://github.com/humbertomonteiro8)
