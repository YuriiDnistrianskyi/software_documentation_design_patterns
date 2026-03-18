from fastapi import FastAPI
from app.route.orders.bank_routes import bank_router

def register_routers(app: FastAPI) -> None:
    app.include_router(bank_router, prefix='/bank', tags=['bank'])
