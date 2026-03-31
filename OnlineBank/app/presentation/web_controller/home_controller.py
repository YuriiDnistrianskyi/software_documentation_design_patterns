from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

home_router = APIRouter()

templates = Jinja2Templates(directory="app/presentation/templates")

@home_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
            request=request, name='home.html'
    )
