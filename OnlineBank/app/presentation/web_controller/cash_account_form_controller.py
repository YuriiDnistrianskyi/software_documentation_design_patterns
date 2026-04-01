from fastapi import APIRouter, responses, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.bll.controller import cash_account_controller
from app.db.dependencies import get_async_session
from app.db.models.cash_account import CashAccount
from app.schemas.create_schemas import CreateCashAccountSchema
from app.schemas.update_schemas import UpdateCashAccountSchema


cash_account_form_router = APIRouter()

templates = Jinja2Templates(directory="app/presentation/templates")

@cash_account_form_router.get("/{bank_id}/{user_id}/create_cash_account")
async def get_create_cash_account_page(
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

@cash_account_form_router.post("/{bank_id}/{user_id}/create_cash_account")
async def create_cash_account(
        bank_id: int,
        user_id: int,
        number_account: str = Form(...),
        cvv: str = Form(),
        session: AsyncSession = Depends(get_async_session)
):
    cash_account_shema: CreateCashAccountSchema = CreateCashAccountSchema(
        number_account=number_account,
        balance=0.0,
        CVV=cvv,
        bank_id=bank_id,
        user_id=user_id,
    )
    cash_account = await cash_account_controller.create(cash_account_shema, session)
    return responses.RedirectResponse(f"/{bank_id}/{user_id}", status_code=302)


@cash_account_form_router.get("/{bank_id}/{user_id}/update_cash_account/{account_id}")
async def get_update_cash_account_page(
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

@cash_account_form_router.post("/{bank_id}/{user_id}/update_cash_account/{account_id}")
async def update_cash_account(
        bank_id: int,
        user_id: int,
        account_id: int,
        number_account: str = Form(...),
        cvv: str = Form(),
        session: AsyncSession = Depends(get_async_session)
):
    new_cash_account: UpdateCashAccountSchema = UpdateCashAccountSchema(
        number_account=number_account,
        __CVV=cvv
    )
    await cash_account_controller.update(account_id, new_cash_account, session)
    return responses.RedirectResponse(f"/{bank_id}/{user_id}", status_code=302)
