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
            match event.type:
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return
                case pygame.MOUSEMOTION:
                    rooms[state].action("move", pygame.mouse.get_pos()) 
                case pygame.MOUSEBUTTONUP:
                    rooms[state].action("click", pygame.mouse.get_pos())
        clock.tick(cc.video.fps) 
        rooms[state].draw(screen)

if __name__ == "__main__":
    pygame.init()
    run()
    pygame.quit()
