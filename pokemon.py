import time, random
import pygame, math
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
main_window = pygame.display.set_mode((960,500))

color = {}
color['brown'] = (148,109,32)
color['red'] = (210,30,7)
color['grey'] = (213,209,198)
color['white'] = (255, 255, 255)
color['black'] = (0,0,0)
color['green'] = (30,210,7)
font = pygame.font.SysFont("Arial", 48)
running_window = True
x,y=250,250
click = False
mode = "default"
fight_click = False
switch_click = False
option1_click = False
option2_click = False

health1 = 10
health2 = 10

# Start the game
while running_window:
    # Check for user clicks
    for event in pygame.event.get():
        if event.type == QUIT:
            running_window = False
        if event.type == MOUSEBUTTONDOWN:
            click = True
            x,y = event.pos

    # Draw arena
    pygame.draw.rect(main_window, color['brown'], (0,0,400,500))
    pygame.draw.ellipse(main_window, color['black'], (150,200,100,100))
    pygame.draw.ellipse(main_window, color['red'], (155,205,90,90))
    pygame.draw.arc(main_window, color['grey'], (155,205,90,90), 0, math.pi,40)
    pygame.draw.line(main_window, color['black'], (155,248),(245,248), 6)
    pygame.draw.ellipse(main_window, color['black'], (200-12,250-12,24,24))
    pygame.draw.ellipse(main_window, color['grey'], (200-7,250-7,14,14))
    # Draw menu area
    pygame.draw.rect(main_window, color['grey'], (400,0,560,500), )
    # Draw buttons
    button1 = Rect(580,115,250,100)
    button2 = Rect(580,285,250,100)
    if fight_click == False and switch_click == False:
        pygame.draw.rect(main_window, color['red'], button1)
        pygame.draw.rect(main_window, color['green'], button2)
        text1_render = font.render("FIGHT", 1, color['white'])
        text2_render = font.render("SWITCH", 1, color['white'])
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

    if fight_click == True:
        pygame.draw.rect(main_window, color['red'], button1)
        pygame.draw.rect(main_window, color['white'], button2)
        text1_render = font.render("EMBER", 1, color['white'])
        text2_render = font.render("SCRATCH", 1, color['black'])
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

        if option1_click == True:
            print("Attacked with option 1!")
            hit_points = random.randint(-1, 1)
            health2 -= hit_points
            fight_click = False
            option1_click = False

        if option2_click == True:
            print("Attacked with option 2!")
            hit_points = random.randint(-1, 1)
            health2 -= hit_points
            fight_click = False
            option2_click = False

    if switch_click == True:
        pygame.draw.rect(main_window, color['black'], button1)
        pygame.draw.rect(main_window, color['white'], button2)
        text1_render = font.render("Squirtle", 1, (255,255,255))
        text2_render = font.render("Bulbasaur", 1, (255,255,255))
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

        if option3_click == True:
            print("Switched Pokemon!")
            fight_click = False
            option3_click = False

        if option4_click == True:
            print("Switched Pokemon")
            fight_click = False
            option4_click = False


    # Draw player 1
    # TO DO

    # Draw player 2
    # TO DO

    # Do action
    if click:

        if button1.collidepoint((x,y)) and option1_click == False and option2_click == False and fight_click == True:
            option1_click = True
            print("clicked option 1")
        elif button2.collidepoint((x,y)) and option2_click == False and option1_click == False and fight_click == True:
            option2_click = True
            print("clicked option 2")
        # elif button1.collidepoint((x,y)) and option3_click == False and option4_click == False and fight_click == True:
        #     option1_click = True
        #     print("clicked option 3")
        # elif button2.collidepoint((x,y)) and option3_click == False and option4_click == False and fight_click == True:
        #     option2_click = True
        #     print("clicked option 4")

        if button1.collidepoint((x,y)) and fight_click == False and switch_click == False:
            fight_click = True
            print("clicked fight")
        elif button2.collidepoint((x,y)) and switch_click == False and fight_click == False:
            switch_click = True
            print("clicked switch")

        # Add stuff to detect other button clicks


        click = False # Reset the click
    pygame.display.update()
    clock.tick(40)
pygame.quit()