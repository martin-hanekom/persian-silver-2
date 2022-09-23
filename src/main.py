import pygame
import assets
import menu
#import game
from conf import cc

state = 0
rooms = [menu]#, game]

def init():
    for room in rooms:
        room.init()

def run():
    screen = pygame.display.set_mode(cc.video.size)
    assets.load()
    clock = pygame.time.Clock()
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        clock.tick(30) 
        rooms[state].draw(screen)

if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()
