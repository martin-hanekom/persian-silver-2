import os
from dataclasses import dataclass
import pygame
from sprite import ISprite
from tools import Position
from constants import *

class IPiece:
    textures: dict[str, list[pygame.Surface]] = {}
    texture: pygame.Surface
    hover: bool
    selected: bool

    def __init__(self):
        self.hover = False
        self.selected = False

    @staticmethod
    def load():
        IPiece.textures = {
            "town": [pygame.image.load(os.path.join("res", "images", "buildings", f"town{i}.png")) for i in range(NUM_PLAYERS)],
        }
        for items in IPiece.textures.values():
            for index, item in enumerate(items):
                items[index] = pygame.transform.scale(item, PIECE_SIZE).convert_alpha()

    def create(team: int, pos: Position, piece: str = "town"):
        match piece:
            case "town":
                return Town(team, pos)

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
        
@dataclass
class Town(IPiece, ISprite):
    team: int
    pos: Position
    
    def __init__(self, team: int, pos: Position):
        super().__init__()
        self.team = team
        self.pos = pos
        self.texture = IPiece.textures.get("town")[self.team]
