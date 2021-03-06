import sys
from time import sleep

import pygame

from random import randint

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from small_star import SmallStar
from d_button import DifficultyButton

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''
    
    def __init__(self) :
        '''Initialize the game, and create game resources.'''
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.s_stars = pygame.sprite.Group()
        
        self.play_button = Button(self, 'PLAY')
        self.easy_button = DifficultyButton(self, 'EASY', 400)
        self.normal_button = DifficultyButton(self, 'NORMAL', 450)
        self.hard_button = DifficultyButton(self, 'HARD', 500)
        
        self._create_fleet()
        self._create_stars_grid()
        
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
    
    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Create an alien and find the number of aliens in a row.
        #  Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        '''Determine the number of rows of aliens that fit on the screen'''
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        #  Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _create_stars_grid(self):
        '''13.1(and2). Stars: Find an image of a star. Make a grid of stars appear on the screen'''
        # Create a star and find the number of stars in a row.
        #  Spacing between each star is equal to one star width.
        s_star = SmallStar(self)
        s_star_width, s_star_height = s_star.rect.size
        available_space_x = self.settings.screen_width - (2 * s_star_width)
        number_s_stars_x = available_space_x // (2 * s_star_width)
        
        '''Determine the number of rows of stars that fit on the screen'''
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * s_star_height) - ship_height)
        number_rows = available_space_y // (2 * s_star_height)
        #  Create the full sky of stars.
        for row_number in range(number_rows):
            if row_number % 4 == 0:
                for s_star_number in range(number_s_stars_x):
                    self._create_s_star(s_star_number, row_number)
    
    def _create_s_star(self, s_star_number, row_number):
        s_star = SmallStar(self)
        s_star_width, s_star_height = s_star.rect.size
        s_star.x = s_star_width + 10 * s_star_width * s_star_number
        s_star.rect.x = s_star.x + randint(-100, 100)
        s_star.rect.y = s_star.rect.height + 2 * s_star.rect.height * row_number
        self.s_stars.add(s_star)
    
    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_button(mouse_pos)

    
    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks Play.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._play_game()
            
    
    def _check_difficulty_button(self, mouse_pos):
        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        normal_clicked = self.normal_button.rect.collidepoint(mouse_pos)
        hard_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if easy_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings() 
        if normal_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.settings.normal_level()
        if hard_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.settings.hard_level()
    
    def _play_game(self):
            # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_images()
        
        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # elif event.key == pygame.K_ESCAPE:
        #     sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._play_game()
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets.'''
        #  Update bullet positions.
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self._start_new_level()
            
    def _start_new_level(self):
            '''Destroy existing bullets and create new fleet.'''
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            self.stats.level += 1
            self.sb.prep_level()
    
    def _update_aliens(self):
        '''Update the positions of all aliens in the fleet.'''
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
            
    def _check_aliens_bottom(self):
        '''Check if any aliens have reached the bottom of the screen.'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break
            
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            self.aliens.empty()
            self.bullets.empty()
        
            self._create_fleet()
            self.ship.center_ship()
            
             # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            
    def _update_buttons(self):
        self.easy_button.draw_button()
        self.normal_button.draw_button()
        self.hard_button.draw_button()
        
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.s_stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.sb.show_score()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
            self._update_buttons()
        

        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()
                
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()