from dataclasses import dataclass
import math
import pygame
import game
from sprite import ISprite
from tools import Resource
from constants import *

@dataclass
class Ui(ISprite):
    __instance = None

    def __init__(self):
        if Ui.__instance:
            raise Exception("Ui already instantiated.")
        self.panel = pygame.Rect(SCREEN_SIZE[0] - UI_SIZE - UI_PADDING, UI_PADDING, UI_SIZE, SCREEN_SIZE[1] - 2 * UI_PADDING)
        self.turn = UiTurn(self.panel)
        Ui.__instance = self

    @staticmethod
    def _get():
        """ Static Access Method """
        if not Ui.__instance:
            Ui()
        return Ui.__instance

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, CL_UI, self.panel, border_radius=3)
        self.turn.draw(screen)

    def update(self, dt: float):
        self.turn.update(dt)

    def mouse_move(self, mouse_pos: (float, float)):
        self.turn.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.turn.mouse_clicked(mouse_pos)

@dataclass
class UiTurn(ISprite):
    panel: pygame.Rect
    button: pygame.Rect
    button_text: pygame.Surface
    description: list[pygame.Surface]
    timer: int
    warn_timer: float
    hover: bool
    flash: int

    def __init__(self, panel: pygame.Rect):
        self.panel = panel
        self.button = pygame.Rect(self.panel.left + self.panel.width - TURN_BUTTON_SIZE[0] - 20, self.panel.top + self.panel.height - TURN_BUTTON_SIZE[1] - 20, *TURN_BUTTON_SIZE)
        self.button_text = Resource.fonts.get("systeml").render("END TURN", True, CL_BACKGROUND)
        self.description = [Resource.fonts.get("system").render(f"Player {i}'s turn", True, CL_UI_TEXT) for i in range(NUM_PLAYERS)]
        self.timer = 0
        self.warn_timer = 0.5
        self.timer_text = Resource.fonts.get("system").render(f"0:{self.timer}", True, CL_BACKGROUND)
        self.hover = False
        self.flash = 0

    def draw(self, screen: pygame.Surface):
        color = self.hover if not self.flash else self.flash - 1
        pygame.draw.rect(screen, CL_SECTOR[color], self.button, border_radius=3)
        desc_w, desc_h = self.description[game.game.turn].get_size()
        bt_w, bt_h = self.button_text.get_size()
        screen.blit(self.description[game.game.turn], (self.button.left + (self.button.width - desc_w) / 2, self.button.top - 30))
        screen.blit(self.button_text, (self.button.left + (self.button.width - bt_w) / 2, self.button.top + (self.button.height - bt_h) / 2))
        screen.blit(self.timer_text, (self.button.left, self.button.top))

    def update(self, dt: float):
        if game.game.timer < self.timer or game.game.timer > self.timer + 1:
            self.timer = math.floor(game.game.timer)
            self.timer_text = Resource.fonts.get("system").render(f"0:{self.timer}", True, CL_BACKGROUND)
        if self.timer <= TURN_BUTTON_WARNING:
            self.warn_timer -= dt / 1000
            if not self.flash:
                self.flash = 1
            if self.warn_timer < 0:
                self.warn_timer = 0.5
                self.flash = (self.flash * 2) % 3
        else:
            self.flash = 0

    def mouse_move(self, mouse_pos: (float, float)):
        self.hover = self.button.collidepoint(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        if self.button.collidepoint(mouse_pos):
            game.game.end_turn()
