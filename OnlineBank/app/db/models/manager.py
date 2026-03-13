from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, DateTime
from app.db.database import Base


class Manager(Base):
    __tablename__ = 'manager'

    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    manager_key: Mapped[str] = mapped_column(String)
