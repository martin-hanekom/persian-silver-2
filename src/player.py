from __future__ import annotations
from threading import Thread
import pygame
import time
from game import Game
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
    def spawn(npcs: (bool, bool, bool) = (False, False, False)) -> None:
        Game.players = [Player(i, npc) for i, npc in enumerate(npcs)]
        for player in Game.players:
            player.setDaemon(True)
            player.start()

    def run(self) -> None:
        while not Game.end_game.isSet():
            if self.team == Game.turn:
                print(f"Player {self.team}'s turn")
                time.sleep(5)
                Game.next_turn()
            else:
                turner = Game.turn_event.wait()
                if self.team == Game.turn:
                    Game.turn_event.clear()

    def move(self, piece: Piece, tile: Tile) -> None:
        pass

    def buy(self, piece: Piece, tile: Tile) -> None:
        pass

class Piece:
    def __init__(self, label: str) -> None:
        self.label = label
        self.surf = Assets.textures.get(self.label)

