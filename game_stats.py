class GameStats:
    """Track statistics for Game Character"""

    def __init__(self,goku_limit=3):
        """define limit, and areset method"""
        self.goku_limit = goku_limit
        
    def keep_stats(self):
        """Initialize statistics that can change during the game"""
        self.goku_limit -= 1
        return self.goku_limit

    def reset_stats(self):
        """reset goku stats"""
        self.goku_limit = 3