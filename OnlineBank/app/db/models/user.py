from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app.db.database import Base
from app.schemas.create_schemas import CreateUserSchema


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String),
    email: Mapped[str] = mapped_column(String),
    address: Mapped[str] = mapped_column(String)

    @staticmethod
    def get_columns() -> str:
        return '#user\nname;phone;email;address\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'user{i};{i};user{i}@gmail.com;some_street{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateUserSchema):
        return User(**schema.model_dump())

    @staticmethod
    def create_from_dict(data: dict):
        pass
