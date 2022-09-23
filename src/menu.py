import pygame
import main
import assets
from conf import cc

components = {}
texts = {}

colors = {
    "panel": pygame.Color("#284A03"),
    "background": pygame.Color("#305904"),
    "button": pygame.Color("#009A17"),
    "text": pygame.Color("#DCE9CD"),
}

""" component functions """
def enter(state: int):
    main.state = state

class Sprite:
    def __init__(self,
            rect: pygame.Rect = None,
            surf: pygame.Surface = None,
            pos: (float, float) = None,
            color: pygame.Color = None,
            func = None):
        self.rect = rect
        self.surf = surf
        self.pos = pos
        self.color = color
        self.func = func

    def draw(self, screen: pygame.Surface):
        if self.rect is not None:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=2)
        elif self.surf is not None:
            size = self.surf.get_size()
            screen.blit(self.surf, (self.pos[0] - size[0] / 2, self.pos[1] - size[1] / 2))

def init():
    global components, texts
    panel_rect = ((cc.video.size[0] - 300) / 2, (cc.video.size[1] - 500) / 2, 300, 500)
    components = {
        "panel": Sprite(
            rect=pygame.Rect(*panel_rect),
            color=colors["panel"],
            func=lambda: 1
        ),
        "play": Sprite(
            rect=pygame.Rect((cc.video.size[0] - 200) / 2, panel_rect[1] + 50, 200, 80),
            color=colors["button"],
            func=enter(1)
        ),
        "load": Sprite(
            rect=pygame.Rect((cc.video.size[0] - 200) / 2, panel_rect[1] + 150, 200, 80),
            color=colors["button"],
            func=lambda: 1
        ),
    }
    texts = {
        "play": Sprite(
            surf=assets.fonts["systeml"].render("Play", True, colors["text"]),
            pos=(cc.video.size[0] / 2, components["play"].rect.y + components["play"].rect.h / 2)
        ),
        "load_text": Sprite(
            surf=assets.fonts["systeml"].render("Load", True, colors["text"]),
            pos=(cc.video.size[0] / 2, components["load"].rect.y + components["load"].rect.h / 2)
        )
    }

def action(t: str, pos: (float, float)):
    match t:
        case "move":
            pass

def draw(screen: pygame.Surface):
    screen.fill(colors["background"])
    for sprite in components.values():
        sprite.draw(screen)
    for sprite in texts.values():
        sprite.draw(screen)
    pygame.display.update()
