from app.bll.service.general_service import GeneralService
from app.db.database import User
from app.schemas.create_schemas import CreateUserSchema


class UserService(GeneralService[User, CreateUserSchema]):
    pass
