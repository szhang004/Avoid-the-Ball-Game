import pygame.font

class Scoreboard():

    def __init__(self, bg_settings, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.bg_settings = bg_settings
        self.stats = stats

        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.create_score()

    def create_score(self):
        score_str = "Score:" + str(self.stats.score) + "\nLevel:" + str(self.stats.level)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_settings.bg_color)

    # position it at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
