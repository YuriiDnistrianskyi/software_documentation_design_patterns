from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.dal.dao.interface_dao import InterfaceDAO
from app.db.database import Cashier
from app.schemas.create_schemas import CreateCashierSchema
from app.schemas.update_schemas import UpdateCashierSchema


class CashierService(GeneralService[Cashier, CreateCashierSchema, UpdateCashierSchema]):
    def __init__(self, class_type, dao: InterfaceDAO, cash_account_dao: InterfaceDAO) -> None:
        super().__init__(class_type, dao)
        # self._class_type = class_type
        # self._dao = dao
        self.__cash_account_dao = cash_account_dao

    async def update(self, id: int, data: UpdateCashierSchema, session: AsyncSession) -> Cashier:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'employee_id' in data_dict:
            obj.employee_id = data_dict['employee_id']

        if 'cashier_key' in data_dict:
            obj.cashier_key = data_dict['cashier_key']

        return obj

    async def transfer(self, cash_id_1: int, cash_id_2: int, amount: float, session: AsyncSession) -> None:
        cash_account_1 = await self.__cash_account_dao.get_by_id(cash_id_1, session)
        cash_account_2 = await self.__cash_account_dao.get_by_id(cash_id_2, session)

        if cash_account_1.balance < amount:
            raise

        cash_account_1.balance = cash_account_1.balance - amount
        cash_account_2.balance = cash_account_2.balance + amount

