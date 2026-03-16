from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from app.db.database import Base

class Bank(Base):
    __tablename__ = 'bank'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
