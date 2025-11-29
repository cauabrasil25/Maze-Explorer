import time
from typing import List, Tuple, Dict

Position = Tuple[int, int]


class Minimax:
    """Depth-limited minimax-like search for single-agent maze.

    This implementation treats the environment adversarially in a
    simplified manner: it alternates between "max" (player choosing a move)
    and "min" (adversary choosing the worst outcome among the player's
    reachable positions). The adversary does not move enemies explicitly
    but simulates worst-case continuation, which makes the search
    pessimistic and useful to avoid risky positions.

    The method returns a tuple `(path, metrics)` to match the other
    algorithm modules. `metrics` contains `score`, `time`, `cost`.
    """

    @staticmethod
    def minimax_search(maze, depth_limit: int = 6) -> Tuple[List[Position], Dict]:
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

        def neighbors(pos: Position):
            x, y = pos
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if (nx, ny) not in walls:
                        yield (nx, ny)

        def heuristic(a: Position, b: Position) -> int:
            # Manhattan distance
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # counter for expanded nodes
        expanded = 0

        # memoization to avoid recomputing identical states (pos, depth, maximizing)
        cache = {}

        def evaluate(pos: Position) -> float:
            # simple static evaluation used at depth limit: closer to goal is better,
            # items on position are good, enemy on position is very bad
            if pos in enemies:
                return -10000.0
            val = -heuristic(pos, end)  # closer to goal => less negative
            if pos in items:
                val += 100.0
            return val

        def minimax(pos: Position, depth: int, maximizing: bool, visited: frozenset) -> Tuple[float, List[Position]]:
            nonlocal expanded
            key = (pos, depth, maximizing)
            if key in cache:
                return cache[key]

            expanded += 1

            # terminal conditions
            if pos == end:
                cache[key] = (10000.0, [pos])
                return cache[key]
            if depth == 0:
                val = evaluate(pos)
                cache[key] = (val, [pos])
                return cache[key]

            best_path: List[Position] = [pos]

            if maximizing:
                best_val = float('-inf')
                for nb in neighbors(pos):
                    if nb in visited:
                        continue
                    v, p = minimax(nb, depth - 1, False, visited | {nb})
                    if v > best_val:
                        best_val = v
                        best_path = [pos] + p
                if best_val == float('-inf'):
                    best_val = evaluate(pos)
                    best_path = [pos]
                cache[key] = (best_val, best_path)
                return cache[key]
            else:
                # adversary (min) chooses the continuation that minimizes player's value
                worst_val = float('inf')
                for nb in neighbors(pos):
                    if nb in visited:
                        continue
                    v, p = minimax(nb, depth - 1, True, visited | {nb})
                    if v < worst_val:
                        worst_val = v
                        best_path = [pos] + p
                if worst_val == float('inf'):
                    worst_val = evaluate(pos)
                    best_path = [pos]
                cache[key] = (worst_val, best_path)
                return cache[key]

        # run minimax from start (player to move)
        val, path = minimax(start, depth_limit, True, frozenset({start}))

        # compute final metrics using same scoring rules as other algorithms
        steps = max(0, len(path) - 1)
        score = 0
        found = False
        for pos in path:
            if pos in items:
                score += 100
            if pos in enemies:
                score -= 50
            if pos == end:
                found = True
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


def minimax_search(maze, depth: int = 6):
    """Module wrapper to match other algorithm modules' API."""
    return Minimax.minimax_search(maze, depth)
    