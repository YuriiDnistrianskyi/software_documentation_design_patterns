from fastapi import APIRouter, Request, Depends, responses, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_async_session
from app.db.database import User, Bank, CashAccount
from app.bll.controller import user_controller, cash_account_controller, bank_controller
from app.schemas.create_schemas import CreateCashAccountSchema

home_router = APIRouter()

templates = Jinja2Templates(directory="app/presentation/templates")

@home_router.get("/{bank_id}/{user_id}")
async def home(
        bank_id: int,
        user_id: int,
        request: Request,
        session: AsyncSession = Depends(get_async_session)
    ):
    bank: Bank = await bank_controller.get_by_id(bank_id, session)
    user: User = await user_controller.get_by_id(user_id, session)
    cash_accounts: list = await cash_account_controller.get_cash_accounts_by_user_id(user_id, session)

    context: dict = {
        'bank': bank,
        'user': user,
        'cash_accounts': cash_accounts
    }
    return templates.TemplateResponse(
        request=request, name='home.html', context=context,
    )

@home_router.delete("/delete/{account_id}")
async def delete_cash_account(
        account_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await cash_account_controller.delete(account_id, session)
    return {"message": "Cash account deleted"}
