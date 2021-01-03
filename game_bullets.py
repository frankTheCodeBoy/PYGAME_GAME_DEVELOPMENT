import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage character bullets"""
    def __init__(self,first_play):
        """Create bullets at character location"""
        super().__init__()
        self.screen = first_play.screen
        self.settings = first_play.settings
        self.color = self.settings.bullet_color
        # Create bullet at 0,0 then correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.center = first_play.goku.rect.center
        # Store bullet speed as float value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally across the screen"""
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
