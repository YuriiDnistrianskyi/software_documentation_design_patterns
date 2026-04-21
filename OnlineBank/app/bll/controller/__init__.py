from app.bll.service import *
from app.bll.controller.orders.bank_controller import BankController
from app.bll.controller.orders.cash_account_controller import CashAccountController
from app.bll.controller.orders.cashier_controller import CashierController
from app.bll.controller.orders.deposit_contract_controller import DepositContractController
from app.bll.controller.orders.credit_contract_controller import CreditContractController
from app.bll.controller.orders.employee_controller import EmployeeController
from app.bll.controller.orders.manager_controller import ManagerController
from app.bll.controller.orders.user_controller import UserController

bank_controller = BankController(bank_service)
cash_account_controller = CashAccountController(cash_account_service)
cashier_controller = CashierController(cashier_service)
deposit_contract_controller = DepositContractController(deposit_contract_service)
credit_contract_controller = CreditContractController(credit_contract_service)
employee_controller = EmployeeController(employee_service)
manager_controller = ManagerController(manager_service)
user_controller = UserController(user_service)
