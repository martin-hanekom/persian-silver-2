import threading
import pygame
from conf import cc, g

threads = []

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(cc.video.size)

    import assets
    import menu
    import lobby

    thread = threading.Thread(target=menu.run, args=(screen,))
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()

    pygame.quit()
