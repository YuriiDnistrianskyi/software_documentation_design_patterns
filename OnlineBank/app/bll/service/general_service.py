from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.interface_service import InterfaceService
from app.dal.dao.interface_dao import InterfaceDAO
from typing import TypeVar


T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema')
UpdateSchema = TypeVar('UpdateSchema')

class GeneralService(InterfaceService[T, CreateSchema, UpdateSchema]):
    def __init__(self, class_type, dao: InterfaceDAO):
        self._class_type = class_type
        self._dao = dao

    async def get_all(self, session: AsyncSession) -> list[T]:
        objects: list = await self._dao.get_all(session)
        return objects

    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        obj = await self._dao.get_by_id(id, session)
        return obj

    async def create(self, schema: CreateSchema, session) -> T:
        obj = self._class_type.create_from_schema(schema)
        await self._dao.create(obj, session)
        return obj

    async def update(self, id: int, obj: UpdateSchema, session) -> T:
        pass

    async def delete(self, id: int, session: AsyncSession) -> None:
        await self._dao.delete(id, session)

