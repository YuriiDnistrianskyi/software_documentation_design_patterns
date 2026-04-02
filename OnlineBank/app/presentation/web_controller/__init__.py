from fastapi import FastAPI

from app.presentation.web_controller.home_controller import home_router
from app.presentation.web_controller.cash_account_form_controller import cash_account_form_router
from app.presentation.web_controller.top_up_router import top_up_router

def register_web_routers(app: FastAPI):
    app.include_router(home_router, tags=["web"])
    app.include_router(cash_account_form_router, tags=["web"])
    app.include_router(top_up_router, tags=["web"])
