'''12.4. Ракета: создайте игру, в которой в исходном состоянии в центре экрана
находится ракета. Игрок может перемещать ракету вверх, вниз, вправо и влево
четырьмя клавишами со стрелками. Проследите за тем, чтобы ракета не выходила за
края экрана.'''
import sys

import pygame

from rocket import Rocket

class RocketGame():
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Rocket Game')
        
        self.bg_color = (0, 0, 255)
        
        self.rocket = Rocket(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
                           
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _update_screen(self):
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            pygame.display.flip()        
        
if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()