from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.general_service import GeneralService
from app.db.database import DepositContract
from app.schemas.create_schemas import CreateDepositContractSchema
from app.schemas.update_schemas import UpdateDepositContractSchema


class DepositContractService(GeneralService[DepositContract, CreateDepositContractSchema, UpdateDepositContractSchema]):
    async def update(self, id: int, data: UpdateDepositContractSchema, session: AsyncSession) -> DepositContract:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'interest' in data_dict:
            obj.interest = data_dict['interest']

        if 'cash_account_id' in data_dict:
            obj.cash_account_id = data_dict['cash_account_id']

        if 'amount_of_money' in data_dict:
            obj.amount_of_money = data_dict['amount_of_money']

        if 'opening_date' in data_dict:
            obj.opening_date = data_dict['opening_date']

        if 'closing_date' in data_dict:
            obj.closing_date = data_dict['closing_date']

        return obj
