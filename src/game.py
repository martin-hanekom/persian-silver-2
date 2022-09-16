from dataclasses import dataclass
import pygame
from board import Board
from constants import FPS, SCREEN_SIZE

@dataclass
class Game:
    __instance = None
    clock: pygame.time.Clock
    screen: pygame.Surface
    board: Board

    def __init__(self):
        if Game.__instance:
            raise Exception("Game already instantiated.")
        pygame.init()
        self.font = pygame.font.SysFont("Calibri", 16)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.board = Board()
        Game.__instance = self

    def __del__(self):
        pygame.quit()

    @staticmethod
    def _get():
        """ Static Access Method """
        if not Game.__instance:
            Game()
        return Game.__instance

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    self.board.mouse_move(mouse_pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    self.board.mouse_clicked(mouse_pos)

            self.draw()
            self.update(self.clock.tick(FPS))

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw(self.screen, self.font)
        pygame.display.update()

    def update(self, dt: float):
        pass
