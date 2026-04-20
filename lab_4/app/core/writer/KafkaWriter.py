from app.core.writer.i_writer import IWriter
from app.sources.kafka_connect import producer

class KafkaWriter(IWriter):
    def write(self, data):
        producer.send('data_csv', data)
        producer.flush()
