from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.presentation.controller import credit_contract_controller
from app.schemas.create_schemas import CreateCreditContractSchema
from app.schemas.update_schemas import UpdateCreditContractSchema

credit_contract_router = APIRouter()
controller = credit_contract_controller

@credit_contract_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'credit_contracts': result}

@credit_contract_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'credit_contract': obj.to_dict()}

@credit_contract_router.post('/')
async def create(
        data: CreateCreditContractSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'credit_contract': new_obj.to_dict()}

@credit_contract_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateCreditContractSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@credit_contract_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
