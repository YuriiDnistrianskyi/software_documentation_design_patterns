from fastapi import APIRouter, responses, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.bll.controller import cash_account_controller
from app.db.dependencies import get_async_session

templates = Jinja2Templates(directory="app/templates")

top_up_router = APIRouter()

@top_up_router.get("/{bank_id}/{user_id}/top_up/{account_id}")
async def get_top_up_page(
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

@top_up_router.post("/{bank_id}/{user_id}/top_up/{account_id}")
async def top_up_cash_account(
        bank_id: int,
        user_id: int,
        account_id: int,
        add_to_balance: Optional[float] = Form(None),
        session: AsyncSession = Depends(get_async_session)
):
    print("--" * 60)
    if add_to_balance is not None:
        await cash_account_controller.update_balance(account_id, add_to_balance, session)
    return responses.RedirectResponse(f"/{bank_id}/{user_id}", status_code=302)
