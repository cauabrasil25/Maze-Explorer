from enum import Enum

from Display import Display
import Input
from Player import Player


class State(Enum):
    """Possible states."""
    INIT = 0
    WELCOME_SCREEN = 1
    MAIN_MENU = 2
    MAIN_GAME = 3   
    VIEW_SCORES = 4
    SET_ALGORITHM = 5
    EXIT = 6
    END = 7


class Controller:
    """Controller placeholder: implement game flow here."""

    def __init__(self):
        # Atributo `estate` guarda um membro de `Estate`.
        # Ex.: `self.estate = Estate.INIT`
        self.state = State.INIT
        self.player = Player()
        self.display = Display()
        self.input = Input()
        self.running = True

    def setState(self, state):
        """Set new state for controller."""
        self.state = state

    def getState(self):
        """Get current state of controller."""
        return self.state
    
    def input(self, state):
        """Handle input based on current state."""
        self.input.MainswitchInput(state)

    def display(self, state, player):
        """Handle display based on current state."""
        self.display.MainswitchDisplay(state, player)

    def update(self):
        """Update controller state based on current estate."""
        match self.state:
            case State.INIT:
                pass  
