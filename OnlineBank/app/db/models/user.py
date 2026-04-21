from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app.db.database import Base
from app.schemas.create_schemas import CreateUserSchema


class User(Base):
    __tablename__ = '_user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
        }

    @staticmethod
    def get_columns() -> str:
        return '#_user\nid;name;phone;email;password;address\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};user{i};{i};user{i}@gmail.com;password{i};some_street{i}\n'

    @staticmethod
    def create_from_dict(data: dict):
        pass

    @staticmethod
    async def create_from_schema(schema: CreateUserSchema):
        return User(**schema.model_dump())
