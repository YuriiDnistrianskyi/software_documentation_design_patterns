from app.bll.controller.general_controller import GeneralController
from app.db.database import Employee
from app.schemas.create_schemas import CreateEmployeeSchema

class EmployeeController(GeneralController[Employee, CreateEmployeeSchema]):
    pass
