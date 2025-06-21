"""Consume data messaging with Kafka"""
import os
from confluent_kafka import Consumer
from supabase import create_client, Client
import dotenv
from helper import extract_delimited_string

dotenv.load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
KAFKA_NETWORK = os.environ.get("KAFKA_NETWORK")
supabase: Client = create_client(url, key)


# Consumer configuration (replace with your Redpanda details)
consumer = Consumer({
    'bootstrap.servers': KAFKA_NETWORK,
    'group.id': 'trpl-group',  # Assign a unique consumer group ID
    'auto.offset.reset': 'earliest'
})
consumer.subscribe([TOPIC_NAME])

# Continuously listen for messages
try:
    while True:
        msg = consumer.poll(1.0)  # Check for new messages every second
        if msg is None:
            continue
        elif msg.error():
            print(f"Error: {msg.error()}")
        else:
            # delimiter based untuk handle message tersebut sehingga di proses oleh multi
            # column pada supabase
            # example => I want to insert data delimited:john doe
            message = msg.value().decode('utf-8')
            print(f"Received message: {message}")
            message_extracted = extract_delimited_string(message)

            message_data = {
                "topic": TOPIC_NAME,
                "message": message_extracted[0],
                "sender": message_extracted[1]
            }
            data = supabase.table("message_store").insert(
                message_data).execute()
            # Process the message further (e.g., play audio, store in database)

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer connection
    consumer.close()
