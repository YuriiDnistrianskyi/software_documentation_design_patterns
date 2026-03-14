from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.interface_service import InterfaceService
from app.dal.dao.interface_dao import InterfaceDAO
from typing import TypeVar

T = TypeVar('T')

class GeneralService(InterfaceService[T]):
    def __init__(self, dao: InterfaceDAO):
        self._dao = dao

    async def get_all(self, session: AsyncSession) -> list[T]:
        objects = await self._dao.get_all(session)
        return objects

    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        obj = await self._dao.get_by_id(id, session)
        return obj

    async def create(self, obj: T, session) -> T:
        pass

    async def update(self, id: int, obj: T, session) -> None:
        pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        await self._dao.delete(id, session)

