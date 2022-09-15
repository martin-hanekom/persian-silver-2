from abc import ABC, abstractmethod

class ISprite(ABC):
    @abstractmethod
    def draw(self):
        """ Draw sprite to screen """
        pass

    def update(self):
        """ Optionally update sprite """
        pass
