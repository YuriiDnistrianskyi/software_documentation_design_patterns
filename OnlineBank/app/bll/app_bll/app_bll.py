from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.app_bll.interface_app_bll import IAppBll
from app.dal.app_dal.interface_app_dal import IAppDal


class AppBll(IAppBll):
    def __init__(self, dal: IAppDal):
        self.__dal: IAppDal = dal

    def create_db(self, session: AsyncSession):
        dict_data: dict = self.__dal.read_csv()
        # self.__dal.create_db()
        # self.__dal.insert_data(session, dict_data)
