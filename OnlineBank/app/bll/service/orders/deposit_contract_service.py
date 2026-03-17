from app.bll.service.general_service import GeneralService
from app.db.database import DepositContract
from app.schemas.create_schemas import CreateDepositContractSchema


class DepositContractService(GeneralService[DepositContract, CreateDepositContractSchema]):
    pass
