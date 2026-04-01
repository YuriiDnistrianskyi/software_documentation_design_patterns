from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_async_session
from app.db.database import User, Bank, CashAccount
from app.bll.controller import user_controller, cash_account_controller, bank_controller, cash_account_controller

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

@home_router.get("/{bank_id}/{user_id}/create_cash_account")
async def create_cash_account_page(
        bank_id: int,
        user_id: int,
        request: Request,
):
    context: dict = {
        'type': 'Create',
        'bank_id': bank_id,
        'user_id': user_id,
    }

    return templates.TemplateResponse(
        request=request, name='cash_account_form.html', context=context,
    )

@home_router.get("/{bank_id}/{user_id}/update_cash_account/{account_id}")
async def update_cash_account_page(
        bank_id: int,
        user_id: int,
        account_id: int,
        request: Request,
        session: AsyncSession = Depends(get_async_session)
):
    cash_account: CashAccount = await cash_account_controller.get_by_id(account_id, session)

    context: dict = {
        'type': 'Update',
        'cash_account': cash_account,
        'bank_id': bank_id,
        'user_id': user_id,
    }
    return templates.TemplateResponse(
        request=request, name='cash_account_form.html', context=context,
    )
