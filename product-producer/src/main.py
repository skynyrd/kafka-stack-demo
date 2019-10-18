import schedule
import time

import ujson
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = [NewTopic(name="test_topic", num_partitions=3, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: ujson.dumps(v).encode('utf-8'))


# def job():
#     producer.send('fizzbuzz', 'foo-bar')
#
#
# schedule.every(1).second.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
