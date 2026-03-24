from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.dependencies import get_async_session
from app.db.models.user import User
from app.schemas.auth_schemas import *
from app.core.auth import *

auth_router = APIRouter()

@auth_router.post('/login')
async def login(
        data: LoginUserSchema,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        stmt = select(User).where(User.email == data.email)
        _list = await session.execute(stmt)
        user = _list.scalars().one()

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")

        if user.password != data.password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect")

        token = create_access_token(user_id=user.id, email=user.email)
        return {'access_token': token}

    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Some")
