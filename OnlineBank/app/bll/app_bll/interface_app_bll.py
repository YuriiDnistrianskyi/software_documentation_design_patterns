from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class IAppBll(ABC):

    @abstractmethod
    async def create_db(self, session: AsyncSession):
        pass
