import sys
import pygame

from balls import Ball
from user import User
from gems import Gem

def check_events(bg_settings, user, play_button, stats, sb, balls, screen):
    # Watching events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, user)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,user)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y) and not bg_settings.game_start:
                game_reset(bg_settings, stats, sb, user, balls, screen)
                bg_settings.game_start = True
            

def update_screen(bg_settings, screen, sb, user, balls, gem, play_button, stats):
    screen.fill(bg_settings.bg_color)
    user.blitme()
    sb.show_score()
  
    balls.draw(screen)
    gem.blitme()

    if not bg_settings.game_start:
        play_button.draw_button()

    pygame.display.flip()

def check_keydown_events(event, user):
    if event.key == pygame.K_RIGHT:
        user.moving_right = True
    elif event.key == pygame.K_LEFT:
        user.moving_left = True
    if event.key == pygame.K_DOWN:
        user.moving_down = True
    elif event.key == pygame.K_UP:
        user.moving_up = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, user):
    if event.key == pygame.K_RIGHT:
        user.moving_right = False
    elif event.key == pygame.K_LEFT:
        user.moving_left = False
    if event.key == pygame.K_DOWN:
        user.moving_down = False
    elif event.key == pygame.K_UP:
        user.moving_up = False

def update_user(user):
    user.update()

def set_balls(balls, bg_settings, screen, user):
    for ball_number in range(bg_settings.num_balls):
        new_ball = Ball(bg_settings, screen, user)
        balls.add(new_ball)


def update_balls(balls, bg_settings, screen, sb, user, stats):
    balls.update()

    for ball in balls.copy():
        check_edges(bg_settings, screen, ball)

    ball_collision(bg_settings, stats, sb, user, balls, screen)

def check_edges(bg_settings, screen, ball):
    screen_rect = ball.screen.get_rect()
    if ball.rect.right >= screen_rect.right-10:
        ball.directionx *= -1
    elif ball.rect.left <= 10:
        ball.directionx *= -1
    if ball.rect.bottom >= screen_rect.bottom-10:
        ball.directiony *= -1
    elif ball.rect.top <= 10:
        ball.directiony *= -1

def check_gem_collect(bg_settings, stats, screen, user, gem, balls, sb):
    if pygame.Rect.colliderect(user.rect, gem.rect):
        gem.reset_gem()
        stats.score += 1
        check_level(bg_settings, stats, screen, user, balls)
        sb.create_score()

def check_level(bg_settings, stats, screen, user, balls):
    if stats.score % 10 == 0:
        level_up(bg_settings, screen, stats, user, balls)

def level_up(bg_settings, screen, stats, user, balls):
    stats.level += 1
    for i in range(2):
        new_ball = Ball(bg_settings, screen, user)
        balls.add(new_ball)
    for ball in balls.copy():
        ball.velocityx *= bg_settings.ball_speed_increase
        ball.velocityy *= bg_settings.ball_speed_increase
        
def ball_collision(bg_settings, stats, sb, user, balls, screen):
    if pygame.sprite.spritecollideany(user, balls):
        game_reset(bg_settings, stats, sb, user, balls, screen)

def game_reset(bg_settings, stats, sb, user, balls, screen):
    bg_settings.game_start = False
    stats.score = 0
    stats.level = 1
    sb.create_score()
    balls.empty()
    user.rect.centerx = user.screen_rect.centerx
    user.rect.bottom = user.screen_rect.bottom
    set_balls(balls, bg_settings, screen, user)