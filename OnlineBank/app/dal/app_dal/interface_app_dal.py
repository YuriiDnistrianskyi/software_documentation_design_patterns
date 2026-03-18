from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class IAppDal(ABC):
    @abstractmethod
    async def read_csv(self) -> dict:
        pass

    @abstractmethod
    async def _create_table(self):
        pass

    @abstractmethod
    async def create_db(self):
        pass

    @abstractmethod
    def insert_data(self, session: AsyncSession, data: dict):
        pass
