from app.db.database import async_session

async def get_async_session():
    with async_session() as session:
        yield session
