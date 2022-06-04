'''12.2. Игровой персонаж: найдите изображение игрового персонажа, который вам 
нравится, в формате .bmp (или преобразуйте существующее изображение).
Создайте класс, который рисует персонажа в центре экрана, и приведите цвет
фона изображения в соответствие с цветом фона экрана (или наоборот).'''

import pygame

class GameChar():
    
    def __init__(self, bs_game) :
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()
        
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)