from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import TypeVar
from app.dal.dao.interface_dao import InterfaceDAO

T = TypeVar('T')

class GeneralDAO(InterfaceDAO[T]):
    async def get_all(self, session: AsyncSession) -> list[T]:
        stmt = select(T)
        _list = await session.execute(stmt)
        result: list = _list.scalars().all()
        return result

    async def get_by_id(self, id: int, session: AsyncSession) -> object:
        obj = await session.get(T, id)
        return obj

    async def create(self, obj: dict, session: AsyncSession) -> dict:
        session.add(obj)
        return obj

    async def update(self, id: int, session: AsyncSession):
        obj = await session.get(T, id)
        return obj

    async def delete(self, id: int, session: AsyncSession):
        obj = await session.get(T, id)
        if obj:
            await session.delete(obj)
