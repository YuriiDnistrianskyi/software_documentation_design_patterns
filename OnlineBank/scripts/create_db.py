from app.presentation.app_presentation import app_presentation

def main():
    result_create_db = app_presentation.create_db()
    if not result_create_db:
        return
    print('Table created')
    result_read_csv = app_presentation.read_csv()

    if not result_read_csv:
        return
    print('Table read')

if __name__ == '__main__':
    main()
