import requests
import json
from boto3 import client

# Technical Analysis API Configuration
API_URL = "https://technical-analysis-api.com/api/v1/analysis"
API_KEY = "YOUR_API_KEY"

# Setting up Amazon Kinesis
KINESIS_STREAM_NAME = "YOUR_DATA_STREAM_NAME"

# Configuración de Amazon S3
S3_BUCKET_NAME = "YOUR_BUCKET_NAME"

# Inicializar el cliente de Kinesis
kinesis = client("kinesis")

# Inicializar el cliente de S3

s3 = client('s3')

def get_crypto_data():
    # Obtener datos de las 3 criptomonedas más demandadas
    crypto_data = {
        "Bitcoin": {"symbol": "BTC"},
        "Ethereum": {"symbol": "ETH"},
        "Ripple": {"symbol": "XRP"}
    }

    # Enviar solicitud a la API de Technical Analysis
    for crypto in crypto_data:
        response = requests.get(API_URL, params={"symbol": crypto_data[crypto]["symbol"], "apikey": API_KEY})
        crypto_data[crypto]["data"] = response.json()

    return crypto_data

def send_to_kinesis(crypto_data):
    # Enviar datos a Kinesis
    for crypto in crypto_data:
        kinesis.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps(crypto_data[crypto]),
            PartitionKey=crypto
        )

def save_to_s3(crypto_data):
    # Guardar datos en S3
    data = json.dumps(crypto_data)
    s3.put_object(Body=data, Bucket=S3_BUCKET_NAME, Key="crypto_data.json")

if __name__ == "__main__":
    crypto_data = get_crypto_data()
    send_to_kinesis(crypto_data)
    save_to_s3(crypto_data)