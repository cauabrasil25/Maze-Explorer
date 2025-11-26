class Player:
    """Player with per-algorithm metrics (score, time, cost, ...)."""

    def __init__(self):
        """Init defaults: metrics dict and default algorithm 'BFS'.

        `self.metrics` is a dict mapping algorithm name -> metrics dict.
        Each metrics dict can contain keys like `score`, `time`, `cost`.
        """
        # default algorithms and empty metrics
        algos = ["BFS", "DFS", "A*", "Minimax", "Hillclimbing"]
        self.metrics = {a: {"score": 0, "time": None, "cost": None} for a in algos}
        self.Algorithm = "BFS"

    # --- convenience setters/getters for single metric ---
    def set_score(self, score, algorithm=None):
        """Set numeric score for an algorithm.

        If `algorithm` is None, uses the current active algorithm.
        """
        if algorithm is None:
            algorithm = self.Algorithm
        self.set_metric(algorithm, "score", score)

    def get_score(self, algorithm=None):
        """Get score for an algorithm (or None if not found)."""
        if algorithm is None:
            algorithm = self.Algorithm
        return self.get_metric(algorithm, "score")

    # --- generic metric access ---
    def set_metric(self, algorithm, metric_name, value):
        """Set arbitrary metric for an algorithm.

        Args:
            algorithm (str): algorithm name.
            metric_name (str): e.g. 'score', 'time', 'cost'.
            value: metric value.
        """
        if algorithm not in self.metrics:
            # create entry if unknown algorithm
            self.metrics[algorithm] = {}
        self.metrics[algorithm][metric_name] = value

    def get_metric(self, algorithm, metric_name):
        """Return the requested metric or None if not present."""
        if algorithm not in self.metrics:
            return None
        return self.metrics[algorithm].get(metric_name)

    def set_metrics(self, algorithm, **kwargs):
        """Set multiple metrics at once (e.g. score=10, time=0.23)."""
        if algorithm not in self.metrics:
            self.metrics[algorithm] = {}
        for k, v in kwargs.items():
            self.metrics[algorithm][k] = v

    # --- algorithm selection ---
    def set_algorithm(self, algorithm):
        """Set active algorithm (string)."""
        self.Algorithm = algorithm

    def get_algorithm(self):
        """Get active algorithm."""
        return self.Algorithm

    # --- utility ---
    def get_all_metrics(self, algorithm=None):
        """Return the metrics dict for an algorithm."""
        if algorithm is None:
            algorithm = self.Algorithm
        return self.metrics.get(algorithm, {})
