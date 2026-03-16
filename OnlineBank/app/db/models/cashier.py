from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from app.db.database import Base


class Cashier(Base):
    __tablename__ = 'cashier'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    cashier_key: Mapped[str] = mapped_column(String)
