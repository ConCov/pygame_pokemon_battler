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
background_colour = (0, 0, 0)
fps = 30

rect_x = 10
rect_y = 20
rect_width = 200
rect_height = 100
rect_colour = (255, 0, 0)
rect_speed = 5

"""
Setup
"""
pygame.init()
main_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simple Window")
clock = pygame.time.Clock()

"""
Objects and functions
"""


"""
Main game loop
"""
running_window = True
while running_window == True:
    # Limits the number of frames per second
    clock.tick(fps)

    # Fills the background with a certain colour
    main_window.fill(background_colour)

    """
    Add any display code after this
    """
    # Draw a simple rectangle on the screen
    pygame.draw.rect(main_window, (rect_colour), (rect_x, rect_y, rect_width, rect_height))

    """
    Add any event code after this
    """
    # In all the events that happen
    for event in pygame.event.get():
        # Check if the user pressed a key DOWN
        if event.type == pygame.KEYDOWN:    # Can also have pygame.KEYUP
            # If the user pressed the right arrow key
            if event.key == pygame.K_RIGHT: # The key format is K_D or K_9 or K_UP
                rect_x = rect_x + rect_speed
            # If the user pressed the left arrow key
            elif event.key == pygame.K_LEFT:
                rect_x = rect_x - rect_speed

    """
    Add any code before this
    """

    # Update the screen
    pygame.display.update()

    # Check whether the 'x' is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
