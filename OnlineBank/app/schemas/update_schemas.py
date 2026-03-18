import datetime
from pydantic import BaseModel
from typing import Optional

class UpdateBankSchema(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class UpdateCashAccountSchema(BaseModel):
    number: Optional[str] = None
    balance: Optional[float] = None
    __CVV: Optional[float] = None
    opening_date: Optional[datetime.datetime] = None
    user_id: Optional[int] = None
    bank_id: Optional[int] = None

class UpdateCashierSchema(BaseModel):
    employee_id: Optional[int] = None
    cashier_key: Optional[str] = None

class UpdateDepositContractSchema(BaseModel):
    interest: Optional[int] = None
    cash_account_id: Optional[int] = None
    amount_of_money: Optional[float] = None
    opening_date: Optional[datetime.datetime] = None
    closing_date: Optional[datetime.datetime] = None

class UpdateCreditContractSchema(BaseModel):
    interest: Optional[int] = None
    cash_account_id: Optional[int] = None
    amount_of_money: Optional[float] = None
    opening_date: Optional[datetime.datetime] = None
    closing_date: Optional[datetime.datetime] = None

class UpdateEmployeeSchema(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    date_of_hire: Optional[datetime.datetime] = None

class UpdateUserSchema(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class UpdateManagerSchema(BaseModel):
    employee_id: Optional[int] = None
    manager_key: Optional[int] = None
