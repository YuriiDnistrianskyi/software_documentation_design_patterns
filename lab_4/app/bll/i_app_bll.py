from abc import ABC, abstractmethod

class IAppBll(ABC):
    @abstractmethod
    def save_data(self):
        pass
