import math
import pygame
from conf import cc

def offset(
    size: (float, float) = None,
    pos: (float, float) = (0, 0),
    rect: pygame.Rect = None,
    offset: (float, float) = (0, 0),
    center: (bool, bool) = (False, False)
) -> (float, float):
    '''
    returns the 2D offset from the shape, optionally from the center
    requires either size or rect
    '''
    if rect:
        return (rect.x + center[0] * rect.w / 2 + offset[0], rect.y + center[1] * rect.h / 2 + offset[1])
    return (pos[0] + center[0] * size[0] / 2 + offset[0], pos[1] + center[1] * size[1] / 2 + offset[1])

class Position:
    center: (float, float) = (0, 0)

    def __init__(self, sector: int, layer: int, index: int):
        self.sector = sector
        self.layer = layer
        self.index = index
        sector_a = self.sector * math.pi / 3
        index_a = sector_a + 2 * math.pi / 3
        self.x = Position.center[0] + 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.sin(sector_a) + self.index * math.sin(index_a))
        self.y = Position.center[1] - 2 * (cc.tile.side + cc.tile.padding) * (self.layer * math.cos(sector_a) + self.index * math.cos(index_a))

    @staticmethod
    def init(center: (float, float)):
        Position.center = center
    
    def to_map(self, offset: (float, float) = (0, 0)):
        return (self.x + offset[0], self.y + offset[1])

    def to_coor(self, offset: (int, int, int) = (0, 0, 0)):
        return (self.sector + offset[0], self.layer + offset[1], self.index + offset[2])

    def circle_intersect(self, radius: float, pos: (float, float)):
        return math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2) <= radius
