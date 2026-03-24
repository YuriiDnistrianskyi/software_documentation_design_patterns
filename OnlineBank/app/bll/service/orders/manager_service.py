from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.bll.service.general_service import GeneralService
from app.dal.dao.interface_dao import InterfaceDAO
from app.db.database import Manager
from app.db.models.employee import Employee
from app.schemas.create_schemas import CreateManagerSchema, CreateEmployeeSchema
from app.schemas.update_schemas import UpdateManagerSchema


class ManagerService(GeneralService[Manager, CreateManagerSchema, UpdateManagerSchema]):
    def __init__(self,
                 class_type,
                 dao: InterfaceDAO,
                 employee_dao: InterfaceDAO,
                 deposit_contract_dao: InterfaceDAO,
                 credit_contract_dao: InterfaceDAO
    ):
        super().__init__(class_type, dao)
        self._employee_dao = employee_dao
        self._deposit_contract_dao = deposit_contract_dao
        self._credit_contract_dao = credit_contract_dao

    async def update(self, id: int, data: UpdateManagerSchema, session: AsyncSession) -> Manager:
        obj = await self._dao.update(id, session)
        data_dict = data.model_dump(exclude_unset=True)

        if 'employee_id' in data_dict:
            obj.employee_id = data_dict['employee_id']

        if 'manager_key' in data_dict:
            obj.manager_key = data_dict['manager_key']

        return obj

    async def create_employee(self, schema: CreateEmployeeSchema, session: AsyncSession) -> Manager:
        obj = Employee.create_from_schema(schema)
        await self._employee_dao.create(obj, session)

    async def delete_employee(self, obj_id: int, session: AsyncSession):
        await self._employee_dao.delete(obj_id, session)

    async def approve_deposit_contract(self, obj_id: int, session: AsyncSession):
        obj = await self._deposit_contract_dao.get_by_id(obj_id, session)
        if obj.approved:
            raise HTTPException(status_code=400, detail="Deposit contract already approved")

        obj.approved = True

    async def approve_credit_contract(self, obj_id: int, session: AsyncSession):
        obj = await self._credit_contract_dao.get_by_id(obj_id, session)
        if obj.approved:
            raise HTTPException(status_code=400, detail="Credit contract already approved")

        obj.approved = True
