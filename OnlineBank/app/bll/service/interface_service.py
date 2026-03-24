from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema')
UpdateSchema = TypeVar('UpdateSchema')

class InterfaceService(ABC, Generic[T, CreateSchema, UpdateSchema]):
    @abstractmethod
    async def get_all(self, session: AsyncSession) -> list[T]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        pass

    @abstractmethod
    async def create(self, obj: CreateSchema, session) -> T:
        pass

    @abstractmethod
    async def update(self, id: int, obj: UpdateSchema, session) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int, session: AsyncSession) -> None:
        pass
