from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.interface_service import InterfaceService
from app.db.database import User, CashAccount
from app.bll.controller.general_controller import GeneralController
from app.db.database import Bank
from app.schemas.create_schemas import CreateBankSchema, CreateUserSchema, CreateCashAccountSchema


class BankController(GeneralController[Bank, CreateBankSchema]):
    def __init__(self, bll: InterfaceService, user_bll: InterfaceService, cash_account_bll: InterfaceService) -> None:
        super().__init__(bll)
        self._user_bll = user_bll
        self._cash_account_bll = cash_account_bll

    async def create_user(self, schema: CreateUserSchema, session: AsyncSession) -> User:
        try:
            obj = await self._user_bll.create(schema, session)
            await session.commit()
            return obj
        except:
            await session.rollback()
            raise


    async def delete_user(self, obj_id: int, session: AsyncSession):
        try:
            await self._user_bll.delete(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise

    async def create_cash_account(self, schema: CreateCashAccountSchema, session: AsyncSession) -> CashAccount:
        try:
            obj = await self._cash_account_bll.create(schema, session)
            await session.commit()
            return obj
        except:
            await session.rollback()
            raise

    async def delete_cash_account(self, obj_id: int, session: AsyncSession):
        try:
            await self._cash_account_bll.delete(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise
