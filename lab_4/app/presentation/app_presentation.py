from app.bll.i_app_bll import IAppBll
from app.core.config import SAVING_PLACE

class AppPresentation:
    def __init__(self, bll: IAppBll):
        self.bll = bll

    def save_data(self):
        print('Saving data...')
        try:
            self.bll.save_data()
            print(f'Data saved in {SAVING_PLACE}')
        except:
            print('Error saving data')
            raise