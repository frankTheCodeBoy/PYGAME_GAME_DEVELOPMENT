import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from goku import Goku
from game_bullets import Bullet
from aliens import Alien

class GameCharacter:
    """a class to manage game resources and activities"""
    def __init__(self):
        """initialize game and define attributes"""
        pygame.init()
        # Screen settings and display
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Game Character- Version One: created by @frank olum.")
        # reference to goku character
        self.goku = Goku(self)
        # Create an instance to store game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._new_fleet()
        # Make a Play button.
        self.play_button = Button(self, "PLAY")

        # Set up the sound and music.
        pygame.mixer.init()
        bulletSound = pygame.mixer.Sound('game_pics/Sonar-sound.mp3')
        raw_array = bulletSound.get_raw()
        raw_array = raw_array[100000:120000]
        self.putBulletSound = pygame.mixer.Sound(buffer=raw_array)
        self.crashSound = pygame.mixer.Sound('game_pics/crash-tone.mp3')
        pygame.mixer.music.load('game_pics/Scorch_Trials.mp3')
        # Set a music playing flag
        self.music_playing = False

    def run_the_game(self):
        """a while loop for the game"""
        while True:
            self._check_the_event()
            
            if self.stats.game_active:
                self.goku.update_me()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            # Reset game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the game character
            self._new_fleet()
            self.goku.restore_goku()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
            # Set music flag to true, let music play
            self.music_playing = True
            pygame.mixer.music.play(-1, 0.0)

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
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
        elif event.key == pygame.K_q:
            # Write high score into a file, exit system.
            import json
            with open("high_scores.json",'w') as f:
                json.dump(self.stats.high_score, f)
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
        elif event.key == pygame.K_m:
            if self.music_playing:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1, 0.0)
            self.music_playing = not self.music_playing

    def _update_bullets(self):
        """Update positions of bullets and rid old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.x < 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Check for any bullets that have hit aliens.
        If so, get rid of the bullet and the alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.putBulletSound.play()
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            """Destroy existing bullets and create new fleet"""
            self.bullets.empty()
            self._new_fleet()
            self.settings.increase_speed()
            # Increae level.
            self.stats.level += 1
            self.sb.prep_level()

    def _new_fleet(self):
        """Create alien fleet"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = (available_space_y // (2 * alien_height)) + 1
        # Determine alien columns to fit on screen
        goku_width = self.goku.rect.width
        available_space_x = (self.settings.screen_width
         - (3 * alien_width) - goku_width)

        number_columns = (available_space_x // (2 * alien_width)) + 1
        # Create full fleet of aliens
        for column_number in range(number_columns):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number,column_number)

    def _create_alien(self,alien_number,column_number):
        # Create an alien and place it in row
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        alien.y = alien_height + (2 * alien_height * alien_number)
        alien.rect.x = alien.rect.width + 2 * alien.rect.width * column_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move fleet across screen and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.fleet_cruise_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        """Check if fleet is at edge 
        update positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for collisions of alien and goku"""
        if pygame.sprite.spritecollideany(self.goku,self.aliens):
            self.crashSound.play()
            self._goku_hit()
        # Look for aliens reaching right side of screen.
        self._check_aliens_right()

    def _goku_hit(self):
        """Respond to goku being hit"""
        if self.stats.goku_left > 0:
            self.stats.goku_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet and restore goku
            self._new_fleet()
            self.goku.restore_goku()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.music_playing = False
            pygame.mixer.music.stop()

    def _check_aliens_right(self):
        """Check whether any aliens have reached the right side of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.right >= screen_rect.right:
                self.crashSound.play()
                self._goku_hit()
                break

    def _update_the_screen(self):
        """fill screen color, blit new image at point"""
        self.screen.fill(self.settings.bg_color)
        self.goku.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()

        # Draw play button if game is inactive state.
        if self.stats.game_active == False:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == "__main__":
    version_one = GameCharacter()
    version_one.run_the_game()

  