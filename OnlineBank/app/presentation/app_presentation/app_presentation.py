from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.app_bll.app_bll import AppBll

class AppPresentation:
    def __init__(self, app_bll: AppBll):
        self.__bll = app_bll

    def create_db(self, session: AsyncSession) -> bool:
        try:
            self.__bll.create_db(session)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False
