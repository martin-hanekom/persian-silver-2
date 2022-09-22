from dataclasses import dataclass
import threading
import pygame
from tools import Resource
from board import Board
from player import Player
from ui import Ui
from piece import Piece
from conf import cc

@dataclass
class GameState:
    """ Keep track of rounds, turns and selected """
    game_round: int = 0
    team_turn: int = 0
    turn_timer: float = cc.player.turn.max
    board: Piece = None
    menu: Piece = None

class Client:
    team: int
    opponents: list[str]
    screen: pygame.Surface 
    board: Board
    players: list[Player]
    ui: Ui
    state: GameState
    clock: pygame.time.Clock

    def __init__(self, team: int, opponents: list[str]):
        threading.Thread.__init__(self)
        self.team = team
        self.opponents = opponents
        self.screen = pygame.display.set_mode(cc.video.size)
        Resource.init()
        self.board = Board()
        self.players = [Player(i) for i in range(cc.player.amount)]
        self.ui = Ui()
        self.state = GameState()
        self.clock = pygame.time.Clock()

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
        if self.state.team_turn == self.team:
            self.state.turn_timer -= dt / 1000
            if self.state.turn_timer <= 0:
                self.end_turn()
            self.ui.update(dt)

    def draw(self):
        self.screen.fill(cc.color.background.base)
        self.board.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        self.ui.draw(self.screen)
        pygame.display.update()

    def mouse_move(self, mouse_pos: (float, float)):
        self.board.mouse_move(mouse_pos)
        for player in self.players:
            player.mouse_move(mouse_pos)
        self.ui.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.board.mouse_clicked(mouse_pos)
        for player in self.players:
            player.mouse_clicked(mouse_pos)
        self.ui.mouse_clicked(mouse_pos)

    def menu_select(self, piece: Piece):
        self.state.menu = piece

    def board_select(self, piece: Piece):
        self.state.board = piece
