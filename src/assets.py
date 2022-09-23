import os
import pygame
from conf import cc

textures = {}
fonts = {}

def load_images(item: str):
    return [pygame.image.load(os.path.join("lib", "images", f"{item}{i}.png")) for i in range(cc.player.amount)]

def load():
    global textures, fonts
    textures = { key: load_images(key) for key in cc.pieces.__dict__ }
    for key, items in textures.items():
        for index, item in enumerate(items):
            items[index] = pygame.transform.scale(item, cc.piece.size).convert_alpha()

    fonts = {
        "systems": pygame.font.SysFont("Calibri", 12),
        "system": pygame.font.SysFont("Calibri", 18),
        "systeml": pygame.font.SysFont("Calibri", 24),
    }

