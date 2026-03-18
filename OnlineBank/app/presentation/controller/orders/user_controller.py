from app.presentation.controller.general_controller import GeneralController
from app.db.database import User
from app.schemas.create_schemas import CreateUserSchema

class CashAccountController(GeneralController[User, CreateUserSchema]):
    pass
