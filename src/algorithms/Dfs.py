import time
from typing import List, Tuple, Dict

Position = Tuple[int, int]


class Dfs:
    """Depth-first search implementation for the maze.

    Provides a static method `dfs_search(maze)` that returns (path, metrics)
    where `path` is a list of (x,y) positions from start to end (or []),
    and `metrics` is a dict with keys `score`, `time`, `cost` (cost = expanded nodes).
    """

    @staticmethod
    def dfs_search(maze) -> Tuple[List[Position], Dict]:
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

        # iterative DFS using stack to avoid recursion depth issues
        stack = [(start, None)]  # (node, parent)
        parents = {start: None}
        visited = {start}
        expanded = 0
        found = False

        while stack:
            node, parent = stack.pop()
            expanded += 1
            # parent already recorded by pushing neighbors
            if node == end:
                found = True
                break
            # push neighbors in reverse order to mimic recursive DFS order
            for nb in neighbors(node):
                if nb not in visited:
                    visited.add(nb)
                    parents[nb] = node
                    stack.append((nb, node))

        path: List[Position] = []
        if found:
            cur = end
            while cur is not None:
                path.append(cur)
                cur = parents.get(cur)
            path.reverse()

        # compute score following the same rules as BFS
        steps = max(0, len(path)-1)
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
