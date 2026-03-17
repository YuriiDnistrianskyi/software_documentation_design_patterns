from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from app.db.database import Base
from app.schemas.create_schemas import CreateEmployeeSchema


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    date_of_hire: Mapped[DateTime] = mapped_column(DateTime)

    @staticmethod
    async def create_from_schema(schema: CreateEmployeeSchema):
        return Employee(**schema.model_dump())
