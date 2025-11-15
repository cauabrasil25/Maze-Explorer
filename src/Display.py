class Display:
    """Print menus and player info to console."""

    def MainswitchDisplay(estate, player):
        switcher = {
            'INIT': Display.ShowStartScreen,
            'MAIN_MENU': Display.ShowMenu,
            'SET_ALGORITHM': lambda: Display.ShowAlgorithms(player),
            'EXIT': Display.ShowExitConfirmation,
            'VIEW_SCORES': lambda: Display.ShowScores(player)
        }
        func = switcher.get(estate.name, lambda: None)
        func()
    
    def ShowStartScreen():
        """Show start screen."""
        print("===========================================")
        print("        Welcome to Maze Explorer!          ")
        print("===========================================")
    
    def ShowMenu():
        """Show main menu."""
        print("=---------------- Main Menu ----------------=")
        print("1. Start Maze Game")
        print("2. View Scores")
        print("3. Set Algorithm")
        print("4. Exit")
        print("=-------------------------------------------=")

    def ShowAlgorithms(player):
        """Show algorithm menu and active algorithm."""
        print("=----------- Select Algorithm -------------=")
        print("1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. Minimax")
        print("5. Hillclimbing")
        print("6. Back to Main Menu")
        print("Active Algorithm: " + player.get_algorithm())
        print("=-------------------------------------------=")

    def ShowScores(player):
        """Show player's name and scores."""
        print("=----------------- Scores ------------------=")
        print(f"Player: {player.get_name()}")
        for algorithm, score in player.score:
            print(f"{algorithm}: {score}")
        print("=-------------------------------------------=")

    def ShowExitConfirmation():
        """Show exit confirmation prompt."""
        print("Are you sure you want to exit? (y/n)")

    def ShowEndScreen():
        """Show end screen."""
        print("===========================================")
        print("         Thank you for playing!            ")
        print("===========================================")    
