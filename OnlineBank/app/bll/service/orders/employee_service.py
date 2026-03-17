from app.bll.service.general_service import GeneralService
from app.db.database import Employee
from app.schemas.create_schemas import CreateEmployeeSchema


class EmployeeService(GeneralService[Employee, CreateEmployeeSchema]):
    pass
