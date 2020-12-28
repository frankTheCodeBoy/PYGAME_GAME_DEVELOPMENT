class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self,first_play):
        """Initialize statistics."""
        self.settings = first_play.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.goku_left = self.settings.goku_lives