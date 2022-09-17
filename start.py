import pygame.font

class Start():

    def __init__(self, bg_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_settings = bg_settings

        self.width, self.height = 200,50
        self.text_color = (0,0,0)
        self.fill_color = (245,222,179)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.create_start()

    def create_start(self):
        self.start_image = self.font.render("Play",True,self.text_color,self.fill_color)
        self.start_image_rect = self.start_image.get_rect()
        self.start_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.fill_color, self.rect)
        self.screen.blit(self.start_image, self.start_image_rect)