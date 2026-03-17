from app.bll.service.general_service import GeneralService
from app.db.database import Cashier
from app.schemas.create_schemas import CreateCashierSchema


class CashierService(GeneralService[Cashier, CreateCashierSchema]):
    pass
