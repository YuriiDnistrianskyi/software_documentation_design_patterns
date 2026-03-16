import asyncio
from app.db.database import engine, Base
from app.dal.app_dal.interface_app_dal import IAppDal


class AppDal(IAppDal):
    def read_csv(self):
        print("read cvs")

    async def _create_table(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def create_db(self):
        asyncio.run(self._create_table())
