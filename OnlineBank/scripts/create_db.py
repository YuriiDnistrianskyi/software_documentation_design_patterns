import asyncio
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.app_presentation import app_presentation
from app.db.dependencies import get_async_session

async def main():
    async for session in get_async_session():
        print('Creating db')
        print('...')
        result_create_db = await app_presentation.create_db(session)
        print('-' * 20)
        print('Create db success ✅' if result_create_db else 'Create db fail ⛔')

if __name__ == '__main__':
    asyncio.run(main())
