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

    def showGameScreen(path, maze=None):
        """Show final trajectory of the player.

        Args:
            path: list of (x,y) positions returned by the pathfinder.
            maze: optional Maze instance (to draw ASCII map with path).
        """
        print("=---------------- Game Path ----------------=")
        if not path:
            print("No path found.")
            print("=-------------------------------------------=")
            return

        steps = max(0, len(path)-1)
        print(f"Steps: {steps} | Path length: {len(path)}")
        # print coordinates
        for i, (x, y) in enumerate(path):
            tag = 'Start' if i == 0 else ('End' if i == len(path)-1 else f'Step{i}')
            print(f"{tag}: ({x}, {y})")

        # if maze provided, draw ASCII map with path marked
        if maze is not None and getattr(maze, 'grid', None) is not None:
            print('\nMap with path ("*" marks path):')
            # copy grid (rows are lists)
            grid = [list(row) for row in maze.grid]
            for i, (x, y) in enumerate(path):
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                    if i == 0:
                        grid[y][x] = 'P'
                    elif i == len(path)-1:
                        grid[y][x] = 'E'
                    else:
                        grid[y][x] = '*'
            for row in grid:
                print(''.join(row))

        print("=-------------------------------------------=")
