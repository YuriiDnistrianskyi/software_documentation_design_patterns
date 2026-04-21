from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from app.db.database import Base
from app.schemas.create_schemas import CreateBankSchema

class Bank(Base):
    __tablename__ = 'bank'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
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
        return '#bank\nid;name;phone;email;address\n'

    @staticmethod
    def get_string(i: int) -> str:
        return f'{i};bank{i};phone{i};bank{i}@bank.com;some_street{i}\n'

    @staticmethod
    async def create_from_schema(schema: CreateBankSchema):
        return Bank(**schema.model_dump())
