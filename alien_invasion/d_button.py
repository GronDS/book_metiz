import pygame.font

class DifficultyButton():
    
    def __init__(self, ai_game, msg, y_pos):
        '''Initialize button attributes.'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('fonts/Arcade.TTF', 48)###
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = ((self.screen_rect.right - self.width/2), y_pos)
        
         # The button message needs to be prepped only once.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        '''Turn msg into a rendered image and center text on the button.'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
        