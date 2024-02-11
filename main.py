import time

import websocket
import json


TRADE_API_KEY="x"
TRADE_API_SECRET="x"

def on_message(ws, message):
    print("Received message:", message)


def on_error(ws, error):
    print("Error:", error)


def on_close(ws):
    print("### WebSocket connection closed ###")


def on_open(ws):
    print("### WebSocket connection opened ###")
    # Subscribe to relevant channels
    subscribe_message = {
        "action": "auth",
        "key": TRADE_API_KEY,
        "secret": TRADE_API_SECRET
    }
    ws.send(json.dumps(subscribe_message))
    # Subscribe to channels you are interested in
    ws.send(json.dumps({"action":"subscribe","trades":["BTC/USD"],"quotes":["ETH/USD"],"bars":["BCH/USD"]}))


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
