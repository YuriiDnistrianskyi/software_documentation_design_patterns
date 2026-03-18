from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.db.database import Cashier
from app.schemas.create_schemas import CreateCashierSchema
from app.schemas.update_schemas import UpdateCashierSchema


class CashierService(GeneralService[Cashier, CreateCashierSchema, UpdateCashierSchema]):
    async def update(self, id: int, data: UpdateCashierSchema, session: AsyncSession) -> Cashier:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'employee_id' in data_dict:
            obj.employee_id = data_dict['employee_id']

        if 'cashier_key' in data_dict:
            obj.cashier_key = data_dict['cashier_key']

        return obj
