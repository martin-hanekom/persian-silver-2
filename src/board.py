import math
from game import Game
from room import Room
from view import Model, View, Tile
from utils import Coordinate
from conf import Ui, cc

class Board(Room):
    def __init__(self, *args, player=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        Game.events.next_turn += self.next_turn
        if not player:
            raise Exception("Player must be attached to board")
        self.player = player
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
                    children=[
                        View(
                            text=f"Player {Game.turn + 1}'s turn",
                            name='player_turn',
                        ),
                        View(
                            size=Ui.size['btnLarge'],
                            color=Ui.colors['btn'],
                            text='End turn',
                            font='systeml',
                            callback=self.player.end_turn,
                        ),
                    ],
                    size=(Ui.size['screen'][0] - Ui.size['board'][0] - 50, Ui.size['screen'][1] - 50),
                    color=Ui.colors['panel'],
                    text='ui',
                    anchor=(View.A_CENTER, View.A_BOTTOM),
                    orient='V',
                ),
            ],
        )
    
    def init(self):
        Coordinate.init(self.view.get('board').center)
        self.view.get('board').update()

    def next_turn(self) -> None:
        print(f"Displaying player {Game.turn + 1}")
        self.view.get('player_turn').set_text(f"Player {Game.turn + 1}'s turn")

    def select_tile(tile: Tile) -> None:
        pass

    def back(self) -> None:
        Game.end_game.set()
        super().back()
