import pygame
import math
from conf import cc

class View:
    def __init__(self, 
            rect: (float, float) = None,
            surf: pygame.Surface = None,
            text: str = None,
            font: str = 'system',
            pos: (float, float) = None,
            color: list[pygame.Color] = [],
            center: (bool, bool) = (True, True),
            padding: (float, float) = (0, 0),
            children: any = None,
            parent: pygame.Surface = None,
            callback = None,
            args = [],
            kwargs = {}) -> None:
        ''' children can be sprite, rect, circle, etc. or list of '''
            self.parent = parent
            self.center = center
            self.pos = self.get_pos(pos)
            self.rect = pygame.Rect(rect, pos) if rect else None
            self.text = text
            self.font = font
            self.color = color
            self.center = center
            self.padding = padding
            self.children = children if isinstance(children, list) else [children]
            self.callback = callback
            self.args = args
            self.kwargs = kwargs
            self.hover = False

    def get_pos(self, pos: (float, float)) -> None:
        if pos:
            self.pos = pos
        else:
            if self.parent:
                self.pos = (self.parent.pos[0] + self.center[0] * self.parent.size()[0], self.parent.pos[1] + self.center[1] * self.parent.size()[1])
            else:
               self.pos = (center[0] * cc.video.size[0] / 2, center[1] * cc.video.size[1] / 2)

   def size(self) -> (float, float):
       if self.rect:
           return (self.rect.w, self.rect.h)
       if self.surf:
           return self.surf.get_size()

    def draw(self, screen: pygame.Surface) -> None:
        if self.rect:
            pygame.draw.rect(screen, self.color[self.hover], self.rect, border_radius=2)
        for child in self.children:
            child.draw(screen)

    def __call__(self) -> None:
        self.callback(*self.args, **self.kwargs)
