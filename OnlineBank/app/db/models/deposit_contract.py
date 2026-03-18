from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, Float, DateTime, Boolean
from app.db.database import Base
from app.schemas.create_schemas import CreateEmployeeSchema

class DepositContract(Base):
    __tablename__ = 'deposit_contract'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    interest: Mapped[float] = mapped_column(Float)
    cash_account_id: Mapped[int] = mapped_column(Integer, ForeignKey('cash_account.id'))
    amount_of_money: Mapped[float] = mapped_column(Float)
    approve: Mapped[bool] = mapped_column(Boolean)
    opening_date: Mapped[DateTime] = mapped_column(DateTime)
    closing_date: Mapped[DateTime] = mapped_column(DateTime)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'interest': self.interest,
            'cash_account_id': self.cash_account_id,
            'amount_of_money': self.amount_of_money,
            'approve': self.approve,
            'opening_date': self.opening_date,
            'closing_date': self.closing_date
        }

    @staticmethod
    def get_columns() -> str:
        return '#deposit_contract\nid;interest;cash_account_id;amount_of_money;approve;opening_date;closing_date\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};{i};{i};{i};0;2025-11-11 11:11:11;2025-11-11 11:11:22\n'

    @staticmethod
    async def create_from_schema(schema: CreateEmployeeSchema):
        return DepositContract(**schema.model_dump())

