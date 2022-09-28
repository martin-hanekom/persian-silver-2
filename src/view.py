import pygame
import math
import assets
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
            callback = None,
            args = [],
            kwargs = {}) -> None:
        ''' children can be sprite, rect, circle, etc. or list of '''
        self.rect = rect
        self.surf = surf
        self.text = assets.fonts[font].render(text, True, Ui.colors['text'][0]),
        self.pos = pos
        self.color = color
        self.center = center
        self.padding = padding
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.hover = False

    def init(self, parent: View = None):
        self.parent = parent
        self.pos = self.get_pos()
        self.rect = self.get_rect()

    def get_pos(self) -> (float, float):
        p = self.parent.pos if self.parent else (0, 0)
        s = self.parent.size() if self.parent else cc.video.size
        return (p[0] + self.pos[0] + self.center[0] * (s[0] - self.rect[0]) / 2,
                p[1] + self.pos[1] + self.center[1] * (s[1] - self.rect[0]) / 2)

    def get_pos(self, pos: (float, float), rect: (float, float)) -> (float, float):
        if pos:
            return pos
        elif rect:
            if self.parent:
                return (self.parent.pos[0] + self.center[0] * (self.parent.size()[0] - rect[0]) / 2,
                        self.parent.pos[1] + self.center[1] * (self.parent.size()[1] - rect[1]) / 2)
            return (self.center[0] * (cc.video.size[0] - rect[0]) / 2, self.center[1] * (cc.video.size[1] - rect[1]) / 2)

    def size(self) -> (float, float):
        if self.rect:
            return (self.rect.w, self.rect.h)
        if self.surf:
            return self.surf.get_size()

    def intersect(self, pos: (float, float)) -> bool:
        if self.rect:
            return self.rect.collidepoint(pos)
        return False

    def draw(self, screen: pygame.Surface) -> None:
        if self.rect:
            pygame.draw.rect(screen, self.color[self.hover], self.rect, border_radius=2)

    def __call__(self) -> None:
        self.callback(*self.args, **self.kwargs)
