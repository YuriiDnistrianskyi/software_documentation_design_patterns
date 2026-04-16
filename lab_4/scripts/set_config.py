from dotenv import set_key

env_path = 'app/.env'

start_txt = '''
resource numbers:
1 - console
2 - txt
3 - redis
4 - kafka
'''

resource_dict = {
    1: 'console',
    2: 'txt',
    3: 'redis',
    4: 'kafka'
}

def main():
    print(start_txt)
    resource_number = int(input('Enter resource number: '))

    if resource_number not in [1, 2, 3, 4]:
        print(f'Resource number [{resource_number}] is not valid')
        return

    resource_txt = resource_dict.get(resource_number)

    set_key(env_path, 'SAVING_PLACE', resource_txt)
    print(f'Set SAVING_PLACE to {resource_txt}')

if __name__ == '__main__':
    main()