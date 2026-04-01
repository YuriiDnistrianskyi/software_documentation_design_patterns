from fastapi import FastAPI
from app.route.orders.bank_routes import bank_router
from app.route.orders.cash_account_routes import cash_account_router
from app.route.orders.cashier_routes import cashier_router
from app.route.orders.deposit_contract_routes import deposit_contract_router
from app.route.orders.credit_contract_routes import credit_contract_router
from app.route.orders.employee_routes import employee_router
from app.route.orders.manager_routes import manager_router
from app.route.orders.user_routes import user_router
from app.route.orders.auth_routes import auth_router
from app.route.orders.file_router import file_router


def register_routers(app: FastAPI) -> None:
    app.include_router(bank_router, prefix='/bank', tags=['bank'])
    app.include_router(cash_account_router, prefix='/cash_account', tags=['cash_account'])
    app.include_router(cashier_router, prefix='/cashier', tags=['cashier'])
    app.include_router(deposit_contract_router, prefix='/deposit_contract', tags=['deposit_contract'])
    app.include_router(credit_contract_router, prefix='/credit_contract', tags=['credit_contract'])
    app.include_router(employee_router, prefix='/employee', tags=['employee'])
    app.include_router(manager_router, prefix='/manager', tags=['manager'])
    app.include_router(user_router, prefix='/user', tags=['user'])
    app.include_router(auth_router, prefix='/auth', tags=['auth'])
    app.include_router(file_router, prefix='/file', tags=['file'])
