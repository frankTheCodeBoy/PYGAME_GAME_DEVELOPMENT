class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,205)

        # Goku settings
        self.goku_lives = 3
        
        # Bullet settings
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = (139,0,0)
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_cruise_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.alien_speed = 1.5
        self.bullet_speed = 3.0
        self.goku_speed = 2.0 
        
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1

        # Scoring.
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.alien_speed *= self.speedup_scale  
        self.bullet_speed *= self.speedup_scale
        self.goku_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


















