import math
from dataclasses import dataclass
import pygame
from sprite import ISprite
from constants import *

# (sector, layer, pos)
# [
#   [
#       [
#           (0, 1, 0),
#       ],
#       [
#           (0, 2, 0),
#           (0, 2, 1),
#       ],
#       ...
#   ],
#   [
#       [
#           (1, 1, 0),
#       ],
#       [
#           (1, 2, 0),
#           (1, 2, 1),
#       ],
#       ...
#   ],
#   ...
# ]

@dataclass
class Board(ISprite):
    def __init__(self):
        pass

    def get_sector_tile(self, sector: int, 

    def draw(self):
        pass

@dataclass
class Tile:
    pos: (float, float)
    color: (int, int, int)

    def get_pos(self, angle: float) -> (float, float):
        """ get tuple pos from radius and arbitrary angle """
        return (math.ceil(self.pos[0] + TILE_RADIUS * math.cos(angle)), math.ceil(self.pos[1] + TILE_RADIUS * math.sin(angle)))

    def points(self) -> [(float, float)]:
        """ use center pos to get polygon points """
        angle = -math.pi / 3
        while True:
            first_pos = self.get_pos(angle)
            angle += (math.pi / 3) % (2 * math.pi)
            second_pos = self.get_pos(angle)
            yield [self.pos, first_pos, second_pos]

    def draw(self, screen: pygame.Surface):
        points = self.points()
        for i in range(6):
            pygame.draw.polygon(screen, self.color, next(points))


class Board:
    def __init__(self):
        self.screen_center = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
        self.tiles = [Tile(self.screen_center, TILE_COLOR)]
        layer = 1
        angle = math.pi / 6
        while layer <= BOARD_LAYERS:
           self.tiles.append(Tile(self.get_center_pos(layer, angle), TILE_COLOR))
           angle += math.pi / 3
           if angle >= 2 * math.pi:
               layer += 1
               angle = math.pi / 6

    def get_center_pos(self, layer: int, angle: float) -> (float, float):
        return (math.ceil(self.screen_center[0] + (TILE_SIDE + TILE_PADDING) * layer * 2 * math.cos(angle)),
                math.ceil(self.screen_center[1] + (TILE_SIDE + TILE_PADDING) * layer * 2 * math.sin(angle)))

    def draw(self, screen: pygame.Surface):
        for tile in self.tiles:
            tile.draw(screen)

