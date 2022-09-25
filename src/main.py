import pygame
from conf import cc, g

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(cc.video.size)
    clock = pygame.time.Clock()

    import assets
    import menu
    import lobby
    rooms = [menu, lobby]

    while g.running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    g.running = False 
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            g.running = False
                case pygame.MOUSEMOTION:
                    rooms[g.room].mouse_move(pygame.mouse.get_pos())
                case pygame.MOUSEBUTTONUP:
                    rooms[g.room].mouse_click(pygame.mouse.get_pos())

        clock.tick(cc.video.fps) 
        rooms[g.room].draw(screen)
        pygame.display.update()

    pygame.quit()
