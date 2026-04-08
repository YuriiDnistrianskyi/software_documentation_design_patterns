from app.bll.i_app_bll import IAppBll
from app.dal.i_app_dal import IAppDal

class AppBll(IAppBll):
    def __init__(self, dal: IAppDal):
        self.__dal = dal
