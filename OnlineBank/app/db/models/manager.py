from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base
from app.schemas.create_schemas import CreateManagerSchema


class Manager(Base):
    __tablename__ = 'manager'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employee.id'))
    manager_key: Mapped[str] = mapped_column(String)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'manager_key': self.manager_key,
        }

    @staticmethod
    def get_columns() -> str:
        return '#manager\nemployee_id;manager_key\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};key_{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateManagerSchema):
        return Manager(**schema.model_dump())
