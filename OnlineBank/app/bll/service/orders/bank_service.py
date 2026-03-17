from app.bll.service.general_service import GeneralService
from app.db.database import Bank
from app.schemas.create_schemas import CreateBankSchema


class BankService(GeneralService[Bank, CreateBankSchema]):
    pass
