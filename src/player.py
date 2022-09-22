from dataclasses import dataclass
import pygame
from piece import Piece
from tools import Position
from conf import cc

@dataclass
class Player:
    team: int
    pieces: list[Piece]

    def __init__(self, team: int):
        self.team = team
        self.pieces = [Piece("town", self.team, 
                Position(self.team * cc.board.sectors / cc.player.amount,
                    cc.board.layers - 1,
                    (cc.board.layers - 1) // 2))]

    def __repr__(self):
        return f"{self.team}: {self.pieces}"

    def draw(self, screen: pygame.Surface):
        for piece in self.pieces:
            piece.draw(screen)
    
    def mouse_move(self, mouse_pos: (float, float)):
        for piece in self.pieces:
            piece.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        for piece in self.pieces:
            piece.mouse_clicked(mouse_pos)
