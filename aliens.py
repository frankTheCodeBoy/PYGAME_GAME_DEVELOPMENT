import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self,first_play):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.screen = first_play.screen

        # Load image and set rect attribute
        self.image = pygame.image.load("game_pics/space_ship.png")
        self.rect = self.image.get_rect()

        # Start each image near the top left screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position
        self.y = float(self.rect.y)


