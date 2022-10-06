from __future__ import annotations
from threading import Thread
import pygame
from assets import Assets
from conf import Ui

class Game:
    rooms: list[Room] = []
    players: list[Player] = []
    screen: pygame.Surface = None

    @staticmethod
    def init() -> None:
        from room import Room
        from player import Player
        pygame.init()
        Game.screen = pygame.display.set_mode(Ui.size['screen'])
        Assets.init()
        Room.spawn('Menu')
        for room in Game.rooms:
            room.join()
        pygame.quit()
