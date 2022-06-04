'''13.3. Капли: найдите изображение дождевой капли и создайте сетку из капель.
Капли должны постепенно опускаться вниз и исчезать у нижнего края экрана.
13.4. Дождь: измените свой код в упражнении 13.3, чтобы при исчезновении ряда
капель у нижнего края экрана новый ряд появлялся у верхнего края и начинал свое
падение.'''

import sys

import pygame

from settings import Settings
from raindrop import RainDrop

class RainyWeather():
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Rainy Weather')
        
        self.raindrops = pygame.sprite.Group()    

        self._create_rain()
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self._update_raindrops()
            self._update_screen()
    
    def _create_rain(self):
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        
        available_space_x = self.settings.screen_width - raindrop_width
        self.number_raindrops_x = available_space_x // (2 * raindrop_width)
        
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height)
    
        for row_number in range(number_rows):
            self._create_row(row_number)
    
    def _create_row(self, row_number):
        for raindrop_number in range(self.number_raindrops_x):
            self._create_raindrop(raindrop_number, row_number)
    
    def _create_raindrop(self, raindrop_number, row_number):
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop.y
        
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        self.raindrops.update()
        
        make_new_drops = False
        for raindrop in self.raindrops.copy():
            if raindrop.check_raindrop():
                self.raindrops.remove(raindrop)
                make_new_drops = True

        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):   
        self.screen.fill(self.settings.bg_color)                 
        self.raindrops.draw(self.screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    rw = RainyWeather()
    rw.run_game()