from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0, 11, 5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    'data_csv',
    bootstrap_servers='localhost:9092',
    api_version=(0, 11, 5),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)
