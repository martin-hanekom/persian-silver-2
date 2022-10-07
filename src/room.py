from __future__ import annotations
import pygame
from threading import Thread
from game import Game
from conf import Ui

class Room(Thread):
    def __init__(self, parent: Room = None) -> None:
        super().__init__()
        self.parent = parent.__class__.__name__ if parent else None

    @staticmethod
    def spawn(classname: str, parent: Room = None) -> None:
        """ CamelCase classname, e.g. Menu """
        module = __import__(classname.lower())
        room = getattr(module, classname)(parent)
        room.start()
        Game.rooms.append(room)

    def run(self) -> None:
        clock = pygame.time.Clock()
        self.view.update()
        self.init()
        while self.model.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
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
            Game.screen.fill(Ui.colors['background'][0])
            self.view.draw(Game.screen)
            pygame.display.update()

    def init(self):
        """ extra room specific configuration """
        pass

    def update(self, dt: float):
        pass

    def set_model(self, **kwargs):
        self.model.set(**kwargs)
        self.view.update()
                    
    def back(self) -> None:
        if self.parent:
            Room.spawn(self.parent)
            self.model.running = False

