from dataclasses import dataclass
from sprite import ISprite
import pygame
from constants import *

@dataclass
class Ui(ISprite):
    __instance = None

    def __init__(self):
        if Ui.__instance:
            raise Exception("Ui already instantiated.")
        self.panel = pygame.Rect(SCREEN_SIZE[0] - UI_SIZE - UI_PADDING, UI_PADDING, UI_SIZE, SCREEN_SIZE[1] - 2 * UI_PADDING)
        Ui.__instance = self

    @staticmethod
    def _get():
        """ Static Access Method """
        if not Ui.__instance:
            Ui()
        return Ui.__instance

    def draw(self, screen: pygame.Surface, font: pygame.font.Font):
        pygame.draw.rect(screen, CL_UI, self.panel)
