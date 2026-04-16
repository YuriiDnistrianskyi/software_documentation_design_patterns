import json

from app.core.writer.i_writer import IWriter
from app.redis.redis_connect import r

class RedisWriter(IWriter):
    def write(self, data):
        r.rpush('data_csv', json.dumps(data))
