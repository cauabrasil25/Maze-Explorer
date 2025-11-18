class Display:
    """Print menus and player info to console."""
    # Dispatcher moved to Controller. Keep display helpers below.
    
    def showStartScreen():
        """Show start screen."""
        print("===========================================")
        print("        Welcome to Maze Explorer!          ")
        print("===========================================")
        print("Press Enter to continue...", end='')
    
    def showMenu():
        """Show main menu."""
        print("=---------------- Main Menu ----------------=")
        print("1. Start Maze Game")
        print("2. View Scores")
        print("3. Set Algorithm")
        print("4. Exit")
        print("=-------------------------------------------=")
        print("Select an option (1-4): ", end='')

    def showAlgorithms(player):
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
        print("Select an algorithm (1-6): ", end='')

    def showScores(player):
        """Show player's scores."""
        print("=----------------- Scores ------------------=")
        for algorithm, score in player.score:
            print(f"{algorithm}: {score}")
        print("=-------------------------------------------=")

    def showExitConfirmation():
        """Show exit confirmation prompt."""
        print("Are you sure you want to exit? (y/n)")

    def showEndScreen():
        """Show end screen."""
        print("===========================================")
        print("         Thank you for playing!            ")
        print("===========================================")    
