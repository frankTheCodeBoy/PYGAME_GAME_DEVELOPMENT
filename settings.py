class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (139,0,0)

        # Ship settings
        self.goku_speed = 2.0

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 7
        self.bullet_height = 19
        self.bullet_color = (0,0,250)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_cruise_speed = 10
        self.goku_lives = 3
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1
        