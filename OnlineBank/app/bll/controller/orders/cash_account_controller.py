from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.interface_service import InterfaceService
from app.bll.controller.general_controller import GeneralController
from app.db.database import CashAccount, DepositContract, CreditContract
from app.schemas.create_schemas import CreateCashAccountSchema, CreateCreditContractSchema, CreateDepositContractSchema


class CashAccountController(GeneralController[CashAccount, CreateCashAccountSchema]):
    def __init__(self, bll: InterfaceService, deposit_contract_bll: InterfaceService, credit_contract_bll: InterfaceService) -> None:
        super().__init__(bll)
        self._deposit_contract_bll = deposit_contract_bll
        self._credit_contract_bll = credit_contract_bll

    async def transfer(self, my_cash_id: int, cash_id: int, amount: float, session: AsyncSession) -> None:
        try:
            await self._bll.transfer(my_cash_id, cash_id, amount, session)
            await session.commit()
        except:
            await session.rollback()
            raise

    async def create_deposit_contract(self, schema: CreateDepositContractSchema, session: AsyncSession) -> DepositContract:
        try:
            obj = await self._user_bll.create(schema, session)
            await session.commit()
            return obj
        except:
            await session.rollback()
            raise

    async def create_credit_contract(self, schema: CreateCreditContractSchema, session: AsyncSession) -> CreditContract:
        try:
            obj = await self._credit_contract_bll.create(schema, session)
            await session.commit()
            return obj
        except:
            await session.rollback()
            raise

    async def delete_deposit_contract(self, obj_id: int, session: AsyncSession) -> None:
        try:
            await self._deposit_contract_bll.delete(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise

    async def delete_credit_contract(self, obj_id: int, session: AsyncSession) -> None:
        try:
            await self._credit_contract_bll.delete(obj_id, session)
            await session.commit()
        except:
            await session.rollback()
            raise
