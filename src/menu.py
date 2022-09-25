import pygame
import assets
import utils
from sprite import Sprite
from conf import cc, g

colors = {
    'panel': (pygame.Color('#284A03'), pygame.Color('#284A03')),
    'background': (pygame.Color('#305904'), pygame.Color('#305904')),
    'button': (pygame.Color('#009A17'), pygame.Color('#59A608')),
    'text': (pygame.Color('#DCE9CD'), pygame.Color('#DCE9CD')),
}

panel = Sprite(
    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(-150, -250), center=(True, True)), (300, 500)),
    colors=colors['panel'],
)
play_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 50), center=(True, False)), (200, 80)),
    colors=colors['button'],
    func=g._set,
    args=['room', 1]
)
load_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 150), center=(True, False)), (200, 80)),
    colors=colors['button'],
    func=g._set,
    args=['running', False]
)
quit_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=panel.rect, offset=(-100, 250), center=(True, False)), (200, 80)),
    colors=colors['button'],
    func=g._set,
    args=['running', False]
)

components = {
    'panel': panel,
    'play_button': play_button,
    'load_button': load_button,
    'quit_button': quit_button,
    'play_text': Sprite(
        surf=assets.fonts['systeml'].render('Play', True, colors['text'][0]),
        pos=utils.offset(rect=play_button.rect, center=(True, True)),
    ),
    'load_text': Sprite(
        surf=assets.fonts['systeml'].render('Load', True, colors['text'][0]),
        pos=utils.offset(rect=load_button.rect, center=(True, True)),
    ),
    'quit_text': Sprite(
        surf=assets.fonts['systeml'].render('Quit', True, colors['text'][0]),
        pos=utils.offset(rect=quit_button.rect, center=(True, True)),
    ),
}

def draw(screen: pygame.Surface):
    screen.fill(colors['background'][0])
    for sprite in components.values():
        sprite.draw(screen)
    pygame.display.update()

def mouse_move(pos: (float, float)):
    for name, sprite in components.items():
        sprite.hover = sprite.intersect(pos)

def mouse_click(pos: (float, float)):
    for name, sprite in components.items():
        if sprite.func and sprite.intersect(pos):
            sprite()
