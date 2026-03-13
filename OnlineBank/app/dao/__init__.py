from app.db.database import *
from app.dao.orders.BankDAO import BankDAO
from app.dao.orders.EmployeeDAO import EmployeeDAO
from app.dao.orders.UserDAO import UserDAO
from app.dao.orders.DepositContractDAO import DepositContractDAO
from app.dao.orders.CashierDAO import CashierDAO
from app.dao.orders.ManagerDAO import ManagerDAO
from app.dao.orders.CashAccountDAO import CashAccountDAO
from app.dao.orders.CreditContractDAO import CreditContractDAO

bank_dao = BankDAO(Bank)
employee_dao = EmployeeDAO(Employee)
user_dao = UserDAO(User)
deposit_contract_dao = DepositContractDAO(DepositContract)
cash_account_dao = CashAccountDAO(CashAccount)
cashier_dao = CashierDAO(Cashier)
manager_dao = ManagerDAO(Manager)
credit_contract_dao = CreditContractDAO(CreditContract)
