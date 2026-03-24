from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.dal.dao.interface_dao import InterfaceDAO
from app.db.database import Bank
from app.db.models.cash_account import CashAccount
from app.db.models.user import User
from app.schemas.create_schemas import CreateBankSchema, CreateUserSchema, CreateCashAccountSchema
from app.schemas.update_schemas import UpdateBankSchema


class BankService(GeneralService[Bank, CreateBankSchema, UpdateBankSchema]):
    def __init__(self, class_type, dao: InterfaceDAO, user_dao: InterfaceDAO, cash_account_dao: InterfaceDAO):
        super().__init__(class_type, dao)
        self.user_dao = user_dao
        self.cash_account_dao = cash_account_dao

    async def update(self, id: int, data: UpdateBankSchema, session: AsyncSession) -> Bank:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'phone' in data_dict:
            obj.phone = data_dict['phone']

        if 'email' in data_dict:
            obj.email = data_dict['email']

        if 'address' in data_dict:
            obj.address = data_dict['address']

        return obj

    async def create_user(self, obj: CreateUserSchema, session: AsyncSession) -> User:
        obj: User = User.create_from_schema(obj)
        await self.user_dao.create(obj, session)
        return obj

    async def delete_user(self, obj_id: int, session: AsyncSession):
        await self.user_dao.delete(obj_id, session)

    async def create_cash_account(self, obj: CreateCashAccountSchema, session: AsyncSession) -> CashAccount:
        obj: CashAccount = CashAccount.create_from_schema(obj)
        await self.cash_account_dao.create(obj, session)
        return obj

    async def delete_cash_account(self, obj_id: int, session: AsyncSession):
        await self.cash_account_dao.delete(obj_id, session)
