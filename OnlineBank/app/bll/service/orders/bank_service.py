from sqlalchemy.ext.asyncio import AsyncSession
from app.bll.service.general_service import GeneralService
from app.db.database import Bank
from app.schemas.create_schemas import CreateBankSchema
from app.schemas.update_schemas import UpdateBankSchema


class BankService(GeneralService[Bank, CreateBankSchema, UpdateBankSchema]):
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
