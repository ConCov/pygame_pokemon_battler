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

button1_x = 600
button1_y = 200
button1_width = 200
button1_height = 100
button1_colour = [255, 0, 0]

button2_x = 100
button2_y = 200
button2_width = 200
button2_height = 100
button2_colour = [0, 255, 0]

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
def checkInsideButton(button_x, button_y, button_width, button_height):
    mouse = pygame.mouse.get_pos()

    # Check the x-position of the mouse
    if mouse[0] >= button_x and mouse[0] <= button_x + button_width:
        # Check the y-position of the mouse
        if mouse[1] >= button_y and mouse[1] <= button_y + button_height:
            return True
        else:
            return False
    else:
        return False

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
    # print(mouse[0], mouse[1])

    # Fills the background with a certain colour
    main_window.fill(background_colour)

    # Draw a rectangle
    pygame.draw.rect(main_window, button1_colour, (button1_x, button1_y, button1_width, button1_height))
    pygame.draw.rect(main_window, button2_colour, (button2_x, button2_y, button2_width, button2_height))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
        # Add your mouse or key events after this
        elif event.type == pygame.MOUSEBUTTONUP:
            if checkInsideButton(button1_x, button1_y, button1_width, button1_height) == True:
                print("Clicked the red button")
            elif checkInsideButton(button2_x, button2_y, button2_width, button2_height) == True:
                print("Clicked the green button")
            else:
                print("Mouse clicked")
