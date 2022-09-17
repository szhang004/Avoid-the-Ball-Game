import pygame
import random

class Gem():

    def __init__(self, bg_settings, screen, user):
        self.screen = screen
        self.bg_settings = bg_settings
        self.image = pygame.image.load('images/gem.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = random.randint(0,bg_settings.screen_width)
        self.rect.centery = random.randint(0,bg_settings.screen_height-20)
        
        while (self.rect.centerx in range(user.rect.left - 30, user.rect.right + 30) and 
        self.rect.centery in range(0, user.rect.top + 30)):
            self.rect.centerx = random.randint(0,bg_settings.screen_width)
            self.rect.centery = random.randint(0,bg_settings.screen_height)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset_gem(self):
        old_x = self.rect.centerx
        old_y = self.rect.centery
        
        while self.rect.centerx == old_x and self.rect.centery == old_y:
            self.rect.centerx = random.randint(0,self.bg_settings.screen_width)
            self.rect.centery = random.randint(0,self.bg_settings.screen_height-20)


    