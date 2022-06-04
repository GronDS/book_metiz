import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    
    def __init__(self, tp_game) :
        '''Create an arrow object at the ship's current position.'''
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.arrow_color
        
        # Create an arrow rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.arrow_width,
        self.settings.arrow_height)
        self.rect.midright = tp_game.ship.rect.midright
        
        # Store the arrow's position as a decimal value.
        self.x = float(self.rect.x)
    
    def update(self):
        '''Move the arrow up the screen.'''
        # Update the decimal position of the arrow.
        self.x += self.settings.arrow_speed
        # Update the rect position.
        self.rect.x = self.x
    
    def draw_arrow(self):
        '''Draw the arrow to the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)