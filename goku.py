import pygame
class Goku:
    """a class to manage game character"""
    def __init__(self,first_play):
        """initialize class and its attributes"""
        self.screen = first_play.screen
        self.screen_rect = first_play.screen.get_rect()

        # load the image and get rect attribute
        self.image = pygame.image.load("game_pics/black_panther.bmp")
        self.scaled_image = pygame.transform.smoothscale(self.image,(200,200))
        self.scaled_image.convert()
        self.rect = self.scaled_image.get_rect()

        # positioning
        self.rect.center = self.screen_rect.center

        # give image ability to move by first setting flag
        self.moving_right = False
        self.moving_left = False 

    def blitme(self):
        """draw character at said position"""
        self.screen.blit(self.scaled_image,self.rect)

    def update_me(self):
        if self.moving_right==True:
            self.rect.x += 1
        if self.moving_left==True:
            self.rect.x -= 1
