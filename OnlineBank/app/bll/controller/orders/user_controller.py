from app.bll.controller.general_controller import GeneralController
from app.db.database import User
from app.schemas.create_schemas import CreateUserSchema

class UserController(GeneralController[User, CreateUserSchema]):
    pass
