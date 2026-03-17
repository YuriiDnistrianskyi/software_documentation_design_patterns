import datetime
from pydantic import BaseModel

class CreateBankSchema(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class CreateCashAccountSchema(BaseModel):
    number: str
    balance: float
    __CVV: float
    opening_date: datetime
    user_id: int
    bank_id: int

class CreateCashierSchema(BaseModel):
    employee_id: int
    cashier_key: str

class CreateDepositContractSchema(BaseModel):
    interest: int
    cash_account_id: int
    amount_of_money: float
    opening_date: datetime
    closing_date: datetime

class CreateCreditContractSchema(BaseModel):
    interest: int
    cash_account_id: int
    amount_of_money: float
    opening_date: datetime
    closing_date: datetime

class CreateEmployeeSchema(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    date_of_hire: datetime.datetime

class CreateUserSchema(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class CreateManagerSchema(BaseModel):
    employee_id: int
    manager_key: int

