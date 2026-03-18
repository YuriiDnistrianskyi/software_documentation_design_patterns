from app.presentation.controller.general_controller import GeneralController
from app.db.database import Manager
from app.schemas.create_schemas import CreateEmployeeSchema

class ManagerController(GeneralController[Manager, CreateEmployeeSchema]):
    pass
