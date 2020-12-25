import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self,first_play):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.screen = first_play.screen
        self.settings = first_play.settings
   
        # Load image and set rect attribute
        self.image = pygame.image.load("game_pics/space_ship.png")
        self.rect = self.image.get_rect()

        # Start each image near the top left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            return True

    def update(self):
        """Move the alien to the up or down."""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y


