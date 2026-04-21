from fastapi import FastAPI
from app.route import register_routers
from app.presentation.web_controller import register_web_routers

def create_app() -> FastAPI:
    app = FastAPI()
    register_routers(app)
    register_web_routers(app)
    return app
