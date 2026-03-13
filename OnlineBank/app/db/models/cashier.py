from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from app.db.database import Base


class Cashier(Base):
    __tablename__ = 'cashier'

    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    cashier_key: Mapped[str] = mapped_column(String)
