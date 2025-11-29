import time
from collections import deque
from typing import List, Tuple, Dict, Optional


Position = Tuple[int, int]


class Bfs:
	"""Breadth-first search implementation for the maze.

	Usage:
		path, metrics = Bfs.bfs_search(maze)

	Returns:
		path: list of (x,y) positions from start to end (inclusive) or [] if no path
		metrics: dict with keys `score`, `time`, `steps`, `expanded`
	"""

	@staticmethod
	def bfs_search(maze) -> Tuple[List[Position], Dict]:
		"""Run BFS on `maze` and compute score according to rules.

		Scoring rules:
			- start with 0 points
			- each item found: +100
			- each enemy/trap encountered: -50
			- each step taken: -5 (per move)
			- finishing the maze (reaching end): +1000

		The function treats items/enemies only if they lie on the final path.
		"""
		start_time = time.time()

		# grid and obstacles
		grid = getattr(maze, 'grid', None)
		walls = set(getattr(maze, 'walls', []))
		items = set(getattr(maze, 'itens', []))
		enemies = set(getattr(maze, 'enemys', []))
		start = getattr(maze, 'start', None) or getattr(maze, 'player', None)
		end = getattr(maze, 'end', None)

		if start is None or end is None:
			return [], {'score': 0, 'time': 0.0, 'steps': 0, 'expanded': 0}

		# BFS
		q = deque()
		q.append(start)
		parents = {start: None}
		visited = {start}
		expanded = 0

		max_y = len(grid) if grid else 0
		max_x = len(grid[0]) if grid and grid[0] else 0

		def neighbors(pos: Position):
			x, y = pos
			for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
				nx, ny = x+dx, y+dy
				if 0 <= nx < max_x and 0 <= ny < max_y:
					if (nx, ny) not in walls:
						yield (nx, ny)

		found = False
		while q:
			cur = q.popleft()
			expanded += 1
			if cur == end:
				found = True
				break
			for nb in neighbors(cur):
				if nb not in visited:
					visited.add(nb)
					parents[nb] = cur
					q.append(nb)

		path: List[Position] = []
		if found:
			node = end
			while node is not None:
				path.append(node)
				node = parents.get(node)
			path.reverse()

		# compute metrics
		steps = max(0, len(path)-1)
		score = 0
		# count items/enemies on path (excluding start if desired)
		for pos in path:
			if pos in items:
				score += 100
			if pos in enemies:
				score -= 50
		# each step costs -5
		score -= steps * 5
		# finishing bonus
		if found:
			score += 1000

		elapsed = time.time() - start_time
		# cost: operational cost measured as number of expanded nodes
		cost = expanded
		metrics = {
			'score': score,
			'time': elapsed,
			'cost': cost
		}

		return path, metrics

