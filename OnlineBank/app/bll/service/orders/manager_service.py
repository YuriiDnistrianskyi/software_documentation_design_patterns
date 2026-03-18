from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.service.general_service import GeneralService
from app.db.database import Manager
from app.schemas.create_schemas import CreateManagerSchema
from app.schemas.update_schemas import UpdateManagerSchema


class ManagerService(GeneralService[Manager, CreateManagerSchema, UpdateManagerSchema]):
    async def update(self, id: int, data: UpdateManagerSchema, session: AsyncSession) -> None:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'employee_id' in data_dict:
            obj.employee_id = data_dict['employee_id']

        if 'manager_key' in data_dict:
            obj.manager_key = data_dict['manager_key']

        return obj
