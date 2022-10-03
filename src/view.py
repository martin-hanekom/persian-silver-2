from __future__ import annotations
import pygame
from assets import Assets
from threading import Thread
from conf import Ui

class Model:
    def __init__(self, **kwargs):
        self.running = True
        self.set(**kwargs)

    def set(self, **kwargs):
        {setattr(self, key, value) for key, value in kwargs.items()}


class View:
    def __init__(self, 
            children: [View] = [],
            orient: str = 'H',
            padding: float = Ui.padding,
            spacing: float = Ui.spacing,
            anchor: (int, int) = (0, 0),  # x, y: 1 - left/top, -1 - right/bottom
            filled: bool = False,
            size: (float, float) = (0, 0),
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
        self.text = Assets.fonts[font].render(text, True, Ui.colors['text'][0]) if text else None
        self.pos = pos
        self.color = color
        self.orient = orient
        self.padding = padding
        self.spacing = spacing
        self.anchor = anchor
        self.filled = filled
        self.children = children
        self.set_model(model)
        self.box_size = self.get_box_size()
        self.size= self.get_size(size)
        self.show_if = show_if
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
        self.hover = False
        self.rect = None
        self.center = (0,0)
        self.text_center = (0,0)
        self.hook = [0,0]
        self.clicked = False

    def update(self, parent: View = None):
        if not self.enabled():
            return
        self.filled = self.filled if parent else True
        self.box_size = self.get_box_size()
        self.size= self.get_size(self.size, parent)
        self.pos = (0,0) if not parent else parent.get_pos(self)
        self.center = (self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2)
        if self.anchor[0] == 1:
            self.hook[0] = self.pos[0]
        elif self.anchor[0] == -1:
            self.hook[0] = self.pos[0] + self.size[0] - self.box_size[0]
        if self.anchor[1] == 1:
            self.hook[1] = self.pos[1]
        elif self.anchor[1] == -1:
            self.hook[1] = self.pos[1] + self.size[1] - self.box_size[1]
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

    def get_box_size(self) -> (float, float):
        enabled_children = list(filter(lambda child: child.enabled(), self.children))
        if not enabled_children:
            if self.text:
                return self.text.get_size()
            return (0, 0)
        if self.orient == 'H':
            maxVSize = max([child.size[1] for child in enabled_children])
            return (2 * self.padding + sum([child.size[0] for child in enabled_children]) + 
                    self.spacing * (len(self.children) - 1), 2 * self.padding + maxVSize)
        if self.orient == 'V':
            maxHSize = max([child.size[0] for child in enabled_children])
            return (2 * self.padding + maxHSize, 2 * self.padding +
                    sum([child.size[1] for child in enabled_children]) +
                    self.spacing * (len(self.children) - 1))

    def get_size(self, size: (float, float), parent: View = None) -> (float, float):
        if self.filled:
            return parent.size if parent else Ui.size['screen']
        return size if sum(size) > sum(self.box_size) else self.box_size

    def get_pos(self, child: View) -> (float, float):
        index = self.children.index(child)
        if index == -1:
            return (0, 0)
        enabled_children = list(filter(lambda child: child.enabled(), self.children[:index]))
        if self.orient == 'H':
            hook = (self.center[0] - self.box_size[0] / 2, self.center[1] - self.padding - child.size[1] / 2) if not sum(self.hook) else self.hook
            prevChildren = sum([child.size[0] + self.spacing for child in enabled_children])
            return (hook[0] + self.padding + prevChildren, hook[1] + self.padding)
        if self.orient == 'V':
            hook = (self.center[0] - self.padding - child.size[0] / 2, self.center[1] - self.box_size[1] / 2) if not sum(self.hook) else self.hook
            prevChildren =  sum([child.size[1] + self.spacing for child in enabled_children])
            return (hook[0] + self.padding, hook[1]+ self.padding + prevChildren)

    def set_model(self, model: dict) -> None:
        self.model = model
        if bool(self.model):
            for child in self.children:
                child.set_model(self.model)

    def enabled(self) -> bool:
        return not self.show_if or getattr(self.model, self.show_if, True)

    def mouse_motion(self, pos: (float, float)) -> None:
        if not self.enabled():
            return
        self.hover = self.rect.collidepoint(pos)
        for child in self.children:
            child.mouse_motion(pos)

    def mouse_button_down(self, pos: (float, float)) -> None:
        self.clicked = self.enabled()
        #print(f'pos: {self.pos}, clicked: {self.clicked}')
        if self.clicked:
            for child in self.children:
                child.mouse_button_down(pos)

    def mouse_button_up(self, pos: (float, float)) -> None:
        if not self.enabled():
            return
        if self.clicked and self.callback and self.rect.collidepoint(pos):
            self()
        self.clicked = False
        for child in self.children:
            child.mouse_button_up(pos)

    def __call__(self) -> None:
        self.callback(*self.args, **self.kwargs)


class Room(Thread):
    rooms: list[Room] = []
    screen: pygame.Surface = None

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def init() -> None:
        pygame.init()
        Room.screen = pygame.display.set_mode(Ui.size['screen'])
        Assets.init()
        Room.spawn('Menu')
        for room in Room.rooms:
            room.join()
        pygame.quit()

    @staticmethod
    def spawn(classname: str) -> None:
        """ CamelCase classname, e.g. Menu """
        module = __import__(classname.lower())
        room = getattr(module, classname)()
        room.start()
        Room.rooms.append(room)
        
    def run(self) -> None:
        clock = pygame.time.Clock()
        self.view.update()
        while self.model.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.back()
                elif event.type == pygame.MOUSEMOTION:
                    self.view.mouse_motion(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.view.mouse_button_down(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.view.mouse_button_up(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return self.back()
            self.update(clock.tick(Ui.fps))
            self.screen.fill(Ui.colors['background'][0])
            self.view.draw(Room.screen)
            pygame.display.update()
        Room.rooms.remove(self)

    def update(self, dt: float):
        pass

    def set_model(self, **kwargs):
        self.model.set(**kwargs)
        self.view.update()
                    
    def back(self) -> None:
        pass
