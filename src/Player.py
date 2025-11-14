class Player:
    
    def __init__(self):
        self.name = ""
        self.score = [("BFS", 0), ("DFS", 0), ("A*", 0), ("Minimax", 0), ("Hillclimbing", 0)]

        
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_score(self, score, algorithm):
        for i in range(len(self.score)):
            if self.score[i][0] == algorithm:
                self.score[i] = (algorithm, score)
                break

    def get_score(self, algorithm):
        for i in range(len(self.score)):
            if self.score[i][0] == algorithm:
                return self.score[i][1]
        return None
