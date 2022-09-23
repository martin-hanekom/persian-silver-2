from dataclasses import dataclass
import pygame
import board
import player
import ui
import piece
import const

@dataclass
class Client:
    opponents: list[str]
    team: int
    board: board.Board = board.Board()
    players: list[player.Player] = [Player(i) for i in range(const.NUM_PLAYERS)]
    ui: ui.Ui = ui.Ui()
    state: GameState = GameState()

    def __init__(self, opponents, team: int):
        self.opponents = opponents
        self.team = team
        self.board = Board() if team == 0 else None
        self.players = [Player(i) for i in range(NUM_PLAYERS)]
        self.ui = Ui()
        self.state = GameState()

    def run(self):
        running = True
        while running:
            for event in pygame

@dataclass
class GameState:
    """ Keep track of rounds, turns and selected """
    game_round: int = 0
    team_turn: int = 0
    turn_timer: float = TURN_MAX_TIME 
    board: Piece = None
    menu: Piece = None
