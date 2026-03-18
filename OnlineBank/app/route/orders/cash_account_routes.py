from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import cash_account_controller
from app.schemas.create_schemas import CreateCashAccountSchema
from app.schemas.update_schemas import UpdateCashAccountSchema

cash_account_router = APIRouter()
controller = cash_account_controller

@cash_account_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'cash_accounts': result}

@cash_account_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'cash_account': obj.to_dict()}

@cash_account_router.post('/')
async def create(
        data: CreateCashAccountSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'cash_account': new_obj.to_dict()}

@cash_account_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateCashAccountSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@cash_account_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
