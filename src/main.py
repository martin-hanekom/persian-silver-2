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
            if event.type == pygame.QUIT:
                g.running = False 
            elif event.type == pygame.MOUSEMOTION:
                rooms[g.room].mouse_move(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                rooms[g.room].mouse_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    g.running = False

        clock.tick(cc.video.fps) 
        rooms[g.room].draw(screen)
        pygame.display.update()

    pygame.quit()
