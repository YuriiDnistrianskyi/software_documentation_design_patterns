from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.bll.controller import manager_controller
from app.schemas.create_schemas import CreateManagerSchema, CreateEmployeeSchema
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

@manager_router.post('/employee')
async def create_employee(
        data: CreateEmployeeSchema,
        session: AsyncSession = Depends(get_async_session)
):
     await controller.create_employee(data, session)
     return {"message": "Employee created"}

@manager_router.delete('/employee/{obj_id}')
async def delete_employee(
        obj_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete_employee(obj_id, session)
    return {"message": "Employee deleted"}

@manager_router.patch('/approve_deposit_contract/{obj_id}')
async def approve_deposit_contract(
        obj_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.approve_deposit_contract(obj_id, session)
    return {"message": "Deposit contract approved"}

@manager_router.patch('/approve_credit_contract/{obj_id}')
async def approve_credit_contract(
        obj_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.approve_credit_contract(obj_id, session)
    return {"message": "Credit contract approved"}
