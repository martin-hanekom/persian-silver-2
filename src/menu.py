import threading
import pygame
import assets
import utils
from view import View
from conf import G, Ui

view: View = None
model: dict = {}

def set_model(**kwargs):
    global model, view
    model.update(**kwargs)
    view.update()

def singleplayer():
    global model
    import client
    client.init()
    model['running'] = False

def multiplayer():
    global model
    import lobby
    lobby.init()
    model['running'] = False

def get_view() -> View:
    return View(
        model=model,
        children=[
            View(
                children=[
                    View(
                        size=Ui.size['btnLarge'],
                        color=Ui.colors['btn'],
                        text='Play',
                        font='systeml',
                        callback=set_model,
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
                        callback=set_model,
                        kwargs={'running', False},
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
                                callback=singleplayer,
                            ),
                            View(
                                size=Ui.size['btnLarge'],
                                color=Ui.colors['btn'],
                                text='Multiplayer',
                                font='systeml',
                                callback=multiplayer,
                            ),
                        ],
                        padding=0,
                    ),
                    View(
                        size=Ui.size['btn'],
                        color=Ui.colors['btnAlt'],
                        text='Cancel',
                        callback=set_model,
                        kwargs={'main_menu': True, 'play_menu': False},
                    ),
                ],
                show_if='play_menu',
                color=Ui.colors['panel'],
                orient='V',
            ),
        ],
    )

def init():
    global model, view
    model = {
        'running': True,
        'main_menu': True,
        'play_menu': False,
    }
    view = get_view()
    thread = threading.Thread(target=G.run, args=[model, view])
    thread.start()
    G.threads.append(thread)
