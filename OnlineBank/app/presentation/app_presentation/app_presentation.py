from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.app_bll.app_bll import AppBll

class AppPresentation:
    def __init__(self, app_bll: AppBll):
        self.__bll = app_bll

    async def create_db(self, session: AsyncSession) -> bool:
        try:
            await self.__bll.create_db(session)
            await session.commit()
            return True
        except Exception as ex:
            await session.rollback()
            print(f'Error: {ex}')
            return False
