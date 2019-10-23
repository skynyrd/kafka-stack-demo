import schedule
import time

import ujson
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer

from src.Product import Product
print("We're ready")

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: ujson.dumps(v).encode('utf-8'))


def job():
    product = Product.load_random()
    producer.send(topic="test-topic", value=product.to_kafka_model())


schedule.every(1).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
