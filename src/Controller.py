from enum import Enum

from src.Display import Display
from src.Player import Player
from src.Input import Input
from src.Maze import Maze

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
        # Atributo `State` guarda um membro de `State`.
        # Ex.: `self.state = State.INIT`
        self.state = State.INIT
        self.player = Player()
        # keep references to helper modules/classes
        self.display_obj = Display
        self.input_obj = Input
        self.running = True
        self.maze = Maze()

    def setState(self, state):
        """Set new state for controller."""
        self.state = state

    def getState(self):
        """Get current state of controller."""
        return self.state
    
    def handle_input(self):
        """Handle input for the current state (dispatch moved here)."""
        st = self.state
        match st:
            case State.INIT:
                return None
            case State.WELCOME_SCREEN:
                # no input expected; proceed
                return None
            case State.MAIN_MENU:
                choice = self.input_obj.mainMenuInput()
                if choice == '1':
                    self.setState(State.MAIN_GAME)
                elif choice == '2':
                    self.setState(State.VIEW_SCORES)
                elif choice == '3':
                    self.setState(State.SET_ALGORITHM)
                elif choice == '4':
                    self.setState(State.EXIT)
                return choice
            case State.SET_ALGORITHM:
                choice = self.input_obj.algorithmMenuInput()
                mapping = {'1': 'BFS', '2': 'DFS', '3': 'A*', '4': 'Minimax', '5': 'Hillclimbing'}
                if choice in mapping:
                    self.player.set_algorithm(mapping[choice])
                # any selection returns to main menu
                self.setState(State.MAIN_MENU)
                return choice
            case State.VIEW_SCORES:
                self.input_obj.showScoresInput()
                self.setState(State.MAIN_MENU)
                return None
            case State.EXIT:
                choice = self.input_obj.exitConfirmationInput()
                if isinstance(choice, str) and choice.lower().startswith('y'):
                    self.setState(State.END)
                    self.running = False
                else:
                    self.setState(State.MAIN_MENU)
                return choice
            case State.MAIN_GAME:
                # gameplay input handled elsewhere; we simulate no-input here
                return None

    def handle_display(self):
        """Display UI for the current state (dispatch moved here)."""
        st = self.state
        # call Display functions (Display class methods)
        match st:
            case State.INIT:
                self.display_obj.showStartScreen()
            case State.WELCOME_SCREEN:
                self.display_obj.showStartScreen()
            case State.MAIN_MENU:
                self.display_obj.showMenu()
            case State.SET_ALGORITHM:
                self.display_obj.showAlgorithms(self.player)
            case State.VIEW_SCORES:
                self.display_obj.showScores(self.player)
            case State.EXIT:
                self.display_obj.showExitConfirmation()
            case State.END:
                self.display_obj.showEndScreen()
            case State.MAIN_GAME:
                # could show game screen; placeholder
                print('Game running... (simulated)')

    def update(self):
        """Update controller state based on current state.

        This method handles transitions that are not directly caused by
        user input (e.g., initialization).
        """
        match self.state:
            case State.INIT:
                self.maze.readMaze()
                self.setState(State.WELCOME_SCREEN)
            case State.WELCOME_SCREEN:
                # after showing welcome, move to main menu
                self.setState(State.MAIN_MENU)
            case State.MAIN_GAME:
                # simulate a finished run: give player a score and return to menu
                self.player.set_score(self.player.get_score(self.player.get_algorithm()) + 10, self.player.get_algorithm())
                self.setState(State.MAIN_MENU)
            case _:
                pass
