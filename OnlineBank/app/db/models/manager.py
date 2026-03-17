from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base
from app.schemas.create_schemas import CreateManagerSchema


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    manager_key: Mapped[str] = mapped_column(String)

    @staticmethod
    async def create_from_schema(schema: CreateManagerSchema):
        return Manager(**schema.model_dump())
