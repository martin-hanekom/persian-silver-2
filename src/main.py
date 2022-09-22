import pygame
import game
from conf import cc

def main():
    pygame.init()
    game.init(0)
    game.g().run()
    pygame.quit()

if __name__ == "__main__":
    main()
