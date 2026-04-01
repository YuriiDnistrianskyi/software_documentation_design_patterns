from fastapi import APIRouter, responses, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.controller import cash_account_controller
from app.db.dependencies import get_async_session

templates = Jinja2Templates(directory="app/presentation/templates")

top_up_router = APIRouter()

@top_up_router.get("/{bank_id}/{user_id}/top_up/{account_id}")
async def get_top_up(
        bank_id: int,
        user_id: int,
        account_id: int,
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    cash_account = await cash_account_controller.get_by_id(account_id, session)
    context: dict = {
        "account": cash_account
    }
    return templates.TemplateResponse(
        request=request, name="top_up.html", context=context)
