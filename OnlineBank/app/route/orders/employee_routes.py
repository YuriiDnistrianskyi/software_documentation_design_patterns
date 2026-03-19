from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import employee_controller
from app.schemas.create_schemas import CreateEmployeeSchema
from app.schemas.update_schemas import UpdateEmployeeSchema

employee_router = APIRouter()
controller = employee_controller

@employee_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'employees': result}

@employee_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'employee': obj.to_dict()}

@employee_router.post('/')
async def create(
        data: CreateEmployeeSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'employee': new_obj.to_dict()}

@employee_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateEmployeeSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@employee_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
