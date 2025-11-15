from enum import Enum

from Display import Display
import Input
from Player import Player


class State(Enum):
    """Possible states."""
    INIT = 0
    MAIN_MENU = 1
    MAIN_GAME = 2
    VIEW_SCORES = 3
    SET_ALGORITHM = 4
    EXIT = 5
    END = 6


class Controller:
    """Controller placeholder: implement game flow here."""

    def __init__(self):
        # Atributo `estate` guarda um membro de `Estate`.
        # Ex.: `self.estate = Estate.INIT`
        self.estate = State.INIT
        self.player = Player()
        self.display = Display()
        self.input = Input()
        self.running = True

    def setEstate(self, state):
        """Set new state for controller."""
        self.estate = state

    def getEstate(self):
        """Get current state of controller."""
        return self.estate
    
    def input(self, estate):
        """Handle input based on current estate."""
        self.input.MainswitchInput(estate)

    def display(self, estate, player):
        """Handle display based on current estate."""
        self.display.MainswitchDisplay(estate, player)

    def update(self):
        """Update controller state based on current estate."""
        pass  # Implement state update logic here
