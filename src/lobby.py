import pygame
import assets
import utils
from sprite import Sprite
from conf import cc, colors, g, size

padding = 50
i_padding = 25

option_panel = Sprite(
    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(padding, padding)), (400, cc.video.size[1] - 100)),
    colors=colors['panel'],
)

list_panel = Sprite(
    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(2*padding + option_panel.rect.w, padding)), (cc.video.size[0] - option_panel.rect.w - 3*padding, cc.video.size[1] - 100)),
    colors=colors['panel'],
)

back_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=option_panel.rect, offset=(i_padding, i_padding)), size['button_sm']),
    colors=colors['background'],
    func=g._set,
    args=['room', 0]
)

back_button_text = Sprite(
    surf=assets.fonts['system'].render('Back', True, colors['text'][0]),
    pos=utils.offset(rect=back_button.rect, center=(True, True)),
)

option_text = Sprite(
    surf=assets.fonts['system'].render('Do you want to host or join game?', True, colors['text'][0]),
    pos=utils.offset(rect=option_panel.rect, offset=(0, back_button.rect.h + 2*i_padding), center=(True, False)),
)

host_button = Sprite(
    rect=pygame.Rect(utils.offset(
        rect=option_panel.rect,
        offset=(i_padding, option_text.pos[1] + i_padding),
    ), size['button_sm']),
    colors=colors['button'],
)

host_button_text = Sprite(
    surf=assets.fonts['system'].render('Host', True, colors['text'][0]),
    pos=utils.offset(rect=host_button.rect, center=(True, True)),
)

join_button = Sprite(
    rect=pygame.Rect(utils.offset(
        rect=option_panel.rect,
        offset=(host_button.rect.w + 2*i_padding, option_text.pos[1] + i_padding),
    ), size['button_sm']),
    colors=colors['button'],
)

join_button_text = Sprite(
    surf=assets.fonts['system'].render('Join', True, colors['text'][0]),
    pos=utils.offset(rect=join_button.rect, center=(True, True)),
)

components = {
    'option_panel': option_panel,
    'list_panel': list_panel,
    'back_button': back_button,
    'back_button_text': back_button_text,
    'option_text': option_text,
    'host_button': host_button,
    'host_button_text': host_button_text,
    'join_button': join_button,
    'join_button_text': join_button_text,
}

def draw(screen: pygame.Surface):
    screen.fill(colors['background'][0])
    for sprite in components.values():
        sprite.draw(screen)

def mouse_move(pos: (float, float)):
    for name, sprite in components.items():
        sprite.hover = sprite.intersect(pos)

def mouse_click(pos: (float, float)):
    for name, sprite in components.items():
        if sprite.func and sprite.intersect(pos):
            sprite()
