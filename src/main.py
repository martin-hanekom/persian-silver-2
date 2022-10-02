import threading
import pygame
from conf import G, Ui

if __name__ == '__main__':
    pygame.init()
    G.screen = pygame.display.set_mode(Ui.size['screen'])

    import assets
    import menu
    menu.init()

    for thread in G.threads:
        thread.join()

    pygame.quit()
