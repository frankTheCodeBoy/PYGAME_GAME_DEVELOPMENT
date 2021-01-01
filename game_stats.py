class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self,first_play):
        """Initialize statistics."""
        self.settings = first_play.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset
        import json
        with open("high_scores.json",'r') as f:
            self.high_score = json.load(f)

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.goku_left = self.settings.goku_lives
        self.score = 0
        self.level = 1
        