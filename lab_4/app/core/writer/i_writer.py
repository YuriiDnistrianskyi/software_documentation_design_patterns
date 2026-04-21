from abc import ABC, abstractmethod

class IWriter(ABC):
    def write(self, data: str):
        pass
