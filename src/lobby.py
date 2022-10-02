import socket
import threading
import pygame
import assets
import utils
import server
from view import View
from sprite import Sprite
from conf import cc, G, Ui

view: View = None
model: dict = {}

def set_model(**kwargs):
    global model, view
    model.update(**kwargs)
    view.update()

def mainmenu():
    global model
    import menu
    menu.init()
    model['running'] = False

def get_view():
    return View(
        model=model,
        children=[
            View(
                children=[
                    View(
                        size=Ui.size['btnSmall'],
                        color=Ui.colors['btnAlt'],
                        text='Back',
                        callback=mainmenu,
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
                                callback=set_model,
                                args=[{'host': True}],
                            ),
                            View(
                                size=Ui.size['btn'],
                                color=Ui.colors['btn'],
                                text='Join',
                                callback=set_model,
                                args=['join'],
                                kwargs={'flip': True},
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
                size=(400, cc.video.size[1] - 100),
                color=Ui.colors['panel'],
                orient='V',
                anchor=(1, 1),
            ),
            View(
                size=(800, cc.video.size[1] - 100),
                color=Ui.colors['panel'],
                anchor=(1, 1),
            )
        ],
    )

def init():
    global model, view
    model = {
        'running': True,
        'host': False,
        'join': False,
    }
    view = get_view()
    thread = threading.Thread(target=G.run, args=[model, view])
    thread.start()
    G.threads.append(thread)
