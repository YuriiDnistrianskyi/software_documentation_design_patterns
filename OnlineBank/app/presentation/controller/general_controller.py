from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar
from app.presentation.controller.interface_controller import InterfaceController
from app.bll.service.interface_service import InterfaceService

T = TypeVar('T')
CreateSchema = TypeVar('CreateSchema')

class GeneralController(InterfaceController[T, CreateSchema]):
    def __init__(self, bll: InterfaceService) -> None:
        self._bll = bll

    async def get_all(self, session: AsyncSession) -> list[T]:
        try:
            objects = await self._bll.get_all(session)
            return objects
        except Exception as e:
            await session.rollback()

    async def get_by_id(self, id: int, session: AsyncSession) -> T:
        try:
            obj = await self._bll.get_by_id(id, session)
            return obj
        except Exception as e:
            await session.rollback()

    async def create(self, obj: CreateSchema, session) -> T:
        try:
            new_obj = await self._bll.create(obj, session)
            await session.commit()
            await session.refresh(new_obj)
            return new_obj
        except Exception as e:
            await session.rollback()

    async def update(self, id: int, obj: T, session) -> None:
        try:
            await self._bll.update(id, obj, session)
            await session.commit()
        except Exception as e:
            await session.rollback()

    async def delete(self, id: int, session: AsyncSession) -> None:
        try:
            await self._bll.delete(id, session)
            await session.commit()
        except Exception as e:
            await session.rollback()
