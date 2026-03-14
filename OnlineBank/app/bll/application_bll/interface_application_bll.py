from abc import ABC, abstractmethod

class IApplicationBll(ABC):
    @abstractmethod
    def read_csv(self):
        pass

    def create_table(self):
        pass
