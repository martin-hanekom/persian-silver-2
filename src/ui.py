from dataclasses import dataclass
from sprite import ISprite
import pygame
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

@dataclass
class UiTurn(ISprite):
    def __init__(self, panel: pygame.Rect):
        self.panel = panel
        self.button = pygame.Rect(self.panel.left + self.panel.width - TURN_BUTTON_SIZE[0] - 20, self.panel.top + self.panel.height - TURN_BUTTON_SIZE[1] - 20, *TURN_BUTTON_SIZE)
        self.description = [Resource.fonts.get("system").render(f"Player {i}'s turn", True, CL_UI_TEXT) for i in range(NUM_PLAYERS)]
        self.button_text = Resource.fonts.get("systeml").render("END TURN", True, CL_BACKGROUND)
        self.turn = 0

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, CL_SECTOR[0], self.button, border_radius=3)
        desc_w, desc_h = self.description[self.turn].get_size()
        bt_w, bt_h = self.button_text.get_size()
        screen.blit(self.description[self.turn], (self.button.left + (self.button.width - desc_w) / 2, self.button.top - 30))
        screen.blit(self.button_text, (self.button.left + (self.button.width - bt_w) / 2, self.button.top + (self.button.height - bt_h) / 2))

    def update(self, screen: pygame.Surface, game):
        self.turn = self.game.turn
