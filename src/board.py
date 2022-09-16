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
        # sector: i, layer: j, pos: k
        self.tiles = [[[Tile((0, 0, 0))]]] + [[[Tile((sector, layer, index)) for index in range(layer)]
            for layer in range(1, BOARD_LAYERS + 1)]
            for sector in range(BOARD_SECTORS)]

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        for sector in self.tiles:
            for layer in sector:
                for tile in layer:
                    tile.draw(screen, font)

    def mouse_move(self, mouse_pos: (float, float)):
        for sector in self.tiles:
            for layer in sector:
                for tile in layer:
                    tile.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        for sector in self.tiles:
            for layer in sector:
                for tile in layer:
                    tile.mouse_clicked(mouse_pos)

@dataclass
class Tile(ISprite):
    pos: (int, int, int)
    center: (float, float)
    points: [((float, float), (float, float), (float, float))]
    color: (int, int, int)
    hover: bool
    selected: bool

    def __init__(self, pos: (int, int, int)):
        self.pos = pos
        sector_angle = self.pos[0] * math.pi / 3
        pos_angle = sector_angle + 2 * math.pi / 3
        self.center = (
            SCREEN_CENTER[0] + 2 * TILE_RADIUS * (self.pos[1] * math.sin(sector_angle) + self.pos[2] * math.sin(pos_angle)),
            SCREEN_CENTER[1] - 2 * TILE_RADIUS * (self.pos[1] * math.cos(sector_angle) + self.pos[2] * math.cos(pos_angle))
        )
        point_angle = -math.pi / 3
        self.points = []
        for i in range(6):
            first = self.get_pos(point_angle)
            point_angle += (math.pi / 3) % (2 * math.pi)
            second = self.get_pos(point_angle)
            self.points.append((self.center, first, second))
        self.color = CL_SECTOR[self.pos[0] % 2]
        self.hover = False
        self.selected = False

    def get_pos(self, angle: float) -> (float, float):
        """ get tuple pos from radius and arbitrary angle """
        return (math.ceil(self.center[0] + TILE_RADIUS * math.cos(angle)), math.ceil(self.center[1] + TILE_RADIUS * math.sin(angle)))

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        if self.selected:
            color = CL_SECTOR_SELECTED
        elif self.hover:
            color = CL_SECTOR_HOVER
        else:
            color = self.color
        for point in self.points:
            pygame.draw.polygon(screen, color, point)
        #screen.blit(font.render(f"{self.pos}", True, CL_BLACK), self.center)

    def _intersect(self, pos: (float, float)):
        return math.sqrt((pos[0] - self.center[0])**2 + (pos[1] - self.center[1])**2) <= TILE_SIDE

    def mouse_move(self, mouse_pos: (float, float)):
        self.hover = self._intersect(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.selected = self._intersect(mouse_pos)

"""
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
"""

