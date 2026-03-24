from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

class Base(DeclarativeBase):
    pass

from app.db.models.bank import Bank
from app.db.models.cash_account import CashAccount
from app.db.models.cashier import Cashier
from app.db.models.deposit_contract import DepositContract
from app.db.models.credit_contract import CreditContract
from app.db.models.employee import Employee
from app.db.models.manager import Manager
from app.db.models.user import User
