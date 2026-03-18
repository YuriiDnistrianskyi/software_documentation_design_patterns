from app.presentation.controller.general_controller import GeneralController
from app.db.database import Bank
from app.schemas.create_schemas import CreateBankSchema

class BankController(GeneralController[Bank, CreateBankSchema]):
    pass
