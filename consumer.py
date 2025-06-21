"""Consume data messaging with Kafka"""
import os

from confluent_kafka import Consumer
from supabase import create_client, Client
import dotenv
from msgpack import unpackb
from helper import deconstruct_payload


dotenv.load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
KAFKA_NETWORK = os.environ.get("KAFKA_NETWORK")
supabase: Client = create_client(url, key)


# Consumer configuration (replace with your Redpanda details)
consumer = Consumer({
    'bootstrap.servers': KAFKA_NETWORK,
    'group.id': 'trpl-group-id-chat-trpl-ilkom',  # Assign a unique consumer group ID
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
            # consume data with msgpack.unpackb
            msg_received = msg.value()
            message_unpack = unpackb(msg_received, raw=False)
            topic, message, sender = deconstruct_payload(message_unpack)
            data = {
                "topic": topic,
                "message": message,
                "sender": sender
            }

            try:
                supabase.table("message_store").insert(data).execute()
                print("inserted")
            except ValueError as e:
                print(f"Unexpected error: {str(e)}")

            # Process the message further (e.g., play audio, store in database)

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer connection
    consumer.close()
