import json
from app.redis.redis_connect import r

def main():
    redis = r
    len_read = 100
    start = 0

    while True:
        rows = redis.lrange('data_csv', start, start + len_read -1)

        if not rows:
            break

        rows = [json.loads(row) for row in rows]
        print(rows)
        start += len_read

    print('This is in redis')

if __name__ == "__main__":
    main()
