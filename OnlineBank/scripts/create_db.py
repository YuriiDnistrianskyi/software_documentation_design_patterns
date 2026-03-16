from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.app_presentation import app_presentation
from app.db.dependencies import get_async_session

def main(session: AsyncSession=get_async_session):
    result_create_db = app_presentation.create_db(session)
    if not result_create_db:
        return
    print('-' * 20)
    print('Table created')

if __name__ == '__main__':
    main()
