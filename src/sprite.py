import pygame
import math
import utils

class Sprite:
    def __init__(self,
            rect: pygame.Rect = None,
            surf: pygame.Surface = None,
            pos: (float, float) = None,
            colors: (pygame.Color, pygame.Color) = None,
            radius: float = None,
            text: pygame.Surface = None,
            func = None,
            args = [],
            kwargs = {}) -> None:
        self.rect = rect
        self.surf = surf
        self.pos = pos
        self.colors = colors
        self.radius = radius
        self.text = text
        self.func = func
        self.args= args
        self.kwargs = kwargs
        self.hover = False

    def draw(self, screen: pygame.Surface) -> None:
        if self.rect:
            pygame.draw.rect(screen, self.colors[self.hover], self.rect, border_radius=2)
            if self.text:
                size = self.text.get_size()
                screen.blit(self.text, utils.offset(rect=self.rect, offset=(-size[0] / 2, -size[1] / 2), center=(True, True)))
        elif self.surf:
            size = self.surf.get_size()
            screen.blit(self.surf, utils.offset(size=size, pos=self.pos))

    def intersect(self, pos: (float, float)) -> bool:
        ''' check if rect or surface intersects with point '''
        if self.rect:
            return self.rect.collidepoint(pos)
        elif self.radius:
            return math.dist(pos, self.pos) <= self.radius
        return False

    def __call__(self) -> None:
        self.func(*self.args, **self.kwargs)
