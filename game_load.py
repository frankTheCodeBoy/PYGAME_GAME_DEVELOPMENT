import sys
import pygame
from goku import Goku
from game_bullets import Bullet

class GameCharacter:
    """a class to manage game resources and activities"""
    def __init__(self):
        """initialize game and define attributes"""
        pygame.init()
        
        self.screen_width = 700
        self.screen_height = 1150
        self.screen = pygame.display.set_mode((self.screen_height,self.screen_width))
        self.bg_color = (100,100,100)
        pygame.display.set_caption("Game Character- Version One: created by @frank olum.")
        self.goku = Goku(self)
        self.bullets = pygame.sprite.Group()

    def run_the_game(self):
        """a while loop for the game"""
        while True:
            self._check_the_event()
            self.goku.update_me()
            self._update_bullets()
            self._update_the_screen()

    def _check_the_event(self):
        """watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.goku.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.goku.moving_left = True
                elif event.key == pygame.K_UP:
                    self.goku.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.goku.moving_down = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.goku.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.goku.moving_left = False
                elif event.key  == pygame.K_UP:
                    self.goku.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.goku.moving_down = False

    def _update_bullets(self):
        """Update positions of bullets and rid old bullets"""
        self.bullets.update()
               
    def _update_the_screen(self):
        """fill screen color, blit new image at point"""
        self.screen.fill(self.bg_color)
        self.goku.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == "__main__":
    version_one = GameCharacter()
    version_one.run_the_game()

