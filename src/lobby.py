from room import Room
from view import Model, View
from conf import Ui

class Lobby(Room):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = Model(host=False, join=False)
        self.view = View(
            model=self.model,
            children=[
                View(
                    children=[
                        View(
                            size=Ui.size['btnSmall'],
                            color=Ui.colors['btnAlt'],
                            text='Back',
                            callback=self.back,
                        ),
                        View(
                            text='Would you like to host or join?',
                        ),
                        View(
                            children=[
                                View(
                                    size=Ui.size['btn'],
                                    color=Ui.colors['btn'],
                                    text='Host',
                                    callback=self.set_model,
                                    kwargs={'host': True},
                                ),
                                View(
                                    size=Ui.size['btn'],
                                    color=Ui.colors['btn'],
                                    text='Join',
                                    callback=self.set_model,
                                    kwargs={'join': True},
                                ),
                            ],
                            padding=0,
                        ),
                        View(
                            children=[
                                View(text='Host ip: '),
                                View(text='192.168.0.1'),
                            ],
                            show_if='host',
                        ),
                        View(
                            text='Join ip',
                            show_if='join',
                        ),
                        View(
                            size=Ui.size['btn'],
                            color=Ui.colors['btn'],
                            text='Play',
                        )
                    ],
                    size=(400, Ui.size['screen'][1] - 100),
                    color=Ui.colors['panel'],
                    orient='V',
                    anchor=(View.A_LEFT, View.A_TOP),
                ),
                View(
                    size=(800, Ui.size['screen'][1] - 100),
                    color=Ui.colors['panel'],
                )
            ],
        )
