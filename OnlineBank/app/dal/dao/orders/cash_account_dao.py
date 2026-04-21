from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.dal.dao.general_dao import GeneralDAO
from app.db.database import CashAccount


class CashAccountDAO(GeneralDAO[CashAccount]):
    async def get_cash_accounts_by_user_id(self, user_id: int, session: AsyncSession) -> list[CashAccount]:
        stmt = select(CashAccount).where(CashAccount.user_id == user_id).order_by(CashAccount.id)
        _list = await session.execute(stmt)
        result = list(_list.scalars().all())

        return result
