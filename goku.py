import pygame
class Goku:
    """a class to manage game character"""
    def __init__(self,first_play):
        """initialize class and its attributes"""
        self.screen = first_play.screen
        self.screen_rect = first_play.screen.get_rect()
        self.goku_speed = 1.5

        # load the image and get rect attribute
        self.image = pygame.image.load("game_pics/black_panther.png")
        self.scaled_image = pygame.transform.smoothscale(self.image,(150,150))
        self.scaled_image.convert()
        self.rect = self.scaled_image.get_rect()

        # positioning
        self.rect.midbottom = self.screen_rect.midbottom

        # give image ability to move by first setting flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # define speed holder for horizontal and vertical movements
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        """draw character at said position"""
        self.screen.blit(self.scaled_image,self.rect)

    def update_me(self):
        if self.moving_right==True and self.rect.right < self.screen_rect.right:
            self.x += self.goku_speed
        if self.moving_left==True and self.rect.left > self.screen_rect.left:
            self.x -= self.goku_speed
        if self.moving_up==True and self.rect.top > self.screen_rect.top:
            self.y -= self.goku_speed
        if self.moving_down==True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.goku_speed
       
        # Finally update rect object with x and y
        self.rect.x = self.x
        self.rect.y = self.y
        
