import pygame
import assets
import utils
from sprite import Sprite
from view import View
from conf import cc, g, Ui

model = {
    'main_menu': True,
    'play_menu': False,
}

def set_model(changes: dict):
    model.update(changes)
    view.update()

view = View(
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
                    args=[{'main_menu': False, 'play_menu': True}],
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
                    callback=g._set,
                    args=['running', False],
                ), 
            ],
            show_if='main_menu',
            color=Ui.colors['panel'],
            orient='V',
        ),
        View(
            children=[
                View(
                    size=Ui.size['btnLarge'],
                    color=Ui.colors['btn'],
                    text='Singleplayer',
                    font='systeml',
                    callback=g._set,
                    args=['room', 2],
                ),
                View(
                    size=Ui.size['btnLarge'],
                    color=Ui.colors['btn'],
                    text='Multiplayer',
                    font='systeml',
                    callback=g._set,
                    args=['room', 1],
                ),
            ],
            show_if='play_menu',
            color=Ui.colors['panel'],
        ),
    ],
    size=cc.video.size,
)
view.update()

def draw(screen: pygame.Surface):
    screen.fill(Ui.colors['background'][0])
    view.draw(screen)

def mouse_move(pos: (float, float)):
    view.mouse_move(pos)

def mouse_click(pos: (float, float)):
    view.mouse_click(pos)
