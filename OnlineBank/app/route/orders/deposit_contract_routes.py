from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_async_session
from app.bll.controller import deposit_contract_controller
from app.schemas.create_schemas import CreateDepositContractSchema
from app.schemas.update_schemas import UpdateDepositContractSchema

deposit_contract_router = APIRouter()
controller = deposit_contract_controller

@deposit_contract_router.get('/')
async def get_all(
        session: AsyncSession = Depends(get_async_session)
):
    objects = await controller.get_all(session)
    result = [obj.to_dict() for obj in objects]
    return {'deposit_contracts': result}

@deposit_contract_router.get('/{_id}')
async def get_by_id(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    obj = await controller.get_by_id(_id, session)
    return {'deposit_contract': obj.to_dict()}

@deposit_contract_router.post('/')
async def create(
        data: CreateDepositContractSchema,
        session: AsyncSession = Depends(get_async_session),
):
    new_obj = await controller.create(data, session)
    return {'deposit_contract': new_obj.to_dict()}

@deposit_contract_router.patch('/{_id}')
async def update(
        _id: int,
        data: UpdateDepositContractSchema,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.update(_id, data, session)
    return {'massage': "Updated"}

@deposit_contract_router.delete('/{_id}')
async def delete(
        _id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await controller.delete(_id, session)
    return {'massage': "Deleted"}
