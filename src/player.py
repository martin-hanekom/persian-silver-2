from __future__ import annotations
from threading import Thread
import pygame
from conf import Ui

class Player(Thread):
    def __init__(self, team: int, npc: bool = False) -> None:
        super().__init__()
        self.team = team
        self.npc = npc

    @staticmethod
    def spawn(team: int, npc: bool = False) -> None:
        player = Player(team, npc)
        player.start()
        player.setDaemon(True)
        Game.players.append(player)

    def run(self) -> None:
        pass
