from dataclasses import dataclass
import pygame
import board
from constants import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.board = board.Board()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(WHITE)
            self.board.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()

def main():
    game = Game()
    game.run()

main()
