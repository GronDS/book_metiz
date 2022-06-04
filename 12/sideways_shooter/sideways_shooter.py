'''12.6. Боковая стрельба: напишите игру, в которой корабль размещается у 
левого края экрана, а игрок может перемещать корабль вверх и вниз. При нажатии
клавиши «пробел» корабль стреляет и снаряд двигается вправо по экрану.
Проследите за тем, чтобы снаряды удалялись при выходе за край экрана.'''
import sys
from time import sleep

import pygame

from random import randint

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from small_star import SmallStar
from alien import Alien

class SidewaysShooter:
    '''Overall class to manage game assets and behavior.'''
    
    def __init__(self) :
        '''Initialize the game, and create game resources.'''
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')
        
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.s_stars = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_stars_grid()
        self._create_fleet()
    
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            

    
    def _create_stars_grid(self):
        s_star = SmallStar(self)
        s_star_width, s_star_height = s_star.rect.size
        available_space_x = self.settings.screen_width
        number_s_stars_x = available_space_x // (2 * s_star_width)
        
        '''Determine the number of rows of stars that fit on the screen'''
        available_space_y = self.settings.screen_height
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
        s_star.rect.y = s_star.rect.height + 2 * s_star.rect.height * row_number + randint(-100,100)
        self.s_stars.add(s_star)            
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height =  alien.rect.height
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)
        
        ship_width = self.ship.rect.width
        available_space_x = (self.settings.screen_width -
                             (3 *alien_width) - ship_width)
        number_rows = available_space_x //(2 * alien_width) - 1
        for row_number in range(number_rows):
           for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width = alien.rect.width
            alien_height = alien.rect.height
            alien.y = alien_height + 2 * alien_height * alien_number
            alien.rect.y = alien.y
            alien.rect.x = alien.rect.x - 4 * alien.rect.height * row_number
            self.aliens.add(alien)
            
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        '''Respond to keypresses and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

        
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        # elif event.key == pygame.K_ESCAPE:
        #     sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

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
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_left()
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            
            print(self.stats.aliens_pwned)###
            sleep(0.75)
        else:
            self.stats.game_active = False
    
    def _check_aliens_left(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                self._ship_hit()
                break
    
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.s_stars.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()
                
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()