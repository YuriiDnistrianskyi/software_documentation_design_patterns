from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base
from app.schemas.create_schemas import CreateCashierSchema


class Cashier(Base):
    __tablename__ = 'cashier'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    cashier_key: Mapped[str] = mapped_column(String)

    @staticmethod
    async def create_from_schema(schema: CreateCashierSchema):
        return Cashier(**schema.model_dump())
