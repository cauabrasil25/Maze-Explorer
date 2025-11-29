import time
from typing import List, Tuple, Dict

Position = Tuple[int, int]


class Hillclimbing:
    """Simple hill-climbing (greedy) local search for the maze.

    The algorithm moves from the start to the neighbor with the best
    heuristic (Manhattan distance to goal) if it improves the heuristic.
    Stops when no improving neighbor exists or when the end is reached.

    Returns (path, metrics) where metrics contains `score`, `time`, `cost`.
    `cost` here is the number of nodes inspected/expanded.
    """

    @staticmethod
    def search(maze) -> Tuple[List[Position], Dict]:
        start_time = time.time()

        grid = getattr(maze, 'grid', None)
        walls = set(getattr(maze, 'walls', []))
        items = set(getattr(maze, 'itens', []))
        enemies = set(getattr(maze, 'enemys', []))
        start = getattr(maze, 'start', None) or getattr(maze, 'player', None)
        end = getattr(maze, 'end', None)

        if start is None or end is None:
            return [], {'score': 0, 'time': 0.0, 'cost': 0}

        max_y = len(grid) if grid else 0
        max_x = len(grid[0]) if grid and grid[0] else 0

        def neighbors(pos):
            x, y = pos
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if (nx, ny) not in walls:
                        yield (nx, ny)

        def heuristic(a: Position, b: Position) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        path: List[Position] = [start]
        visited = {start}
        current = start
        expanded = 0
        found = False

        cur_h = heuristic(current, end)

        while True:
            if current == end:
                found = True
                break

            # evaluate neighbors and pick best (lowest heuristic)
            best = None
            best_h = cur_h
            inspected = 0
            for nb in neighbors(current):
                inspected += 1
                h = heuristic(nb, end)
                if h < best_h and nb not in visited:
                    best = nb
                    best_h = h

            expanded += inspected

            if best is None:
                # no improving neighbor; stop (local maximum)
                break

            # move to best neighbor
            current = best
            visited.add(current)
            path.append(current)
            cur_h = best_h

        # compute metrics
        steps = max(0, len(path) - 1)
        score = 0
        for pos in path:
            if pos in items:
                score += 100
            if pos in enemies:
                score -= 50
        score -= steps * 5
        if found:
            score += 1000

        elapsed = time.time() - start_time
        metrics = {
            'score': score,
            'time': elapsed,
            'cost': expanded
        }

        return path, metrics


def hillclimbing_search(maze):
    """Module-level wrapper to match other algorithm modules' API.

    Returns (path, metrics).
    """
    return Hillclimbing.search(maze)
