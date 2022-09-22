from dataclasses import dataclass
import math
import pygame
from game import g
from tools import Position, SpriteState
from piece import Piece
from conf import cc

@dataclass
class Board:
    def __init__(self):
        # sector: i, layer: j, pos: k
        self.tiles = [[[Tile(Position(0, 0, 0))]]] + [[[Tile(Position(sector, layer, index))
            for index in range(layer)]
            for layer in range(1,cc.board.layers  + 1)]
            for sector in range(cc.board.sectors)]

    def draw(self, screen: pygame.Surface):
        for sector in self.tiles:
            for layer in sector:
                for tile in layer:
                    tile.draw(screen)

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
class Tile:
    pos: Position
    points: [((float, float), (float, float), (float, float))]
    color: (int, int, int)
    state: SpriteState

    def __init__(self, pos: Position):
        self.pos = pos
        point_angle = -math.pi / 3
        self.points = []
        for i in range(6):
            first = self.get_point(point_angle)
            point_angle += (math.pi / 3) % (2 * math.pi)
            second = self.get_point(point_angle)
            self.points.append((self.pos.to_map(), first, second))
        self.color = cc.color.sector.base[self.pos.sector % 2]
        self.state = SpriteState()

    def get_point(self, angle: float) -> (float, float):
        """ get tuple pos from radius and arbitrary angle """
        return (math.ceil(self.pos.x + cc.tile.radius * math.cos(angle)), math.ceil(self.pos.y + cc.tile.radius * math.sin(angle)))

    def draw(self, screen: pygame.Surface):
        if self.state.selected:
            color = cc.color.sector.selected[self.pos.sector % 2]
        elif self.state.hover:
            color = cc.color.sector.hover[self.pos.sector % 2]
        else:
            color = self.color
        for point in self.points:
            pygame.draw.polygon(screen, color, point)
    
    def mouse_move(self, mouse_pos: (float, float)):
        self.state.hover = self.pos.circle_intersect(cc.tile.side, mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.state.selected = self.pos.circle_intersect(cc.tile.side, mouse_pos)
        if self.state.selected:
            if g().state.menu:
                g().buy_piece(self.pos)
            else:
               g().board_select(None) 
