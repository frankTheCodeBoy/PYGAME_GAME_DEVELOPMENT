import sys
import pygame
from goku import Goku
class GameCharacter:
    """a class to manage game resources and activities"""
    def __init__(self):
        """initialize game and define attributes"""
        pygame.init()

        self.screen = pygame.display.set_mode((1150,700))
        self.bg_color = (100,100,100)
        pygame.display.set_caption("Game Character- Version One: created by @frank olum.")
        self.goku = Goku(self)

    def run_the_game(self):
        """a while loop for the game"""
        while True:
            self._check_the_event()
            self.goku.update_me()
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
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.goku.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.goku.moving_left = False
                elif event.key == pygame.K_UP:
                    self.goku.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.goku.moving_down = False
               
    def _update_the_screen(self):
        """fill screen color, blit new image at point"""
        self.screen.fill(self.bg_color)
        self.goku.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    version_one = GameCharacter()
    version_one.run_the_game()

