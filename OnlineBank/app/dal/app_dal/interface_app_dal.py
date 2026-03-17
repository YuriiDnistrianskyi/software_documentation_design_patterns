from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class IAppDal(ABC):
    @abstractmethod
    def read_csv(self) -> dict:
        pass

    @abstractmethod
    async def _create_table(self):
        pass

    @abstractmethod
    def create_db(self):
        pass

    @abstractmethod
    def insert_data(self, session: AsyncSession, data: dict):
        pass
