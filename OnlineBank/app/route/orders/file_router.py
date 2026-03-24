from fastapi import Depends, HTTPException, status, UploadFile, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_async_session
from app.core.auth import verify_token
from app.presentation.app_presentation import app_presentation

file_router = APIRouter()

@file_router.post('/read_csv')
async def read_csv(
        token: str,
        file: UploadFile,
        session: AsyncSession = Depends(get_async_session),
):
    payload = verify_token(token)
    await app_presentation.create_db_from_swagger(file, session)
    return {"message": f"Success by user {payload.get('email')}"}
