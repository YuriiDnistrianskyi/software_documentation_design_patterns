from app.bll.service.general_service import GeneralService
from app.db.database import CreditContract
from app.schemas.create_schemas import CreateCreditContractSchema


class CreditContractService(GeneralService[CreditContract, CreateCreditContractSchema]):
    pass
