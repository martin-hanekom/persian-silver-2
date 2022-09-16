import math
from dataclasses import dataclass
import pygame
from sprite import ISprite
from tools import Position
from constants import *

@dataclass
class Board(ISprite):
    def __init__(self):
        # sector: i, layer: j, pos: k
        self.tiles = [[[Tile(Position(0, 0, 0))]]] + [[[Tile(Position(sector, layer, index))
            for index in range(layer)]
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
    pos: Position
    points: [((float, float), (float, float), (float, float))]
    color: (int, int, int)
    hover: bool
    selected: bool

    def __init__(self, pos: Position):
        self.pos = pos
        point_angle = -math.pi / 3
        self.points = []
        for i in range(6):
            first = self.get_point(point_angle)
            point_angle += (math.pi / 3) % (2 * math.pi)
            second = self.get_point(point_angle)
            self.points.append((self.pos.to_map(), first, second))
        self.color = CL_SECTOR[self.pos.sector % 2]
        self.hover = False
        self.selected = False

    def get_point(self, angle: float) -> (float, float):
        """ get tuple pos from radius and arbitrary angle """
        return (math.ceil(self.pos.x + TILE_RADIUS * math.cos(angle)), math.ceil(self.pos.y + TILE_RADIUS * math.sin(angle)))

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

    def mouse_move(self, mouse_pos: (float, float)):
        self.hover = self.pos.circle_intersect(TILE_SIDE, mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.selected = self.pos.circle_intersect(TILE_SIDE, mouse_pos)
