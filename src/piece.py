import os
from dataclasses import dataclass
import pygame
import game
from sprite import ISprite
from tools import Position, Resource
from constants import *

@dataclass
class Piece(ISprite):
    texture: pygame.Surface
    team: int
    pos: Position
    label: str
    hover: bool
    selected: bool

    def __init__(self, team: int, label: str, pos: Position = Position(0, 0, 0)):
        self.hover = False
        self.selected = False
        self.team = team
        self.pos = pos
        self.label = label
        self.texture = Resource.textures.get(self.label)[self.team]

    def draw(self, screen: pygame.Surface):
        offset = (-PIECE_SIZE[0] / 2, -PIECE_SIZE[1] / 2)
        if self.hover:
            self.texture.set_alpha(200)
        else:
            self.texture.set_alpha(255)
        screen.blit(self.texture, self.pos.to_map(offset))

    def mouse_move(self, mouse_pos: (float, float)):
        self.hover = self.pos.circle_intersect(PIECE_SIZE[0] / 2, mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.selected = self.pos.circle_intersect(PIECE_SIZE[0] / 2, mouse_pos)
        if self.selected:
            game.game.select(self) 
