import os
import json
import math
import threading
import pygame

class Ui:
    colors = {
        'panel': (pygame.Color('#284A03'), pygame.Color('#284A03')),
        'background': (pygame.Color('#305904'), pygame.Color('#305904')),
        'btn': (pygame.Color('#009A17'), pygame.Color('#59A608')),
        'btnAlt': (pygame.Color('#305904'), pygame.Color('#44691D')),
        'text': (pygame.Color('#DCE9CD'), pygame.Color('#DCE9CD')),
        'tile': [(pygame.Color('#'), pygame.Color('#')), (pygame.Color('#'), pygame.Color('#'))],
    }
    size = {
        'screen': (1300, 900),
        'btnSmall': (80, 40),
        'btn': (120, 50),
        'btnLarge': (180, 70),
        'board': (900, 900),
    }
    fps = 30
    padding = 7
    spacing = 7
    board = {
        'layers': 5,
        'sectors': 6,
    }


class G:
    threads: list[threading.Thread] = []
    screen: pygame.Surface = None

    @staticmethod
    def run(model, view):
        clock = pygame.time.Clock()
        view.update()

        while model['running']:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEMOTION:
                    view.mouse_move(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    view.mouse_down(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    view.mouse_up(pygame.mouse.get_pos())
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            clock.tick(Ui.fps)
            G.screen.fill(Ui.colors['background'][0])
            view.draw(G.screen)
            pygame.display.update()

CONF_FILE = "conf.json"

class Conf:
    def __init__(self, conf: dict = None):
        if conf is not None:
            for key, item in conf.items():
                if isinstance(item, dict):
                    item = Conf(item)
                setattr(self, key, item)

    def __repr__(self):
        return f"{self.__dict__}"

    def __iter__(self):
        for key in self.__dict__:
            yield key

    def _set(self, key, value):
        setattr(self, key, value)

cc = None
with open(os.path.join(os.path.dirname(__file__), CONF_FILE), "r") as f:
    contents = json.load(f)
    cc = Conf(contents)
    # additional calculated constants
    cc.video.center = (cc.video.size[0] / 2, cc.video.size[1] / 2)
    cc.tile.side = cc.tile.radius * math.cos(math.pi / 6)
    cc.board.radius = 2 * (cc.tile.padding + cc.tile.side) * cc.board.layers + cc.tile.side
    cc.board.center = (cc.board.radius + cc.board.padding, cc.video.size[1] / 2)
    cc.piece = Conf()
    cc.piece.size = (1.4 * cc.tile.radius, 1.4 * cc.tile.radius)
    cc.piece.offset = (-cc.piece.size[0] / 2, -cc.piece.size[1] / 2)
    print(cc)
