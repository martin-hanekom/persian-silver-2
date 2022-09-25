import os
import json
import math
import pygame

class Ui:
    colors = {
        'panel': (pygame.Color('#284A03'), pygame.Color('#284A03')),
        'background': (pygame.Color('#305904'), pygame.Color('#44691D')),
        'button': (pygame.Color('#009A17'), pygame.Color('#59A608')),
        'text': (pygame.Color('#DCE9CD'), pygame.Color('#DCE9CD')),
    }
    size = {
        'btnSmall': (100, 40),
        'btn': (150, 60),
        'btnLarge': (200, 80),
    }

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

g = Conf({
    'team': 0,
    'room': 0,
    'running': True,
    'paused': False,
    'error': '',
})
