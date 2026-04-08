import requests
import csv

from app.dal.i_app_dal import IAppDal
from app.core.config import DATA_SOURCE, DATA_FILE_CSV

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
        print('write')
