from kiteconnect import KiteConnect
from confluent_kafka import Producer
import json

# Zerodha API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
access_token = 'your_access_token'

# Kafka configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
    'client.id': 'zerodha-producer'
}

# Create a Kafka producer instance
kafka_producer = Producer(kafka_config)

# Create a Zerodha KiteConnect instance
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Define the instrument token for the stock you want to track
instrument_token = 256265  # Replace with the instrument token for your desired stock

# Kafka topic to publish data
kafka_topic = 'stock_data'

# Callback function to handle Kafka delivery reports
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Fetch live data from Zerodha and send it to Kafka
while True:
    instrument_data = kite.ltp('NSE:' + str(instrument_token))
    data_to_publish = json.dumps(instrument_data)

    # Produce the data to the Kafka topic
    kafka_producer.produce(kafka_topic, key=str(instrument_token), value=data_to_publish, callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery reports to be received.
kafka_producer.flush()
