import socket
import pygame
import assets
import utils
import server
from sprite import Sprite
from conf import cc, g, Ui

padding = 50
i_padding = 25
local_ip = socket.gethostbyname(socket.getfqdn())
components = []


option_panel = Sprite(
    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(padding, padding)), (400, cc.video.size[1] - 100)),
    colors=Ui.colors['panel'],
)

list_panel = Sprite(
    rect=pygame.Rect(utils.offset(size=cc.video.size, offset=(2*padding + option_panel.rect.w, padding)), (cc.video.size[0] - option_panel.rect.w - 3*padding, cc.video.size[1] - 100)),
    colors=Ui.colors['panel'],
)

back_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=option_panel.rect, offset=(i_padding, i_padding)), Ui.size['btnSmall']),
    colors=Ui.colors['background'],
    text=assets.fonts['system'].render('Back', True, Ui.colors['text'][0]),
    func=g._set,
    args=['room', 0]
)

host_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=option_panel.rect, offset=(i_padding, 100 + i_padding)), Ui.size['btn']),
    colors=Ui.colors['button'],
    text=assets.fonts['systeml'].render('Host', True, Ui.colors['text'][0]),
    func=server.host,
)

join_button = Sprite(
    rect=pygame.Rect(utils.offset(rect=option_panel.rect, offset=(host_button.rect.w + 2*i_padding, 100 + i_padding)), Ui.size['btn']),
    colors=Ui.colors['button'],
    text=assets.fonts['systeml'].render('Join', True, Ui.colors['text'][0]),
    func=server.join,
    args=(local_ip, 'test'),
)

option_texts = [
    Sprite(
        surf=assets.fonts['system'].render(f'Your IP: {local_ip}.', True, Ui.colors['text'][0]),
        pos=utils.offset(rect=host_button.rect, offset=(0, -2*i_padding)),
    ),
    Sprite(
        surf=assets.fonts['system'].render('Do you want to host or join game?', True, Ui.colors['text'][0]),
        pos=utils.offset(rect=host_button.rect, offset=(0, -i_padding)),
    ),
]

components = [
    option_panel,
    list_panel,
    back_button,
    *option_texts,
    host_button,
    join_button,
]

def draw(screen: pygame.Surface):
    screen.fill(Ui.colors['background'][0])
    for sprite in components:
        sprite.draw(screen)

def mouse_move(pos: (float, float)):
    for sprite in components:
        sprite.hover = sprite.intersect(pos)

def mouse_click(pos: (float, float)):
    for sprite in components:
        if sprite.func and sprite.intersect(pos):
            sprite()
