from fastapi import FastAPI

from app.presentation.web_controller.home_controller import home_router

def register_web_routers(app: FastAPI):
    app.include_router(home_router)