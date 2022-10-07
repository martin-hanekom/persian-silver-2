from room import Room
from view import Model, View
from conf import Ui

class Client(Room):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Model(main_menu=True, play_menu=False)
        self.view =  View(
            model=self.model,
            children=[
                View(
                    size=Ui.size['board'],
                    text='Board',
                ),
                View(
                    size=(Ui.size['screen'][0] - Ui.size['board'][0] - 50, Ui.size['screen'][1] - 50),
                    color=Ui.colors['panel'],
                    text='ui',
                ),
            ],
        )
