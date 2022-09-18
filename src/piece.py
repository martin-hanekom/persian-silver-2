from dataclasses import dataclass
import pygame
from tools import Position, Resource

@dataclass
class Piece:
    label: str
    team: int
    pos: Position
    sprite: pygame.Surface

    def __init__(self, label: str, team: int, pos: Position):
        self.label = label
        self.team = team
        self.pos = pos
        self.sprite = Resource.textures.get(self.label)[self.team]

