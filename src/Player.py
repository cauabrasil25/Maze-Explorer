class Player:
    """Player with scores and selected algorithm."""

    def __init__(self):
        """Init with defaults: zeroed scores, 'BFS'."""
        self.score = [("BFS", 0), ("DFS", 0), ("A*", 0), ("Minimax", 0), ("Hillclimbing", 0)]
        self.Algorithm = "BFS"
    
    def set_score(self, score, algorithm):
        """Set score for a specific algorithm."""
        for i in range(len(self.score)):
            if self.score[i][0] == algorithm:
                self.score[i] = (algorithm, score)
                break

    def get_score(self, algorithm):
        """Get score for an algorithm or None if not found."""
        for i in range(len(self.score)):
            if self.score[i][0] == algorithm:
                return self.score[i][1]
        return None
    
    def set_algorithm(self, algorithm):
        """Set active algorithm."""
        self.Algorithm = algorithm
    
    def get_algorithm(self):
        """Get active algorithm."""
        return self.Algorithm
