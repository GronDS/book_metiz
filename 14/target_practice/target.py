import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        
        #  Load the alien image and set its rect attribute.
        self.rect = pygame.Rect(0, 0, self.settings.target_width,
        self.settings.target_height)
        self.rect.x = self.settings.screen_width - 2 *  self.rect.width
        self.rect.y = self.rect.height        
        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)
        
    def check_edges(self):
        '''Return True if alien is at edge of screen.'''
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True
      
    def update(self):
        self.y += (self.settings.target_speed *
                   self.settings.target_direction)
        self.rect.y = self.y
    
    def draw_target(self):
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)