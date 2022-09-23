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

def init():
    global components, texts
    panel_rect = ((cc.video.size[0] - 300) / 2, (cc.video.size[1] - 500) / 2, 300, 500)
    components = {
        "panel": (pygame.Rect(*panel_rect), colors["panel"], lambda: 1),
        "play": (pygame.Rect((cc.video.size[0] - 200) / 2, panel_rect[1] + 50, 200, 80), colors["button"], enter(1)),
        "load": (pygame.Rect((cc.video.size[0] - 200) / 2, panel_rect[1] + 150, 200, 80), colors["button"], lambda: 1),
    }
    texts = {
        "play_text": (assets.fonts["systeml"].render("Play", True, colors["text"]), (cc.video.size[0] / 2, components["play"][0].y + components["play"][0].h / 2)),
        "load_text": (assets.fonts["systeml"].render("Load", True, colors["text"]), (cc.video.size[0] / 2, components["load"][0].y + components["load"][0].h / 2))
    }

def draw(screen: pygame.Surface):
    screen.fill(colors["background"])
    for rect, color, func in components.values():
        pygame.draw.rect(screen, color, rect, border_radius=2)
    for font, pos in texts.values():
        size = font.get_size()
        screen.blit(font, (pos[0] - size[0] / 2, pos[1] - size[1] / 2))
    pygame.display.update()
