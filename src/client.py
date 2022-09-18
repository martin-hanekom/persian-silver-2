from dataclasses import dataclass
import pygame
from board import Board
from player import Player
from ui import Ui
from piece import Piece
from conf import cc

@dataclass
class Client:
    opponents: list[str]
    team: int
    screen: pygame.Surface = pygame.display.set_mode(cc.video.screen_size)
    board: Board = Board()
    players: list[Player] = [Player(i) for i in range(cc.player.amount)]
    ui: Ui = Ui()
    state: GameState = GameState()
    clock: pygame.time.Clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                running = False
                    case pygame.MOUSEMOTION:
                        self.mouse_move(pygame.mouse.get_pos())
                    case pygame.MOUSEBUTTONUP:
                        self.mouse_clicked(pygame.mouse.get_pos())
            self.update(self.clock.tick(cc.video.fps))
            self.draw()

    def update(self, dt: float):
        pass
    
    def draw(self):
        pass

@dataclass
class GameState:
    """ Keep track of rounds, turns and selected """
    game_round: int = 0
    team_turn: int = 0
    turn_timer: float = TURN_MAX_TIME 
    board: Piece = None
    menu: Piece = None
