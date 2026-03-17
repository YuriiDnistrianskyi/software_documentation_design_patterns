from app.bll.service.general_service import GeneralService
from app.db.database import CashAccount
from app.schemas.create_schemas import CreateCashAccountSchema


class CashAccountService(GeneralService[CashAccount, CreateCashAccountSchema]):
    pass
