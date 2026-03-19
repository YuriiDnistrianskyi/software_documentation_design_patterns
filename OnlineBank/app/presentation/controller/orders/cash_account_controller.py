from sqlalchemy.ext.asyncio import AsyncSession

from app.presentation.controller.general_controller import GeneralController
from app.db.database import CashAccount
from app.schemas.create_schemas import CreateCashAccountSchema

class CashAccountController(GeneralController[CashAccount, CreateCashAccountSchema]):
    async def transfer(self, my_cash_id: int, cash_id: int, amount: float, session: AsyncSession) -> None:
        await self._bll.transfer(my_cash_id, cash_id, amount, session)
