from app.bll.app_bll.app_bll import AppBll

class AppPresentation:
    def __init__(self, app_bll: AppBll):
        self.__bll = app_bll

    def read_csv(self):
        try:
            self.__bll.read_csv()
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    def create_db(self) -> bool:
        try:
            self.__bll.create_db()
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False
