"""Send message with Kafka using msgpack and log to Supabase"""
import os
import argparse
from supabase import create_client, Client
from confluent_kafka import Producer
import msgpack
import dotenv
from helper import delivery_report

# Load .env file
dotenv.load_dotenv()

# Command-line argument parser
parser = argparse.ArgumentParser(description="Send a message via Kafka and log to Supabase.")
parser.add_argument('-m', '--message', type=str, default="Send With msgpack",
                    help="Message content to send (default: 'Send With msgpack')")
args = parser.parse_args()

# Supabase config
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Kafka config
TOPIC_NAME = os.environ.get("TOPIC_NAME")
KAFKA_NETWORK = os.environ.get("KAFKA_NETWORK")
kafka_config = {
    'bootstrap.servers': KAFKA_NETWORK,
}
producer = Producer(kafka_config)

# Compose message
data = {
    "topic": TOPIC_NAME,
    "message": args.message,
    "sender": "msg-pack-agent"
}

# Send message to Kafka
encoded_data = msgpack.packb(data, use_bin_type=True)
producer.produce(TOPIC_NAME, encoded_data, on_delivery=delivery_report)
producer.poll(0)
producer.flush()
