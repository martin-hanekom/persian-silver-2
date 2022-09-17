from dataclasses import dataclass
import pygame
from sprite import ISprite
from piece import Piece
from tools import Position
from constants import *

@dataclass
class Player(ISprite):
    team: int

    def __init__(self, team: int):
        self.team = team
        self.pieces = [Piece(self.team, "town", Position(self.team * 2, BOARD_LAYERS - 1, (BOARD_LAYERS - 1) // 2))]

    def draw(self, screen: pygame.Surface):
        for piece in self.pieces:
            piece.draw(screen)
    
    def mouse_move(self, mouse_pos: (float, float)):
        for piece in self.pieces:
            piece.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        for piece in self.pieces:
            piece.mouse_clicked(mouse_pos)
