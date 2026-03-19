from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.db.database import CashAccount
from app.schemas.create_schemas import CreateCashAccountSchema
from app.schemas.update_schemas import UpdateCashAccountSchema


class CashAccountService(GeneralService[CashAccount, CreateCashAccountSchema, UpdateCashAccountSchema]):
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
