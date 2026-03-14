from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod

class InterfaceDAO(ABC):
    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list:
        pass

    @abstractmethod
    async def get_by_id(self, id: int, session: AsyncSession) -> object:
        pass

    @abstractmethod
    async def create(self, obj: object, session: AsyncSession) -> dict:
        pass

    @abstractmethod
    async def update(self, id: int, session: AsyncSession) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int, session: AsyncSession) -> None:
        pass
