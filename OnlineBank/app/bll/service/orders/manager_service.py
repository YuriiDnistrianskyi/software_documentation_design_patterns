from app.bll.service.general_service import GeneralService
from app.db.database import Manager
from app.schemas.create_schemas import CreateManagerSchema


class ManagerService(GeneralService[Manager, CreateManagerSchema]):
    pass
