from __future__ import annotations
from threading import Thread
import pygame
from assets import Assets
from conf import Ui, cc

class Player(Thread):
    def __init__(self, team: int, npc: bool = False) -> None:
        super().__init__()
        self.team = team
        self.npc = npc
        self.resources = cc.player.start
        self.pieces = []

    @staticmethod
    def spawn(team: int, npc: bool = False) -> None:
        player = Player(team, npc)
        player.start()
        player.setDaemon(True)
        Game.players.append(player)

    def run(self) -> None:
        pass

    def move(self, piece: Piece, tile: Tile) -> None:
        pass

    def buy(self, piece: Piece, tile: Tile) -> None:
        pass

class Piece:
    def __init__(self, label: str) -> None:
        self.label = label
        self.surf = Assets.textures.get(self.label)

