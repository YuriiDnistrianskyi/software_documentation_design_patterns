from app.db.database import *
from app.dal.dao.orders.bank_dao import BankDAO
from app.dal.dao.orders.employee_dao import EmployeeDAO
from app.dal.dao.orders.user_dao import UserDAO
from app.dal.dao.orders.deposit_contract_dao import DepositContractDAO
from app.dal.dao.orders.cashier_dao import CashierDAO
from app.dal.dao.orders.manager_dao import ManagerDAO
from app.dal.dao.orders.cash_account_dao import CashAccountDAO
from app.dal.dao.orders.credit_contract_dao import CreditContractDAO

bank_dao = BankDAO(Bank)
employee_dao = EmployeeDAO(Employee)
user_dao = UserDAO(User)
deposit_contract_dao = DepositContractDAO(DepositContract)
cash_account_dao = CashAccountDAO(CashAccount)
cashier_dao = CashierDAO(Cashier)
manager_dao = ManagerDAO(Manager)
credit_contract_dao = CreditContractDAO(CreditContract)
