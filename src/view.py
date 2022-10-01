from __future__ import annotations
import pygame
import math
import assets
from conf import cc, Ui

class View:
    def __init__(self, 
            children: [View] = [],
            orient: str = 'H',
            padding: float = Ui.padding,
            spacing: float = Ui.spacing,
            size: (float, float) = None,
            surf: pygame.Surface = None,
            text: str = None,
            font: str = 'system',
            pos: (float, float) = None,
            color: list[pygame.Color] = None,
            model: dict = {},
            show_if: str = None,
            callback = None,
            args = [],
            kwargs = {}) -> None:
        self.surf = surf
        self.text = assets.fonts[font].render(text, True, Ui.colors['text'][0]) if text else None
        self.pos = pos
        self.color = color
        self.orient = orient
        self.padding = padding
        self.spacing = spacing
        self.children = children
        self.size = size if size else self.get_size()
        self.model = model
        self.show_if = show_if
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.hover = False
        self.rect = None
        self.center = (0,0)
        self.text_center = (0,0)

    def update(self, parent: View = None):
        if parent and not bool(self.model):
            self.model = parent.model
        if not self.enabled():
            return
        self.pos = (cc.video.center[0] - self.size[0] / 2, cc.video.center[1] - self.size[1] / 2) if parent is None else parent.get_pos(self)
        self.center = (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2)
        if not self.color:
            self.color = parent.color if parent else Ui.colors['background']
        if self.text:
            text_size = self.text.get_size()
            self.text_center = (self.center[0] - text_size[0] / 2, self.center[1] - text_size[1] / 2)
        self.rect = pygame.Rect(self.pos, self.size)
        for child in self.children:
            child.update(self)

    def draw(self, screen: pygame.Surface) -> None:
        if not self.enabled():
            return
        pygame.draw.rect(screen, self.color[self.hover], self.rect, border_radius=2)
        if self.text:
            screen.blit(self.text, self.text_center)
        for child in self.children:
            child.draw(screen)

    def get_size(self) -> (float, float):
        if not self.children:
            if self.text:
                return self.text.get_size()
            return (0, 0)
        if self.orient == 'H':
            maxVSize = max([child.size[1] for child in self.children])
            return (2 * self.padding + sum([child.size[0] for child in self.children]) + 
                    self.spacing * (len(self.children) - 1), 2 * self.padding + maxVSize)
        if self.orient == 'V':
            maxHSize = max([child.size[0] for child in self.children])
            return (2 * self.padding + maxHSize, 2 * self.padding +
                    sum([child.size[1] for child in self.children]) +
                    self.spacing * (len(self.children) - 1))

    def get_pos(self, child: View) -> (float, float):
        index = self.children.index(child)
        if index == -1:
            return (0, 0)
        if self.orient == 'H':
            prevChildren = sum([child.size[0] + self.spacing for child in self.children[:index] if child.enabled()])
            return (self.pos[0] + self.padding + prevChildren, self.pos[1] + self.padding)
        if self.orient == 'V':
            prevChildren =  sum([child.size[1] + self.spacing for child in self.children[:index] if child.enabled()])
            return (self.pos[0] + self.padding, self.pos[1] + self.padding + prevChildren)

    def enabled(self) -> bool:
        return not self.show_if or self.model.get(self.show_if)

    def mouse_move(self, pos: (float, float)) -> None:
        if not self.enabled():
            return
        self.hover = self.rect.collidepoint(pos)
        for child in self.children:
            child.mouse_move(pos)

    def mouse_click(self, pos: (float, float)) -> None:
        if not self.enabled():
            return
        if self.callback and self.rect.collidepoint(pos):
            self()
        for child in self.children:
            child.mouse_click(pos)

    def __call__(self) -> None:
        self.callback(*self.args, **self.kwargs)
