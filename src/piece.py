from dataclasses import dataclass
import pygame
from game import g
from tools import Position, Resource, SpriteState
from conf import cc

@dataclass
class Piece:
    label: str
    team: int
    pos: Position
    sprite: pygame.Surface
    state: SpriteState

    def __init__(self, label: str, team: int, pos: Position):
        self.label = label
        self.team = team
        self.pos = pos
        self.sprite = Resource.textures.get(self.label)[self.team]
        self.state = SpriteState()

    def draw(self, screen: pygame.Surface, pos: (float, float) = None):
        if self.state.hover:
            self.sprite.set_alpha(200)
        else:
            self.sprite.set_alpha(255)
        pos = self.pos.to_map(cc.piece.offset) if pos is None else pos
        screen.blit(self.sprite, pos)

    def mouse_move(self, mouse_pos: (float, float)):
        self.state.hover = self.pos.circle_intersect(cc.tile.side, mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.state.selected = self.pos.circle_intersect(cc.tile.side, mouse_pos)
        if self.state.selected:
           g().board_select(self) 
