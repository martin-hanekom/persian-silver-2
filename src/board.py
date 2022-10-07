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
                            color=Ui.colors['tile'][0],
                            callback=self.select_tile,
                        )
                    ] + [
                        Tile(
                            coordinate=Coordinate(k, j, i),
                            color=Ui.colors['tile'][k % 2],
                            callback=self.select_tile,
                        ) for j in range(1, Ui.board['layers'])
                        for i in range(j) 
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
    
    def init(self):
        Coordinate.init(self.view.get('board').center)
        self.view.get('board').update()

    def select_tile(tile: Tile) -> None:
        pass
