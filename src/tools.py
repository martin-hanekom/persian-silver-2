from dataclasses import dataclass
import pygame
from conf import cc

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
        self.index = self.index
        sector_a = self.sector * math.pi / 3
        index_a = sector_a + 2 * math.pi / 3
        x = cc.board.center[0] + 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.sin(sector_a) + self.index * math.sin(index_a))
        y = cc.board.center[1] - 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.cos(sector_a) + self.index * math.cos(index_a))
    
    def to_map(self, offset: tuple(float, float) = (0, 0)):
        return (self.x + offset[0], self.y + offset[1])

    def to_coor(self, offset: tuple(int, int, int) = (0, 0, 0)):
        return (self.sector + offset[0], self.layer + offset[1], self.index + offset[2])

    def circle_intersect(self, radius: float, pos: (float, float)):
        return math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2) <= radius

