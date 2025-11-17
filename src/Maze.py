class Maze: 

    """Class representing the maze structure."""

    def __init__(self):
        
        """Initialize maze with default parameters."""
        self.enemys = []
        self.itens = []
        self.walls = []
        self.emptys = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.player = (0, 0)

    def add_wall(self, position):
        
        """Add a wall at the specified position."""
        self.walls.append(position)

    def add_item(self, item):
        
        """Add an item to the maze."""
        self.itens.append(item)

    def add_enemy(self, enemy):
        
        """Add an enemy to the maze."""
        self.enemys.append(enemy)

    def add_empty(self, position):
        
        """Add an empty space to the maze."""
        self.emptys.append(position)

    def add_trap(self, trap):
        
        """Add a trap to the maze."""
        self.traps.append(trap)

    def set_start(self, position):
        
        """Set the starting position of the maze."""
        self.start = position   
    
    def set_end(self, position):
        
        """Set the ending position of the maze."""
        self.end = position

    def set_playerPosition(self, position):
        
        """Set the player's position in the maze."""
        self.playerPosition = position

    def readMaze(self):
        """Read maze from `resource/maze.txt` and populate structure.

        The expected characters in the file:
            '#': wall
            'P': player start/position
            'X': end/goal
            'I': item
            'E': enemy
            'T': trap
            '.': empty space
            other chars are ignored or treated as empty.

        Coordinates use (x, y) with x = column, y = row (0-based).
        """
        from pathlib import Path

        repo_root = Path(__file__).parent.parent
        maze_file = repo_root / 'resource' / 'maze.txt'

        if not maze_file.exists():
            raise FileNotFoundError(f"Maze file not found: {maze_file}")

        with maze_file.open('r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f if line.strip() != '']

        # optional: keep a grid representation
        self.grid = []

        for y, line in enumerate(lines):
            row = []
            for x, ch in enumerate(line):
                row.append(ch)
                pos = (x, y)
                if ch == '#':
                    self.add_wall(pos)
                elif ch == 'P':
                    self.set_player(pos)
                    self.set_start(pos)
                elif ch == 'E':
                    self.add_enemy(pos)
                elif ch == 'I':
                    self.add_item(pos)
                elif ch == 'X':
                    self.set_end(pos)
                elif ch == '.':
                    self.add_empty(pos)
                elif ch == 'T':
                    self.add_trap(pos)
            self.grid.append(row)
