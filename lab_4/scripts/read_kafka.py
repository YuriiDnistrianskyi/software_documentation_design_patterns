from app.sources.kafka_connect import consumer

def main():
    try:
        for message in consumer:
            if message:
                print(message.value.decode('utf-8'))
    except Exception as ex:
        print(f'Error: {ex}')
    except KeyboardInterrupt:
        print('Stop read by Ctrl+C')
    finally:
        print('This is in kafka')
        consumer.close()

if __name__ == '__main__':
    main()
