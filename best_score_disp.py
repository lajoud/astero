import pygame
from constants import *
import sys


def display_best_score(screen, score_list, x_pos, dt):
    white=(255,255,255)
    best_score_text=""

    for element in score_list:
        best_score_text+= f"{element[0]}: {element[1]}; "
    
    font = pygame.font.Font('freesansbold.ttf', 28)
    # create a text surface object,
    # on which text is drawn on it.
    text3 = font.render(best_score_text[:-2], True, white)
    

    # create a rectangular object for the
    # text surface object
    textRect3 = text3.get_rect()
    #set the center of the rectangular object.
    textRect3.centery= SCREEN_HEIGHT // 2
    textRect3.centerx= x_pos
    

    screen.blit(text3, textRect3)

    # move left
    speed = 150  # pixels per second, tweak later
    x_pos -= speed * dt

    return x_pos, textRect3.width

def game_over_screen(screen, score_history, my_clock):
    import pygame, sys

    x_pos = 2 * SCREEN_WIDTH

    while True:
        dt = my_clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("black")

        x_pos, text_width = display_best_score(screen, score_history, x_pos, dt)

        pygame.display.flip()

        # when text completely off the left side, quit
        if x_pos < -text_width:
            pygame.quit()
            sys.exit()