import sys
import pygame
from goku import Goku
class GameCharacter:
    """a class to manage game resources and activities"""
    def __init__(self):
        """initialize game and define attributes"""
        pygame.init()

        self.screen = pygame.display.set_mode((1000,600))
        self.bg_color = (100,100,100)
        pygame.display.set_caption("Game Character- Version One: created by @frank olum.")
        self.goku = Goku(self)

    def run_the_game(self):
        """a while loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.goku.blitme()

            pygame.display.flip()

if __name__ == "__main__":
    version_one = GameCharacter()
    version_one.run_the_game()

