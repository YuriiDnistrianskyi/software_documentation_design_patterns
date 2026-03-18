from app.presentation.controller.general_controller import GeneralController
from app.db.database import Cashier
from app.schemas.create_schemas import CreateCashierSchema

class CashierController(GeneralController[Cashier, CreateCashierSchema]):
    pass
