import threading
import pygame
import assets
import utils
from view import View
from room import Room
from conf import G, Ui

view: View = None
model: dict = {
    'running': True,
}

class Client(Room):
    def __init__(self):
        self.model = {
            'running': True,
        }
        self.view = View(
            model=model,
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

def init():
    global model, view
    model = {
        'running': True,
    }
    view = get_view()
    thread = threading.Thread(target=G.run, args=[model, view])
    thread.start()
    G.threads.append(thread)