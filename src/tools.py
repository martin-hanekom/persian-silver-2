from dataclasses import dataclass
import os
import math
import pygame
from conf import cc

class Resource:
    textures: dict[str, list[pygame.Surface]] = {}
    fonts: dict[str, pygame.font.Font] = {}

    @staticmethod
    def init():
        Resource.textures = { key: Resource.load_team_images(key) for key in cc.pieces.__dict__ }
        for key, items in Resource.textures.items():
            for index, item in enumerate(items):
                items[index] = pygame.transform.scale(item, cc.piece.size).convert_alpha()
            
        Resource.fonts = {
            "system": pygame.font.SysFont("Calibri", 18),
            "systeml": pygame.font.SysFont("Calibri", 24),
        }

    @staticmethod
    def load_team_images(item: str):
        return [pygame.image.load(os.path.join("lib", "images", f"{item}{i}.png")) for i in range(cc.player.amount)]

@dataclass
class Position:
    sector: int
    layer: int
    index: int
    x: float
    y: float

    def __init__(self, sector, layer, index):
        self.sector = sector
        self.layer = layer
        self.index = index
        sector_a = self.sector * math.pi / 3
        index_a = sector_a + 2 * math.pi / 3
        self.x = cc.board.center[0] + 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.sin(sector_a) + self.index * math.sin(index_a))
        self.y = cc.board.center[1] - 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.cos(sector_a) + self.index * math.cos(index_a))
    
    def to_map(self, offset: (float, float) = (0, 0)):
        return (self.x + offset[0], self.y + offset[1])

    def to_coor(self, offset: (int, int, int) = (0, 0, 0)):
        return (self.sector + offset[0], self.layer + offset[1], self.index + offset[2])

    def circle_intersect(self, radius: float, pos: (float, float)):
        return math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2) <= radius

@dataclass
class SpriteState:
    hover: bool = False
    selected: bool = False
    piece: any = None

