from abc import ABC, abstractmethod

class IAppDal(ABC):
    @abstractmethod
    def read_csv(self) -> dict:
        pass

    @abstractmethod
    async def _create_table(self):
        pass

    @abstractmethod
    def create_db(self):
        pass

    @abstractmethod
    def insert_data(self, data: dict):
        pass
