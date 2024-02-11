import os
import time
import websocket
import json
from confluent_kafka import Producer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'BTCUSD'

# Kafka producer
kafka_producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

# Access the API key and secret from environment variables
api_key = os.getenv("TRADE_API_KEY")
secret_key = os.getenv("TRADE_API_SECRET")


def on_message(ws, message):
    #print("Received message:", message)
    # Send message to Kafka topic
    kafka_producer.produce(KAFKA_TOPIC, message)

def on_error(ws, error):
    print("Error:", error)


def on_close(ws):
    print("### WebSocket connection closed ###")


def on_open(ws):
    #print("### WebSocket connection opened ###")
    # Subscribe to relevant channels
    subscribe_message = {
        "action": "auth",
        "key": api_key,
        "secret": secret_key
    }
    ws.send(json.dumps(subscribe_message))
    ws.send(json.dumps({"action": "subscribe", "bars": ["BTC/USD"]}))


def run_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.data.alpaca.markets/v1beta3/crypto/us",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


run_websocket()

# if __name__ == "__main__":
#     while True:
#         run_websocket()
#         time.sleep(10)  # Wait for 1 second before reconnecting
