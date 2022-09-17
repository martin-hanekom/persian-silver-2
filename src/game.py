from dataclasses import dataclass
import pygame
from piece import IPiece
from player import Player
from board import Board
from ui import Ui
from tools import Resource
from constants import *

@dataclass
class Game:
    __instance = None
    clock: pygame.time.Clock
    screen: pygame.Surface
    board: Board
    turn: int

    def __init__(self):
        if Game.__instance:
            raise Exception("Game already instantiated.")
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        Resource.init()
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.players = [Player(i) for i in range(NUM_PLAYERS)]
        self.turn = 0
        self.ui = Ui._get()
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
                    self.mouse_move(mouse_pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    self.mouse_clicked(mouse_pos)

            self.draw()
            self.update(self.clock.tick(FPS))

    def draw(self):
        self.screen.fill(CL_BACKGROUND)
        self.board.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        self.ui.draw(self.screen)
        pygame.display.update()

    def mouse_move(self, mouse_pos):
        for player in self.players:
            player.mouse_move(mouse_pos)
        self.board.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos):
        for player in self.players:
            player.mouse_clicked(mouse_pos)
        self.board.mouse_clicked(mouse_pos)

    def update(self, dt: float):
        pass
      
