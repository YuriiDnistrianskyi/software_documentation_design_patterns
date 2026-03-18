from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base
from app.schemas.create_schemas import CreateCashierSchema


class Cashier(Base):
    __tablename__ = 'cashier'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    cashier_key: Mapped[str] = mapped_column(String)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'cashier_key': self.cashier_key,
        }

    @staticmethod
    def get_columns() -> str:
        return '#cashier\nemployee_id;cashier_key\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};key_{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateCashierSchema):
        return Cashier(**schema.model_dump())
