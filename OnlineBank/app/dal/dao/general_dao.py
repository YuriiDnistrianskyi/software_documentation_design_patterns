from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import TypeVar
from app.dal.dao.interface_dao import InterfaceDAO

T = TypeVar('T')

class GeneralDAO(InterfaceDAO[T]):
    def __init__(self, class_type):
        self._class_type = class_type

    async def get_all(self, session: AsyncSession) -> list[T]:
        stmt = select(self._class_type)
        _list = await session.execute(stmt)
        result: list = _list.scalars().all()
        return result

    async def get_by_id(self, id: int, session: AsyncSession) -> object:
        obj = await session.get(self._class_type, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")
        return obj

    async def create(self, obj: T, session: AsyncSession) -> dict:
        session.add(obj)
        return obj

    async def update(self, id: int, session: AsyncSession):
        obj = await session.get(self._class_type, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")
        return obj

    async def delete(self, id: int, session: AsyncSession):
        obj = await session.get(self._class_type, id)
        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")
        await session.delete(obj)
