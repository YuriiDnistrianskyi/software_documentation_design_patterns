from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.controller.general_controller import GeneralController
from app.db.database import Manager, Employee
from app.schemas.create_schemas import CreateEmployeeSchema

class ManagerController(GeneralController[Manager, CreateEmployeeSchema]):

    async def create_employee(self, schema: CreateEmployeeSchema, session: AsyncSession) -> Employee:
        try:
            obj = await self._bll.create(schema, session)
            await session.commit()
            return obj
        except:
            await session.rollback()
            raise

    async def delete_employee(self, obj_id: int, session: AsyncSession):
        try:
            await self._bll.delete(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise

    async def approve_deposit_contract(self, obj_id: int, session: AsyncSession):
        try:
            await self._bll.approve_deposit_contract(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise

    async def approve_credit_contract(self, obj_id: int, session: AsyncSession):
        try:
            await self._bll.approve_credit_contract(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise
