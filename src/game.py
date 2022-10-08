from __future__ import annotations
import threading
import events
import pygame
from assets import Assets
from conf import Ui, cc

class Game:
    events: events.Events = events.Events(('next_turn',))
    rooms: list[Room] = []
    players: list[Player] = []
    screen: pygame.Surface = None
    turn: int = 0
    end_game: threading.Event = threading.Event()

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

    def end_turn() -> None:
        Game.turn = (Game.turn + 1) % cc.player.amount
        Game.events.next_turn()
