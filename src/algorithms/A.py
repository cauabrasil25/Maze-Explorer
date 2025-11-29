import time
import heapq
from typing import List, Tuple, Dict

Position = Tuple[int, int]


class A:
	"""A* search implementation for the maze.

	Usage:
		path, metrics = A.astar_search(maze)

	Returns:
		path: list of (x,y) positions from start to end (inclusive) or [] if no path
		metrics: dict with keys `score`, `time`, `cost` (cost = expanded nodes)
	"""

	@staticmethod
	def astar_search(maze) -> Tuple[List[Position], Dict]:
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
			for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
				nx, ny = x+dx, y+dy
				if 0 <= nx < max_x and 0 <= ny < max_y:
					if (nx, ny) not in walls:
						yield (nx, ny)

		def heuristic(a: Position, b: Position) -> int:
			# Manhattan distance
			return abs(a[0] - b[0]) + abs(a[1] - b[1])

		open_heap = []  # elements are (f, g, position)
		heapq.heappush(open_heap, (heuristic(start, end), 0, start))
		came_from = {start: None}
		g_score = {start: 0}
		closed = set()
		expanded = 0

		found = False
		while open_heap:
			f, g, current = heapq.heappop(open_heap)
			# skip if we've already processed a better path to current
			if current in closed:
				continue
			closed.add(current)
			expanded += 1

			if current == end:
				found = True
				break

			for nb in neighbors(current):
				tentative_g = g + 1
				if nb in g_score and tentative_g >= g_score[nb]:
					continue
				# record best path so far
				came_from[nb] = current
				g_score[nb] = tentative_g
				f_score = tentative_g + heuristic(nb, end)
				heapq.heappush(open_heap, (f_score, tentative_g, nb))

		path: List[Position] = []
		if found:
			node = end
			while node is not None:
				path.append(node)
				node = came_from.get(node)
			path.reverse()

		# compute metrics as requested
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
