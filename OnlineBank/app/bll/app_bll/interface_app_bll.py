from abc import ABC, abstractmethod

class IAppBll(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    @abstractmethod
    def create_table(self):
        pass
