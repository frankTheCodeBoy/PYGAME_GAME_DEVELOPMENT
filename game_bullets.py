import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage character bullets"""
    def __init__(self,first_play):
        """Create bullets at character location"""
        super().__init__()
        self.screen = first_play.screen
        # bullet settings
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (250,0,0)
        self.bullet_speed = 1.0
        
        # Create bullet at 0,0 then correct position
        self.rect = pygame.Rect(0,0,self.bullet_width,self.bullet_height)
        self.rect.center = first_play.goku.rect.center
        # Store bullet speed as float value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally across the screen"""
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet on the screen"""
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
