from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class InterfaceDAO(ABC, Generic[T]):
    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list[T]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        pass

    @abstractmethod
    async def create(self, obj: object, session: AsyncSession) -> dict:
        pass

    @abstractmethod
    async def update(self, id: int, session: AsyncSession) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int, session: AsyncSession) -> None:
        pass
