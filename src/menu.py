import pygame
import assets
import utils
from sprite import Sprite
from view import View
from conf import cc, g, Ui

view = View(
    rect=(300, 500),
    color=Ui.colors['panel'],
    children = [
        View(
            rect=Ui.size['btnLarge'],
            color=Ui.colors['btn'],
            text='Play',
            font='systeml',
            callback=g._set,
            args=['room', 1],
        ), 
        View(
            rect=Ui.size['btnLarge'],
            color=Ui.colors['btn'],
            text='Load',
            font='systeml',
        ), 
        View(
            rect=Ui.size['btnLarge'],
            color=Ui.colors['btn'],
            text='Quit',
            font='systeml',
            callback=g._set,
            args=['running', False],
        ), 
    ]
)
    
#panel = Sprite(
#    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(-150, -250), center=(True, True)), (300, 500)),
#    colors=Ui.colors['panel'],
#)
#play_button = Sprite(
#    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 50), center=(True, False)), Ui.size['btnLarge']),
#    colors=Ui.colors['button'],
#    text=assets.fonts['systeml'].render('Play', True, Ui.colors['text'][0]),
#    func=g._set,
#    args=['room', 1]
#)
#load_button = Sprite(
#    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 150), center=(True, False)), Ui.size['btnLarge']),
#    colors=Ui.colors['button'],
#    text=assets.fonts['systeml'].render('Load', True, Ui.colors['text'][0]),
#    func=g._set,
#    args=['running', False]
#)
#quit_button = Sprite(
#    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 250), center=(True, False)), Ui.size['btnLarge']),
#    colors=Ui.colors['button'],
#    text=assets.fonts['systeml'].render('Quit', True, Ui.colors['text'][0]),
#    func=g._set,
#    args=['running', False]
#)
#
#components = {
#    'panel': panel,
#    'play_button': play_button,
#    'load_button': load_button,
#    'quit_button': quit_button,
#}

def draw(screen: pygame.Surface):
    screen.fill(Ui.colors['background'][0])
    for sprite in components:
        sprite.draw(screen)

def mouse_move(pos: (float, float)):
    for sprite in components:
        sprite.hover = sprite.intersect(pos)

def mouse_click(pos: (float, float)):
    for sprite in components:
        if sprite.callback and sprite.intersect(pos):
            sprite()
