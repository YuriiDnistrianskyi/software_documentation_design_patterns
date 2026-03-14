from app.db.database import *
from app.dal.dao.orders.BankDAO import BankDAO
from app.dal.dao.orders.EmployeeDAO import EmployeeDAO
from app.dal.dao.orders.UserDAO import UserDAO
from app.dal.dao.orders.DepositContractDAO import DepositContractDAO
from app.dal.dao.orders.CashierDAO import CashierDAO
from app.dal.dao.orders.ManagerDAO import ManagerDAO
from app.dal.dao.orders.CashAccountDAO import CashAccountDAO
from app.dal.dao.orders.CreditContractDAO import CreditContractDAO

bank_dao = BankDAO(Bank)
employee_dao = EmployeeDAO(Employee)
user_dao = UserDAO(User)
deposit_contract_dao = DepositContractDAO(DepositContract)
cash_account_dao = CashAccountDAO(CashAccount)
cashier_dao = CashierDAO(Cashier)
manager_dao = ManagerDAO(Manager)
credit_contract_dao = CreditContractDAO(CreditContract)
