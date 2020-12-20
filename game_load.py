import sys
import pygame
from goku import Goku
from game_bullets import Bullet
from aliens import Alien

class GameCharacter:
    """a class to manage game resources and activities"""
    def __init__(self):
        """initialize game and define attributes"""
        pygame.init()
        # Screen settings and display
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width 
        self.screen_height = self.screen.get_rect().height
        self.bg_color = (100,0,0)
        pygame.display.set_caption("Game Character- Version One: created by @frank olum.")
        # reference to goku character
        self.goku = Goku(self)
        self.bullets = pygame.sprite.Group()
        # bullets allowed setting
        self.bullets_allowed = 3

        self.aliens = pygame.sprite.Group()
        self._new_fleet()


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
                self._check_keypresses(event)
            elif event.type == pygame.KEYUP:
                self._check_keyrelease(event)

    def _check_keypresses(self,event):
        if event.key == pygame.K_RIGHT:
            self.goku.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.goku.moving_left = True
        elif event.key == pygame.K_UP:
            self.goku.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.goku.moving_down = True
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyrelease(self,event):
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
        for bullet in self.bullets.copy():
            if bullet.rect.x < 0:
                self.bullets.remove(bullet)

    def _new_fleet(self):
        """Create alien fleet"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_height = alien.rect.height
        available_space_y = self.screen_height - (2 * alien_height)
        number_aliens_y = (available_space_y // (2 * alien_height)) + 1
        # Create first row of fleet
        for alien_number in range(number_aliens_y):
            self._create_alien(alien_number)

    def _create_alien(self,alien_number):
        # Create an alien and place it in row
        alien = Alien(self)
        alien_height = alien.rect.height
        alien.y = alien_height + (2 * alien_height * alien_number)
        alien.rect.y = alien.y
        self.aliens.add(alien)


    def _update_the_screen(self):
        """fill screen color, blit new image at point"""
        self.screen.fill(self.bg_color)
        self.goku.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    version_one = GameCharacter()
    version_one.run_the_game()

