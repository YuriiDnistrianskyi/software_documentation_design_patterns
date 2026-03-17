from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from interface_dao import InterfaceDAO

class GeneralDAO(InterfaceDAO):
    _class_type = None

    def __init__(self, class_type: object):
        self._class_type = class_type

    async def get_all(self, session: AsyncSession) -> list:
        stmt = select(self._class_type)
        list = await session.execute(stmt)
        result = list.scalars().all()
        return result

    async def get_by_id(self, id: int, session: AsyncSession) -> object:
        obj = await session.get(self._class_type, id)
        return obj

    async def create(self, obj: dict, session: AsyncSession) -> dict:
        session.add(obj)
        return obj

    async def update(self, id: int, session: AsyncSession):
        obj = await session.get(self._class_type, id)
        return obj

    async def delete(self, id: int, session: AsyncSession):
        obj = await session.get(self._class_type, id)
        if obj:
            await session.delete(obj)
