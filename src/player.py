from __future__ import annotations
from threading import Thread
import pygame
import time
from game import Game
from assets import Assets
from conf import Ui, cc

class Player:
    def __init__(self, team: int, npc: bool = False) -> None:
        self.team = team
        self.npc = npc
        self.resources = cc.player.start
        self.pieces = []


        

class Player(Thread):
    def __init__(self, team: int, npc: bool = False) -> None:
        super().__init__()
        Game.events.next_turn += self.next_turn
        self.team = team
        self.npc = npc
        self.resources = cc.player.start
        self.pieces = []
        if self.npc:
            self.callback = self.npc_callback
        else:
            self.callback = self.player_callback

    @staticmethod
    def spawn(npcs: (bool, bool, bool) = (False, False, False)) -> None:
        Game.players = [Player(i, npc) for i, npc in enumerate(npcs)]
        for player in Game.players:
            player.setDaemon(True)
            player.start()

    def run(self) -> None:
        Game.end_game.wait()

    def player_callback(self) -> None:
        pass

    def npc_callback(self) -> None:
        Game.end_game.wait(5)
        Game.end_turn()

    def end_turn(self) -> None:
        if Game.turn == self.team:
            Game.end_turn()

    def next_turn(self) -> None:
        if self.team == Game.turn:
            print(f"Player {self.team}'s turn")
            self.callback()

    def move(self, piece: Piece, tile: Tile) -> None:
        pass

    def buy(self, piece: Piece, tile: Tile) -> None:
        pass

class Piece:
    def __init__(self, label: str) -> None:
        self.label = label
        self.surf = Assets.textures.get(self.label)

