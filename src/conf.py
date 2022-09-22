import os
import json
import math

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
