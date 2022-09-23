from abc import ABC, abstractmethod

class ISprite(ABC):
    @abstractmethod
    def draw(self):
        """ Draw sprite to screen """
        pass

    def update(self):
        """ Optionally update sprite """
        pass

    def mouse_move(self, mouse_pos: (float, float)):
        """ React to mouse movement """
        pass

    def mouse_click(self, mouse_pos: (float, float)):
        """ React to mouse click """
        pass
