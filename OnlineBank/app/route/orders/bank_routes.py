from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import bank_controller
from app.schemas.create_schemas import CreateBankSchema
from app.schemas.update_schemas import UpdateBankSchema

bank_router = APIRouter()
controller = bank_controller

@bank_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await bank_controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'banks': result}

@bank_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await bank_controller.get_by_id(_id, session)
    return {'bank': obj.to_dict()}

@bank_router.post('/')
async def create(
        data: CreateBankSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await bank_controller.create(data, session)
    return {'bank': new_obj.to_dict()}

@bank_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateBankSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await bank_controller.update(_id, data, session)
    return {'massage': "Updated"}

@bank_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await bank_controller.delete(_id, session)
    return {'massage': "Deleted"}
