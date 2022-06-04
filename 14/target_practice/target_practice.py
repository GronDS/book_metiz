'''14.2. Стрельба по мишени: создайте у правого края экрана прямоугольник, 
который двигается вверх и вниз с постоянной скоростью. У левого края 
располагается корабль, который перемещается вверх и вниз игроком и стреляет по
движущейся прямоугольной мишени. Добавьте кнопку Play для запуска игры. После 
трех промахов игра заканчивается, а на экране снова появляется кнопка Play.
Нажатие этой кнопки перезапускает игру.'''
import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from arrow import Arrow
from target import Target
from button import Button 
from game_stats import GameStats

class TargetPractice:

    def __init__(self) :
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                            self.settings.screen_height))
        pygame.display.set_caption('Target Practice')
        
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.targets = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()

        self.play_button = Button(self, 'PLAY')
        self._create_target()
    def run_game(self):
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_arrows()
                self.targets.update()
                self._check_target()
            
            self._update_screen()
    
    def _create_target(self):
        target = Target(self)
        self.targets.add(target)
    
    def _check_target(self):
        for target in self.targets.sprites():
            if target.check_edges():
                self._change_move_direction()
                break
    
    def _change_move_direction(self):
        for targets in self.targets.sprites():
            self.settings.target_direction *= -1 
    
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
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        # elif event.key == pygame.K_ESCAPE:
        #     sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_arrows()
        elif event.key == pygame.K_p:
            self._play_game()
            
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False
            
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings._reset_difficulty()
            self._play_game()
            
    def _play_game(self):
        if self.stats.game_active == False:
            self.stats.reset_stats()
            self.stats.game_active = True
        
            self.targets.empty()
            self.arrows.empty()
            
            self._create_target()
            self.ship.center_ship()
            
            pygame.mouse.set_visible(False)
    
    def _fire_arrows(self):
        if len(self.arrows) < self.settings.arrow_allowed:
            new_arrow = Arrow(self)
            self.arrows.add(new_arrow)
    
    def _check_arrow_target_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.arrows, self.targets, True, True)
        if not self.targets:
            self.targets.empty()
            self.arrows.empty()
            
            self._create_target()
            self.ship.center_ship()
            
            self.settings._increase_difficulty()

            sleep(1)
    def _game_over(self):
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
                
    def _update_arrows(self):
        self.arrows.update()
        for arrow in self.arrows.copy():
            if arrow.rect.left >= self.settings.screen_width:
                self.arrows.remove(arrow)
                self.stats.miss_left -= 1
                if self.stats.miss_left < 0:
                    self._game_over()
        
        self._check_arrow_target_collisions()
    
 
        
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        if not self.stats.game_active:
            self.play_button.draw_button()

        for arrow in self.arrows.sprites():
            arrow.draw_arrow()
        for target in self.targets.sprites():
            target.draw_target()
            

            
        pygame.display.flip()
        
if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()