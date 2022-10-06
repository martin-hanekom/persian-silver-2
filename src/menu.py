from game import Game
from room import Room
from view import Model, View
from conf import Ui

class Menu(Room):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Model(main_menu=True, play_menu=False)
        self.view =  View(
            model=self.model,
            children=[
                View(
                    children=[
                        View(
                            size=Ui.size['btnLarge'],
                            color=Ui.colors['btn'],
                            text='Play',
                            font='systeml',
                            callback=self.set_model,
                            kwargs={'main_menu': False, 'play_menu': True},
                        ), 
                        View(
                            size=Ui.size['btnLarge'],
                            color=Ui.colors['btn'],
                            text='Load',
                            font='systeml',
                        ), 
                        View(
                            size=Ui.size['btnLarge'],
                            color=Ui.colors['btn'],
                            text='Quit',
                            font='systeml',
                            callback=self.set_model,
                            kwargs={'running': False},
                        ), 
                    ],
                    show_if='main_menu',
                    color=Ui.colors['panel'],
                    orient='V',
                ),
                View(
                    children=[
                        View(
                            children=[
                                View(
                                    size=Ui.size['btnLarge'],
                                    color=Ui.colors['btn'],
                                    text='Singleplayer',
                                    font='systeml',
                                    callback=self.singleplayer,
                                ),
                                View(
                                    size=Ui.size['btnLarge'],
                                    color=Ui.colors['btn'],
                                    text='Multiplayer',
                                    font='systeml',
                                    callback=self.multiplayer,
                                ),
                            ],
                            padding=0,
                        ),
                        View(
                            size=Ui.size['btn'],
                            color=Ui.colors['btnAlt'],
                            text='Cancel',
                            callback=self.set_model,
                            kwargs={'main_menu': True, 'play_menu': False},
                        ),
                    ],
                    show_if='play_menu',
                    color=Ui.colors['panel'],
                    orient='V',
                ),
            ],
        )


    def singleplayer(self):
        Room.spawn('Client', self)
        self.model.running = False

    def multiplayer(self):
        Room.spawn('Lobby', self)
        self.model.running = False
