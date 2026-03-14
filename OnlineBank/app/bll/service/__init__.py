from app.dal.dao import *
from app.bll.service.orders.bank_service import BankService
from app.bll.service.orders.cash_account_service import CashAccountService
from app.bll.service.orders.cashier_service import CashierService
from app.bll.service.orders.deposit_contract_service import DepositContractService
from app.bll.service.orders.credit_contract_service import CreditContractService
from app.bll.service.orders.employee_service import EmployeeService
from app.bll.service.orders.manager_service import ManagerService
from app.bll.service.orders.user_service import UserService

bank_service = BankService(bank_dao)
cash_account_service = CashAccountService(cash_account_dao)
cashier_service = CashierService(cashier_dao)
deposit_contract_service = DepositContractService(deposit_contract_dao)
credit_contract_service = CreditContractService(credit_contract_dao)
employee_service = EmployeeService(employee_dao)
manager_service = ManagerService(manager_dao)
user_service = UserService(user_dao)
