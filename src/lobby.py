import socket
import pygame
import assets
import utils
import server
from view import View
from sprite import Sprite
from conf import cc, g, Ui

model = {
    'host': False,
    'join': False,
}

def set_model(key, value = None, flip = False):
    if flip:
        model[key] = not model[key]
    else:
        model[key] = value
    view.update()

view = View(
    model=model,
    children=[
        View(
            children=[
                View(
                    size=Ui.size['btnSmall'],
                    color=Ui.colors['btnAlt'],
                    text='Back',
                    callback=g._set,
                    args=['room', 0],
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
                            args=['host'],
                            kwargs={'flip': True},
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
        ),
        View(
            size=(800, cc.video.size[1] - 100),
            color=Ui.colors['panel'],
        )
    ],
)
view.update()

def draw(screen: pygame.Surface):
    screen.fill(Ui.colors['background'][0])
    view.draw(screen)

def mouse_move(pos: (float, float)):
    view.mouse_move(pos)

def mouse_click(pos: (float, float)):
    view.mouse_click(pos)
