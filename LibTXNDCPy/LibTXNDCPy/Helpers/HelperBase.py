from abc import ABC

class HelperBase(ABC):
    """Base Helper class"""
    pass
    
    @abstractmethod
    def toNDCSample(self):
        pass
    
    