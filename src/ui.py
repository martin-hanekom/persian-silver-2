from dataclasses import dataclass
import math
import pygame
from game import g
from piece import Piece
from tools import Resource
from conf import cc

@dataclass
class Ui:
    def __init__(self):
        self.panel = pygame.Rect(
            (cc.video.size[0] - cc.ui.width - cc.ui.padding, cc.ui.padding),
            (cc.ui.width, cc.video.size[1] - 2 * cc.ui.padding))
        self.menu = UiMenu(self.panel)
        self.turn = UiTurn(self.panel)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, cc.color.ui.base, self.panel, border_radius=3)
        self.menu.draw(screen)
        self.turn.draw(screen)

    def update(self, dt: float):
        self.turn.update(dt)

    def mouse_move(self, mouse_pos: (float, float)):
        self.menu.mouse_move(mouse_pos)
        self.turn.mouse_move(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        self.menu.mouse_clicked(mouse_pos)
        self.turn.mouse_clicked(mouse_pos)

@dataclass
class UiTurn:
    panel: pygame.Rect
    button: pygame.Rect
    button_text: pygame.Surface
    description: list[pygame.Surface]
    timer: int
    warn_timer: float
    hover: bool
    flash: int

    def __init__(self, panel: pygame.Rect):
        self.panel = panel
        self.button = pygame.Rect(self.panel.left + self.panel.width - cc.ui.turn.size[0] - 20, self.panel.top + self.panel.height - cc.ui.turn.size[1] - 20, *cc.ui.turn.size)
        self.button_text = Resource.fonts.get("systeml").render("END TURN", True, cc.color.background.base)
        self.description = [Resource.fonts.get("system").render(f"Player {i + 1}'s turn", True, cc.color.ui.text) for i in range(cc.player.amount)]
        self.timer = 0
        self.warn_timer = 0.5
        self.timer_text = Resource.fonts.get("system").render(f"0:{self.timer}", True, cc.color.background.base)
        self.hover = False
        self.flash = 0

    def draw(self, screen: pygame.Surface):
        color = self.hover if not self.flash else self.flash - 1
        pygame.draw.rect(screen, cc.color.sector.base[color], self.button, border_radius=3)
        desc_w, desc_h = self.description[g().state.team_turn].get_size()
        bt_w, bt_h = self.button_text.get_size()
        tt_w, tt_h = self.timer_text.get_size()
        screen.blit(self.description[g().state.team_turn], (self.button.left + (self.button.width - desc_w) / 2, self.button.top - 30))
        screen.blit(self.button_text, (self.button.left + (self.button.width - bt_w) / 2, self.button.top + (self.button.height - bt_h) / 2 - 10))
        screen.blit(self.timer_text, (self.button.left + (self.button.width - tt_w) / 2, self.button.top + self.button.height - tt_h - 10))

    def update(self, dt: float):
        if g().state.turn_timer < self.timer or g().state.turn_timer > self.timer + 1:
            self.timer = math.floor(g().state.turn_timer)
            self.timer_text = Resource.fonts.get("system").render(f"0:{self.timer}", True, cc.color.background.base)
        if self.timer <= cc.player.turn.warning:
            self.warn_timer -= dt / 1000
            if not self.flash:
                self.flash = 1
            if self.warn_timer < 0:
                self.warn_timer = 0.5
                self.flash = (self.flash * 2) % 3
        else:
            self.flash = 0

    def mouse_move(self, mouse_pos: (float, float)):
        self.hover = self.button.collidepoint(mouse_pos)

    def mouse_clicked(self, mouse_pos: (float, float)):
        if self.button.collidepoint(mouse_pos):
            g().end_turn()

@dataclass
class UiMenu:
    panel: pygame.Rect
    menu_text: pygame.Surface
    slot_pos: list[(int, int)]
    filled_slots: list[Piece]
    empty_slots: list[pygame.Rect]
    hovers: list[bool]

    def __init__(self, panel: pygame.Rect):
        self.panel = panel
        self.menu_text = Resource.fonts.get("systeml").render("Building Menu", True, cc.color.ui.text)
        self.slot_pos = []
        x, y = (self.panel.left + cc.ui.menu.padding, self.panel.top + self.menu_text.get_size()[1] + 2 * cc.ui.menu.padding)
        for i in range(cc.ui.menu.slots):
            self.slot_pos.append((x, y))
            x += cc.piece.size[0] + cc.ui.menu.padding
            if x > self.panel.left + self.panel.width - cc.piece.size[0] - cc.ui.menu.padding:
                x = self.panel.left + cc.ui.menu.padding
                y += cc.piece.size[1] + cc.ui.menu.padding
        self.filled_slots = [None for _ in range(cc.ui.menu.slots)]
        self.empty_slots = [pygame.Rect(*slot, *cc.piece.size) for slot in self.slot_pos]
        self.hovers = [False for _ in range(cc.ui.menu.slots)]

    def draw(self, screen: pygame.Surface):
        screen.blit(self.menu_text, (self.panel.left + cc.ui.menu.padding, self.panel.top + cc.ui.menu.padding))
        for filled, empty, pos, hover in zip(self.filled_slots, self.empty_slots, self.slot_pos, self.hovers):
            color = cc.color.background.hover if hover else cc.color.background.base
            pygame.draw.rect(screen, color, empty, border_radius=3)
            if filled:
                filled.draw(screen, pos)

    def set_pieces(self, pieces: list[Piece]):
        self.filled_slots = [None for _ in range(cc.ui.menu.slots)]
        for index, piece in enumerate(pieces):
            self.filled_slots[index] = piece

    def mouse_move(self, mouse_pos: (float, float)):
        self.hovers = [empty.collidepoint(mouse_pos) for empty in self.empty_slots]

    def mouse_clicked(self, mouse_pos: (float, float)):
        for filled, empty in zip(self.filled_slots, self.empty_slots):
            if empty.collidepoint(mouse_pos):
                g().menu_select(filled)
