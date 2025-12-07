"""
Algorithm Performance Tracker
Tracks comparisons, swaps, steps, and execution time
"""

class AlgorithmTracker:
    def __init__(self):
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0

    def reset(self):
        """Reset all tracking metrics"""
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0