import time
import os


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
                    if v is None:
                        val = "-"
                    else:
                        # format numeric metrics more readably
                        if k.lower() == 'time':
                            try:
                                fv = float(v)
                                # adaptive units: seconds, milliseconds, microseconds
                                if fv >= 1.0:
                                    val = f"{fv:.3f}s"
                                elif fv >= 0.001:
                                    val = f"{fv*1000:.3f}ms"
                                elif fv >= 0.000001:
                                    val = f"{fv*1000000:.3f}µs"
                                else:
                                    # extremely small: show full precision in seconds
                                    val = f"{fv:.9f}s"
                            except Exception:
                                val = str(v)
                        elif isinstance(v, float):
                            # other floats: 3 decimal places
                            val = f"{v:.3f}"
                        else:
                            val = str(v)
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

    def showGameScreen(path, maze=None, animate=True, delay=1.0):
        """Show final trajectory of the player.

        If `animate=True`, show step-by-step progression with a delay
        between frames. `delay` controls seconds between frames.

        Args:
            path: list of (x,y) positions returned by the pathfinder.
            maze: optional Maze instance (to draw ASCII map with path).
            animate: whether to print the path step-by-step.
            delay: seconds to wait between steps when animating.
        """
        print("=---------------- Game Path ----------------=")
        if not path:
            print("No path found.")
            print("=-------------------------------------------=")
            return

        steps = max(0, len(path) - 1)
        print(f"Steps: {steps} | Path length: {len(path)}")

        # helper to render map with current player position and optional trail
        def render_at(pos_index):
            # if no maze grid, just print coords
            if maze is None or getattr(maze, 'grid', None) is None:
                cur = path[pos_index]
                print(f"Player at: {cur} (step {pos_index}/{len(path)-1})")
                return

            grid = [list(row) for row in maze.grid]
            # mark trail with '*' except start/end
            for i, (x, y) in enumerate(path):
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                    if i == 0:
                        grid[y][x] = 'P'
                    elif i == len(path) - 1:
                        grid[y][x] = 'E'
                    else:
                        grid[y][x] = '*'
            # override current position with 'P' to show movement
            cx, cy = path[pos_index]
            if 0 <= cy < len(grid) and 0 <= cx < len(grid[0]):
                grid[cy][cx] = 'P'

            for row in grid:
                print(''.join(row))

        if animate:
            for i in range(len(path)):
                # clear terminal
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception:
                    print('\033c', end='')
                print(f"Step {i}/{len(path)-1}")
                render_at(i)
                time.sleep(delay)
            # final frame summary
            print('\nFinal path:')
            render_at(len(path) - 1)
        else:
            # non-animated: print coordinates and map with path
            for i, (x, y) in enumerate(path):
                tag = 'Start' if i == 0 else ('End' if i == len(path) - 1 else f'Step{i}')
                print(f"{tag}: ({x}, {y})")
            if maze is not None and getattr(maze, 'grid', None) is not None:
                print('\nMap with path ("*" marks path):')
                render_at(len(path) - 1)

        print("=-------------------------------------------=")
