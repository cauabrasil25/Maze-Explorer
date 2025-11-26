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
        """Show player's metrics for each algorithm.

        Expects `player` to expose `metrics` (dict) or
        `get_all_metrics(algorithm)`.
        """
        print("=----------------- Scores ------------------=")
        metrics_dict = getattr(player, 'metrics', None)
        if metrics_dict is None:
            # fallback: try get_all_metrics method
            try:
                algos = []
                # attempt to discover known algorithms by probing
                for name in ['BFS', 'DFS', 'A*', 'Minimax', 'Hillclimbing']:
                    m = player.get_all_metrics(name)
                    if m:
                        algos.append((name, m))
            except Exception:
                algos = []
        else:
            algos = list(metrics_dict.items())

        if not algos:
            print("No metrics available.")
        else:
            for algorithm, m in algos:
                print(f"{algorithm}:")
                if not m:
                    print("  (no metrics)")
                    continue
                for k, v in m.items():
                    val = v if v is not None else "-"
                    print(f"  {k}: {val}")

        print("=-------------------------------------------=")

    def showExitConfirmation():
        """Show exit confirmation prompt."""
        print("Are you sure you want to exit? (y/n)")

    def showEndScreen():
        """Show end screen."""
        print("===========================================")
        print("         Thank you for playing!            ")
        print("===========================================")    
