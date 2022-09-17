import math, os
from dataclasses import dataclass
import pygame
from constants import *

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
        sector_angle = self.sector * math.pi / 3
        pos_angle = sector_angle + 2 * math.pi / 3
        self.x = BOARD_CENTER[0] + 2 * (TILE_SIDE + TILE_PADDING) * (self.layer * math.sin(sector_angle) + self.index * math.sin(pos_angle))
        self.y = BOARD_CENTER[1] - 2 * (TILE_SIDE + TILE_PADDING) * (self.layer * math.cos(sector_angle) + self.index * math.cos(pos_angle))

    def to_map(self, offset: (float, float) = (0, 0)):
        return (self.x + offset[0], self.y + offset[1])

    def to_coor(self):
        return (self.sector, self.layer, self.index)

    def circle_intersect(self, radius: float, pos: (float, float)):
         return math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2) <= radius
 
class Resource:
    textures: dict[str, list[pygame.Surface]] = {}
    fonts: dict[str, pygame.font.Font] = {}

    @staticmethod
    def init():
        Resource.textures = {
            "town": [pygame.image.load(os.path.join("res", "images", "buildings", f"town{i}.png")) for i in range(NUM_PLAYERS)],
            "farm": [pygame.image.load(os.path.join("res", "images", "buildings", f"farm{i}.png")) for i in range(NUM_PLAYERS)],
            "soldier": [pygame.image.load(os.path.join("res", "images", "units", f"soldier{i}.png")) for i in range(NUM_PLAYERS)]
        }
        for items in Resource.textures.values():
            for index, item in enumerate(items):
                items[index] = pygame.transform.scale(item, PIECE_SIZE).convert_alpha()
        Resource.fonts = {
            "system": pygame.font.SysFont("Calibri", 18),
            "systeml": pygame.font.SysFont("Calibri", 24),
        }
