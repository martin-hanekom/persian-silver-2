import math
from room import Room
from view import Model, View, Tile
from utils import Coordinate
from conf import Ui, cc

class Board(Room):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = Model(main_menu=True, play_menu=False)
        self.view =  View(
            model=self.model,
            children=[
                View(
                    children=[
                        Tile(
                            coordinate=Coordinate(0, 0, 0),
                            callback=select_tile,
                            color=Ui.colors['tile'][0],
                            args=[(0, 0, 0)],
                        )
                    ] + [
                        Tile(
                            coordinate=Coordinate(i, j, k),
                            color=Ui.colors['tile'][k % 2],
                            callback=select_tile,
                            args=[(i, j, k)],
                        ) for i in range(j) 
                        for j in range(1, Ui.board['layers'])
                        for k in range(Ui.board['sectors'])
                    ],
                    size=Ui.size['board'],
                    text='Board',
                    name='board',
                ),
                View(
                    size=(Ui.size['screen'][0] - Ui.size['board'][0] - 50, Ui.size['screen'][1] - 50),
                    color=Ui.colors['panel'],
                    text='ui',
                ),
            ],
        )
        Coordinate.init(self.view.get('board').center)

"""
class Tile:
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
        self.hover = False

    def get_point(self, angle: float) -> (float, float):
        # get tuple pos from radius and arbitrary angle
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
        self.hover = self.pos.circle_intersect(cc.tile.side, mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.state.selected = self.pos.circle_intersect(cc.tile.side, mouse_pos)
        if self.state.selected:
            if g().state.menu:
                g().buy_piece(self.pos)
            else:
               g().board_select(None) 
"""
