from enum import Enum

import os

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

    def clear_screen(self):
        """Clear the terminal in a cross-platform way."""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            # fallback to ANSI sequence (may not work on all consoles)
            print('\033c', end='')

    def __init__(self):
        self.state = State.INIT
        self.player = Player()
        # keep references to helper modules/classes
        self.display_obj = Display
        self.input_obj = Input
        self.running = True
        self.maze = Maze()
        # Keep flags for navigation on input
        self.toExit = False
        self.toAlgorithmMenu = False
        self.toScoresMenu = False
        self.toMainMenu = False
        self.toMainGame = False
        self.toEnd = False

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
                # accept any input but don't change state here
                choice = self.input_obj.welcomeScreenInput()
                return choice
            case State.MAIN_MENU:
                choice = self.input_obj.mainMenuInput()
                # record requested action; do not change state here
                if choice == '1':
                    self.toMainGame = True
                elif choice == '2':
                    self.toScoresMenu = True
                elif choice == '3':
                    self.toAlgorithmMenu = True
                elif choice == '4':
                    self.toExit = True
                else:
                    print("Invalid choice. Please select a valid option.")
                return choice
            case State.SET_ALGORITHM:
                choice = self.input_obj.algorithmMenuInput()
                mapping = {'1': 'BFS', '2': 'DFS', '3': 'A*', '4': 'Minimax', '5': 'Hillclimbing'}
                if choice in mapping:
                    self.player.set_algorithm(mapping[choice])
                else:
                    print("Invalid choice. Please select a valid option.")
                self.toMainMenu = True
                return choice
            case State.VIEW_SCORES:
                # wait for Enter and then request return to menu
                self.input_obj.showScoresInput()
                self.toMainMenu = True
                return None
            case State.EXIT:
                choice = self.input_obj.exitConfirmationInput()
                # defer exit decision to update()
                if choice.lower() == 'y':
                    self.toEnd = True
                else:
                    self.toMainGame = True
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
                return None
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

        This method handles transitions.
        """
        # First handle automatic transitions
        match self.state:
            case State.INIT:
                self.maze.readMaze()
                # stay in WELCOME_SCREEN until user continues
                self.setState(State.WELCOME_SCREEN)
                self.clear_screen()
            case State.WELCOME_SCREEN:
                self.setState(State.MAIN_MENU)
                self.clear_screen()
            case State.MAIN_MENU:
                if self.toAlgorithmMenu:
                    self.setState(State.SET_ALGORITHM)
                    self.clear_screen()
                    self.toAlgorithmMenu = False
                elif self.toScoresMenu:
                    self.setState(State.VIEW_SCORES)
                    self.clear_screen()
                    self.toScoresMenu = False
                elif self.toExit:
                    self.setState(State.EXIT)
                    self.clear_screen()
                    self.toExit = False
                elif self.toMainGame:
                    self.setState(State.MAIN_GAME)
                    self.clear_screen()
                    self.toMainGame = False
            case State.MAIN_GAME:
                # simulate a finished run: give player a score and return to menu
                self.player.set_score(self.player.get_score(self.player.get_algorithm()) + 10, self.player.get_algorithm())
                self.setState(State.MAIN_MENU)
                self.clear_screen()
            case State.VIEW_SCORES:
                self.setState(State.MAIN_MENU)
                self.clear_screen()
            case State.SET_ALGORITHM:
                self.setState(State.MAIN_MENU)
                self.clear_screen() 
            case State.EXIT:
                if self.toEnd:
                    self.setState(State.END)
                    self.clear_screen()
                    self.running = False
                else:
                    self.setState(State.MAIN_MENU)
                    self.clear_screen()
                    self.toEnd = False