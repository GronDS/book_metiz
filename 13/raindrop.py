import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    '''A class to represent a single raindrop.'''
    
    def __init__(self, rw_game):
        super().__init__()
        self.screen = rw_game.screen
        self.settings = rw_game.settings
                
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)
        
    def check_raindrop(self):
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False
        
      
    def update(self):
        '''Move the raindrop down.'''
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y