from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import manager_controller
from app.schemas.create_schemas import CreateManagerSchema
from app.schemas.update_schemas import UpdateManagerSchema

manager_router = APIRouter()
controller = manager_controller

@manager_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'managers': result}

@manager_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'manager': obj.to_dict()}

@manager_router.post('/')
async def create(
        data: CreateManagerSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'manager': new_obj.to_dict()}

@manager_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateManagerSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@manager_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
