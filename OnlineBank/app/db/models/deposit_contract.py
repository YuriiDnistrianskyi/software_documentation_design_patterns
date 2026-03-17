from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, Float, DateTime
from app.db.database import Base
from app.schemas.create_schemas import CreateEmployeeSchema

class DepositContract(Base):
    __tablename__ = 'deposit_contract'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    interest: Mapped[float] = mapped_column(Float)
    cash_account_id: Mapped[int] = mapped_column(Integer, ForeignKey('cash_account.id'))
    amount_of_money: Mapped[float] = mapped_column(Float)
    opening_date: Mapped[DateTime] = mapped_column(DateTime)
    closing_date: Mapped[DateTime] = mapped_column(DateTime)

    @staticmethod
    async def create_from_schema(schema: CreateEmployeeSchema):
        return DepositContract(**schema.model_dump())

