"""
Imports
"""
# import sys
# import os
import pygame

"""
Variables
"""
window_width = 960
window_height = 520
background_colour = [0, 0, 0]
fps = 30
#image = pygame.image.load("C:/Users/...")
image_x = 10
image_y = 10
rect_x = 10
rect_y = 20
rect_width = 200
rect_height = 100
rect_colour = [255, 0, 0]

"""
Setup
"""
pygame.init()
main_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Demo Window")
clock = pygame.time.Clock()

"""
Objects and functions
"""


"""
Main game loop
"""
running_window = True
while running_window == True:
    clock.tick(fps)

    # Get keyboard and mouse presses and position
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    # The mouse x and y positions
    print(mouse[0], mouse[1])

    """
    Add any functions or display code after this
    """
    #main_window.blit(image, (image_x, image_y))
    pygame.draw.rect(main_window, (0, 0, 0), (0, 0, window_width, window_height))
    pygame.draw.rect(main_window, rect_colour, (rect_x, rect_y, rect_width, rect_height))

    # Update the screen
    pygame.display.update()

    # Check whether the 'x' is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_x += 5
            elif event.key == pygame.K_LEFT:
                rect_x -= 5
    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_UP:
    #         mario.up = False
    #         mario.down = True
    #     elif event.key == pygame.K_DOWN:
    #         mario.down = True
    #         mario.up = False
