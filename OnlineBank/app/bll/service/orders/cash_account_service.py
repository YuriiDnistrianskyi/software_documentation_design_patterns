from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.dal.dao.interface_dao import InterfaceDAO
from app.db.database import CashAccount
from app.db.models.credit_contract import CreditContract
from app.db.models.deposit_contract import DepositContract
from app.schemas.create_schemas import CreateCashAccountSchema, CreateDepositContractSchema, CreateCreditContractSchema
from app.schemas.update_schemas import UpdateCashAccountSchema


class CashAccountService(GeneralService[CashAccount, CreateCashAccountSchema, UpdateCashAccountSchema]):
    def __init__(self, class_type, dao: InterfaceDAO, deposit_account_dao: InterfaceDAO, credit_account_dao: InterfaceDAO):
        super().__init__(class_type, dao)
        self._deposit_contract_dao = deposit_account_dao
        self._credit_contract_dao = credit_account_dao

    async def update(self, id: int, data: UpdateCashAccountSchema, session: AsyncSession) -> CashAccount:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'number_account' in data_dict:
            obj.number_account = data_dict['number_account']

        if 'balance' in data_dict:
            obj.balance = data_dict['balance']

        if 'opening_date' in data_dict:
            obj.opening_date = data_dict['opening_date']

        if 'user_id' in data_dict:
            obj.user_id = data_dict['user_id']

        if 'bank_id' in data_dict:
            obj.bank_id = data_dict['bank_id']

        return obj

    async def transfer(self, my_cash_id: int, cash_id: int, amount: float, session: AsyncSession) -> None:
        my_cash_account = await self._dao.get_by_id(my_cash_id, session)
        cash_account = await self._dao.get_by_id(cash_id, session)

        if my_cash_account.balance < amount:
            raise

        my_cash_account.balance = my_cash_account.balance - amount
        cash_account.balance = cash_account.balance + amount

    async def create_deposit_contract(self, schema: CreateDepositContractSchema, session: AsyncSession) -> DepositContract:
        obj = DepositContract.create_from_schema(schema)
        await self._deposit_contract_dao.create(obj, session)
        return obj

    async def create_credit_contract(self, schema: CreateCreditContractSchema, session: AsyncSession) -> CreditContract:
        obj = DepositContract.create_from_schema(schema)
        await self._credit_contract_dao.create(obj, session)
        return obj

    async def delete_deposit_contract(self, obj_id: int, session: AsyncSession) -> None:
        await self._deposit_contract_dao.delete(obj_id, session)

    async def delete_credit_contract(self, obj_id: int, session: AsyncSession) -> None:
        await self._credit_contract_dao.delete(obj_id, session)

    async def get_cash_accounts_by_user_id(self, user_id: int, session: AsyncSession) -> list[CashAccount]:
        return await self._dao.get_cash_accounts_by_user_id(user_id, session)
