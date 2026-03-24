from app.presentation.controller.general_controller import GeneralController
from app.db.database import DepositContract
from app.schemas.create_schemas import CreateDepositContractSchema

class DepositContractController(GeneralController[DepositContract, CreateDepositContractSchema]):
    pass
