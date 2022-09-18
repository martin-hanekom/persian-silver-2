import os
import json

CONF_FILE = "conf.json"

class Conf:
    def __init__(self, conf):
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
