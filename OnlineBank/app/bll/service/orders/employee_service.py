from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.general_service import GeneralService
from app.db.database import Employee
from app.schemas.create_schemas import CreateEmployeeSchema
from app.schemas.update_schemas import UpdateEmployeeSchema


class EmployeeService(GeneralService[Employee, CreateEmployeeSchema, UpdateEmployeeSchema]):
    async def update(self, id: int, data: UpdateEmployeeSchema, session: AsyncSession) -> Employee:
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

        if 'date_of_hire' in data_dict:
            obj.date_of_hire = data_dict['date_of_hire']

        return obj
