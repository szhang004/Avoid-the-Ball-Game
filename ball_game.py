"""
features to include: ball reflection angle, difficulty setting, home screen
+ quit screen, score tracker
"""


import sys
import pygame
import pygame.freetype
from pygame.sprite import Group
from settings import Settings 
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from user import User
from balls import Ball
from gems import Gem
from start import Start

def run_game():
    pygame.init()
    bg_settings = Settings()
    screen = pygame.display.set_mode((bg_settings.screen_width, bg_settings.screen_height))
    pygame.display.set_caption("Ball Game")

    stats = GameStats(bg_settings)
    sb = Scoreboard(bg_settings, screen, stats)
    play_button = Start(bg_settings, screen)

    user = User(bg_settings, screen)
    balls = Group()
    gem = Gem(bg_settings, screen, user)

    while True:

        gf.check_events(bg_settings, user, play_button, stats, sb, balls, screen)
        gf.update_screen(bg_settings, screen, sb, user, balls, gem, play_button, stats)

        if bg_settings.game_start:
            gf.update_user(user)
            gf.update_balls(balls, bg_settings, screen, sb, user, stats)
            gf.check_gem_collect(bg_settings, stats, screen, user, gem, balls, sb)
        

        # if check_loss():
            # break 

    # losing screen
    # option to rerun game 
        # run_game()

run_game()