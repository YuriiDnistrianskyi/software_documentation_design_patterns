from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import cashier_controller
from app.schemas.create_schemas import CreateCashierSchema
from app.schemas.update_schemas import UpdateCashierSchema

cashier_router = APIRouter()
controller = cashier_controller

@cashier_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'cahiers': result}

@cashier_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'cahier': obj.to_dict()}

@cashier_router.post('/')
async def create(
        data: CreateCashierSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'cashier': new_obj.to_dict()}

@cashier_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateCashierSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@cashier_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
