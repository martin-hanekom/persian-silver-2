import pygame
import assets
import utils
from sprite import Sprite
from view import View
from conf import cc, g, Ui

view = View(
    children=[
        View(
            size=Ui.size['btnLarge'],
            color=Ui.colors['btn'],
            text='Play',
            font='systeml',
            callback=g._set,
            args=['room', 1],
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
    color=Ui.colors['panel'],
    orient='V',
)
view.update()
    
def draw(screen: pygame.Surface):
    screen.fill(Ui.colors['background'][0])
    view.draw(screen)

def mouse_move(pos: (float, float)):
    view.mouse_move(pos)

def mouse_click(pos: (float, float)):
    view.mouse_click(pos)
