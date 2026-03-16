import asyncio
import csv
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import engine, Base
from app.dal.app_dal.interface_app_dal import IAppDal


class AppDal(IAppDal):
    def read_csv(self) -> dict:
        data_dict: dict = {}
        with open('data.csv', newline='', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('#'):
                    current_table = line[1:]
                    data_dict[current_table] = []
                else:
                    data_dict[current_table].append(line)

        print(data_dict)
        return data_dict

    async def _create_table(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def create_db(self):
        asyncio.run(self._create_table())

    def insert_data(self, session: AsyncSession, data: dict):
        pass
