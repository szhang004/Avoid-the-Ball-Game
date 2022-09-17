import pygame

class User():

    def __init__(self, bg_settings, screen):
        self.screen = screen
        self.bg_settings = bg_settings

        self.image = pygame.image.load('images/user.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.bg_settings.user_speed
        elif self.moving_left == True and self.rect.left > 0:
            self.rect.centerx -= self.bg_settings.user_speed
        if self.moving_up == True and self.rect.top > 0:
            self.rect.centery -= self.bg_settings.user_speed
        elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.bg_settings.user_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)