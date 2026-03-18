from app.db.database import *
from app.dal.dao.orders.bank_dao import BankDAO
from app.dal.dao.orders.employee_dao import EmployeeDAO
from app.dal.dao.orders.user_dao import UserDAO
from app.dal.dao.orders.deposit_contract_dao import DepositContractDAO
from app.dal.dao.orders.cashier_dao import CashierDAO
from app.dal.dao.orders.manager_dao import ManagerDAO
from app.dal.dao.orders.cash_account_dao import CashAccountDAO
from app.dal.dao.orders.credit_contract_dao import CreditContractDAO

bank_dao = BankDAO()
employee_dao = EmployeeDAO()
user_dao = UserDAO()
deposit_contract_dao = DepositContractDAO()
cash_account_dao = CashAccountDAO()
cashier_dao = CashierDAO()
manager_dao = ManagerDAO()
credit_contract_dao = CreditContractDAO()
