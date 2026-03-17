from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from app.db.database import Base
from app.schemas.create_schemas import CreateCashAccountSchema


class CashAccount(Base):
    __tablename__ = 'cash_account'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    number: Mapped[str] = mapped_column(String),
    balance: Mapped[float] = mapped_column(Float),
    __CVV: Mapped[int] = mapped_column(Integer),
    opening_date: Mapped[DateTime] = mapped_column(DateTime) # datetime
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    bank_id: Mapped[int] = mapped_column(Integer, ForeignKey('bank.id'))

    @staticmethod
    def get_columns() -> str:
        return '#cash_account\nnumber;balance;__CVV;opening_date;user_id;bank_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};{i};{i};{i};{i},{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateCashAccountSchema):
        return CashAccount(**schema.model_dump())
