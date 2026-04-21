from app.bll.controller.general_controller import GeneralController
from app.db.database import CreditContract
from app.schemas.create_schemas import CreateCreditContractSchema

class CreditContractController(GeneralController[CreditContract, CreateCreditContractSchema]):
    pass
