import pygame
from pygame.sprite import Sprite 
import random

class Ball(Sprite):

    def __init__(self, bg_settings, screen, user):
        super(Ball,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.directionx = random.choice([-1,1])
        self.directiony = random.choice([-1,1])
        self.velocityx = random.randint(round(bg_settings.ball_speed/2), bg_settings.ball_speed)
        self.velocityy = random.randint(round(bg_settings.ball_speed/2), bg_settings.ball_speed)
        
        self.rect.centerx = random.randint(40,bg_settings.screen_width-40)
        self.rect.centery = random.randint(40,bg_settings.screen_height-40)

        while (self.rect.centerx in range(user.rect.left - 30, user.rect.right + 30) and 
        self.rect.centery in range(0, user.rect.top + 30)):
            self.rect.centerx = random.randint(40,bg_settings.screen_width-40)
            self.rect.centery = random.randint(40,bg_settings.screen_height-40)

        self.speed = bg_settings.ball_speed
        self.color = bg_settings.ball_color
        self.radius = bg_settings.ball_radius

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if not (self.rect.right >= self.screen_rect.right or self.rect.left <= 0):
            self.rect.centerx += self.directionx * self.velocityx
        if not (self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom):
            self.rect.centery += self.directiony * self.velocityy