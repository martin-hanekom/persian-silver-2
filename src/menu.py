import pygame
import assets
import utils
from sprite import Sprite
from view import View
from conf import cc, g, Ui

model = {
    'main_menu': True,
    'play_menu': False,
}

def set_model(changes: dict):
    model.update(changes)
    view.update()

def get_view() -> View:
    return View(
        model=model,
        children=[
            View(
                children=[
                    View(
                        size=Ui.size['btnLarge'],
                        color=Ui.colors['btn'],
                        text='Play',
                        font='systeml',
                        callback=set_model,
                        args=[{'main_menu': False, 'play_menu': True}],
                    ), 
                    View(
                        size=Ui.size['btnLarge'],
                        color=Ui.colors['btn'],
                        text='Load',
                        font='systeml',
                    ), 
                    View(
                        size=Ui.size['btnLarge'],
                        color=Ui.colors['btn'],
                        text='Quit',
                        font='systeml',
                        callback=g._set,
                        args=['running', False],
                    ), 
                ],
                show_if='main_menu',
                color=Ui.colors['panel'],
                orient='V',
            ),
            View(
                children=[
                    View(
                        children=[
                            View(
                                size=Ui.size['btnLarge'],
                                color=Ui.colors['btn'],
                                text='Singleplayer',
                                font='systeml',
                                #callback=g._set,
                                #args=['room', 1],
                            ),
                            View(
                                size=Ui.size['btnLarge'],
                                color=Ui.colors['btn'],
                                text='Multiplayer',
                                font='systeml',
                                callback=g._set,
                                args=['room', 1],
                            ),
                        ],
                        padding=0,
                    ),
                    View(
                        size=Ui.size['btn'],
                        color=Ui.colors['btnAlt'],
                        text='Cancel',
                        callback=set_model,
                        args=[{'main_menu': True, 'play_menu': False}],
                    ),
                ],
                show_if='play_menu',
                color=Ui.colors['panel'],
                orient='V',
            ),
        ],
    )

def run(screen: pygame.Surface):
    clock = pygame.time.Clock()
    view = get_view()
    view.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                view.mouse_move(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                view.mouse_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        clock.tick(cc.video.fps) 
        screen.fill(Ui.colors['background'][0])
        view.draw(screen)
        pygame.display.update()
