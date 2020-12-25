import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self,first_play):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.screen = first_play.screen

        # Define alien speed setting
        self.alien_speed = 1.0

        # Load image and set rect attribute
        self.image = pygame.image.load("game_pics/space_ship.png")
        self.rect = self.image.get_rect()

        # Start each image near the top left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact vertical position
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right."""
        self.y += self.alien_speed
        self.rect.y = self.y


