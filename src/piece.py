from dataclasses import dataclass
import pygame
from tools import Position, Resource

@dataclass
class Piece:
    label: str
    team: int
    pos: Position
    sprite: pygame.Surface = Resource.textures.get(label)[team]

