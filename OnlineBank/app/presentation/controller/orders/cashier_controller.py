from sqlalchemy.ext.asyncio import AsyncSession

from app.presentation.controller.general_controller import GeneralController
from app.db.database import Cashier
from app.schemas.create_schemas import CreateCashierSchema

class CashierController(GeneralController[Cashier, CreateCashierSchema]):
    async def transfer(self, cash_id_1: int, cash_id_2: int, amount: float, session: AsyncSession) -> None:
        try:
            await self._bll.transfer(cash_id_1, cash_id_2, amount, session)
            await session.commit()
        except:
            await session.rollback()
            raise
