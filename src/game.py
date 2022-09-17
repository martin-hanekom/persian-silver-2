from dataclasses import dataclass
import pygame
from player import Player
from piece import Piece
from board import Board, Tile
from ui import Ui
from tools import Resource
from constants import *

@dataclass
class Game:
    __instance = None
    clock: pygame.time.Clock
    screen: pygame.Surface
    turn: int
    timer: float
    menu_piece: Piece
    selected_piece: Piece

    def __init__(self):
        if Game.__instance:
            raise Exception("Game already instantiated.")
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        Resource.init()
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.players = [Player(i) for i in range(NUM_PLAYERS)]
        self.turn = 0
        self.timer = TURN_MAX_TIME
        self.ui = Ui._get()
        self.menu_piece = None
        self.selected_piece = None
        Game.__instance = self

    def __del__(self):
        pygame.quit()

    @staticmethod
    def _get():
        """ Static Access Method """
        if not Game.__instance:
            Game()
        return Game.__instance

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    self.mouse_move(mouse_pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    self.mouse_clicked(mouse_pos)

            self.update(self.clock.tick(FPS))
            self.draw()

    def draw(self):
        self.screen.fill(CL_BACKGROUND)
        self.board.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)
        self.ui.draw(self.screen)
        pygame.display.update()

    def mouse_move(self, mouse_pos):
        self.board.mouse_move(mouse_pos)
        for player in self.players:
            player.mouse_move(mouse_pos)
        self.ui.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos):
        self.board.mouse_clicked(mouse_pos, self.menu_piece)
        for player in self.players:
            player.mouse_clicked(mouse_pos)
        self.ui.mouse_clicked(mouse_pos)

    def update(self, dt: float):
        self.timer -= dt / 1000
        if self.timer < 0:
            self.end_turn()
        self.ui.update(dt)

    def select(self, piece: Piece):
        if not piece:
            self.ui.menu.set_pieces([])
            return
        if self.turn == piece.team:
            pieces = [Piece(piece.team, label) for label in PIECES.get(piece.label)[3]]
            self.ui.menu.set_pieces(pieces)

    def menu_select(self, piece: Piece):
        if not piece or self.turn == piece.team:
            self.menu_piece = piece

    def buy_piece(self, tile: Tile):
        if self.turn == self.menu_piece.team:
            self.players[self.menu_piece.team].pieces.append(Piece(self.menu_piece.team, self.menu_piece.label, tile.pos))
            self.menu_piece = None

    def end_turn(self):
        self.turn = (self.turn + 1) % 3
        self.timer = TURN_MAX_TIME
      
game = Game._get()
