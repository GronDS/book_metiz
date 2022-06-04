'''12.4. Клавиши: создайте файл Pygame, который создает пустой экран. 
В цикле событий выводите значение атрибута event.key при обнаружении события
pygame.KEYDOWN. Запустите программу, нажимайте различные клавиши и понаблюдайте
за реакцией Pygame.'''

import sys

import pygame

class Keys:
    
    def __init__(self) :
        pygame.init()
    
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Keys')

        self.bg_color = (253, 253, 253)
        # self.key = Key(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                            
            self.screen.fill(self.bg_color)
            
            pygame.display.flip()

if __name__ == '__main__':
    k = Keys()
    k.run_game()