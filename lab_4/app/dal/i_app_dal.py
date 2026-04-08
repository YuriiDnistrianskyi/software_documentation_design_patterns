from abc import ABC, abstractmethod

class IAppDal(ABC):
    @abstractmethod
    def read_data_source(self):
        pass

    @abstractmethod
    def write_data(self):
        pass
