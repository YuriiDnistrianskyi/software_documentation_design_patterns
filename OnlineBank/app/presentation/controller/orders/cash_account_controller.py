from app.presentation.controller.general_controller import GeneralController
from app.db.database import CashAccount
from app.schemas.create_schemas import CreateCashAccountSchema

class CashAccountController(GeneralController[CashAccount, CreateCashAccountSchema]):
    pass
