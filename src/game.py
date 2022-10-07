from __future__ import annotations
from threading import Thread, Event
import pygame
from assets import Assets
from conf import Ui, cc

class Game:
    rooms: list[Room] = []
    players: list[Player] = []
    screen: pygame.Surface = None
    turn: int = 0
    turn_event: Event = Event()
    end_game: Event = Event()

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

    def next_turn() -> None:
        Game.turn = (Game.turn + 1) % cc.player.amount
        Game.turn_event.set()
