import requests
import csv

from app.dal.i_app_dal import IAppDal
from app.core.config import DATA_SOURCE, DATA_FILE_CSV, SAVING_PLACE

from app.core.writer.ConsoleWriter import ConsoleWriter
from app.core.writer.TXTWriter import TXTWriter
from app.core.writer.RedisWriter import RedisWriter
from app.core.writer.KafkaWriter import KafkaWriter

class AppDal(IAppDal):
    def read_data_source(self):
        response = requests.get(DATA_SOURCE)
        response.raise_for_status()

        lines = response.text.splitlines()

        reader = csv.reader(lines)

        with open(DATA_FILE_CSV, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)

            for row in reader:
                writer.writerow(row)

    def write_data(self):
        writer = None
        if SAVING_PLACE == 'console':
            writer = ConsoleWriter()
        elif SAVING_PLACE == 'txt':
            writer = TXTWriter()
        elif SAVING_PLACE == 'redis':
            writer = RedisWriter()
        elif SAVING_PLACE == 'kafka':
            writer = KafkaWriter()

        if writer is None:
            print('No find SAVING_PLACE')
            print('So SAVING_PLACE -> console')
            writer = ConsoleWriter()

        with open(DATA_FILE_CSV, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0

            for line in reader:
                writer.write(line)
                count += 1

            print(count)
