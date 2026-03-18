from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.app_bll.interface_app_bll import IAppBll
from app.dal.app_dal.interface_app_dal import IAppDal


class AppBll(IAppBll):
    def __init__(self, dal: IAppDal):
        self.__dal: IAppDal = dal

    async def create_db(self, session: AsyncSession):
        dict_data: dict = await self.__dal.read_csv()
        await self.__dal.create_db()
        await self.__dal.insert_data(session, dict_data)
