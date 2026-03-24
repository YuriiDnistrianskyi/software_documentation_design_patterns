from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.general_service import GeneralService
from app.db.database import User
from app.schemas.create_schemas import CreateUserSchema
from app.schemas.update_schemas import UpdateUserSchema


class UserService(GeneralService[User, CreateUserSchema, UpdateUserSchema]):
    async def update(self, id: int, data: UpdateUserSchema, session: AsyncSession) -> None:
        obj = await self._dao.update(id, session)
        data_dict: dict = data.model_dump()

        if 'name' in data_dict:
            obj.name = data_dict['name']

        if 'phone' in data_dict:
            obj.phone = data_dict['phone']

        if 'email' in data_dict:
            obj.email = data_dict['email']

        if 'address' in data_dict:
            obj.address = data_dict['address']
