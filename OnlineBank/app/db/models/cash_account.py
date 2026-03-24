from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from app.db.database import Base
from app.schemas.create_schemas import CreateCashAccountSchema


class CashAccount(Base):
    __tablename__ = 'cash_account'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    number_account: Mapped[str] = mapped_column(String)
    balance: Mapped[float] = mapped_column(Float)
    CVV: Mapped[int] = mapped_column(Integer)
    opening_date: Mapped[DateTime] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('_user.id'))
    bank_id: Mapped[int] = mapped_column(Integer, ForeignKey('bank.id'))

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'number_account': self.number_account,
            'balance': self.balance,
            'opening_date': self.opening_date,
            'user_id': self.user_id,
            'bank_id': self.bank_id,
        }

    @staticmethod
    def get_columns() -> str:
        return '#cash_account\nid;number_account;balance;__CVV;opening_date;user_id;bank_id\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};{i};{i};{i};2025-11-11 11:11:11;{i};{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateCashAccountSchema):
        return CashAccount(**schema.model_dump())
