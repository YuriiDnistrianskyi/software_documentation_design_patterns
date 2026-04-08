from abc import ABC, abstractmethod

class IAppDal(ABC):
    @abstractmethod
    def read(self):
        pass
