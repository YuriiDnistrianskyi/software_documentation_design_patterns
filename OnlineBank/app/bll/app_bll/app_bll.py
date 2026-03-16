from app.bll.app_bll.interface_app_bll import IAppBll
from app.dal.app_dal.interface_app_dal import IAppDal


class AppBll(IAppBll):
    def __init(self, dal: IAppDal):
        self.__dal: IAppDal = dal

    def read_csv(self):
        self.__dal.read_csv()

    def create_table(self):
        self.__dal.create_table()
