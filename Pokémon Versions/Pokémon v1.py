"""
Imports
"""
# import sys
# import os
import pygame

pygame.init()

"""
Objects and functions
"""

def getPos(pos, SpriteSize):
    return (pos[0]*SpriteSize[0], pos[1]*SpriteSize[1])

def damage(sprite):
    sprite['health'] -= 20
    #damage animation.....

"""
Variables
"""
window_width = 968
window_height = 576
background_colour = (0, 0, 0)
fps = 30

#colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
light_grey = (180, 180, 180)
grey = (90, 90, 90)
black = (0, 0, 0)

#text font
font = pygame.font.Font('freesansbold.ttf', 32)

#SPRITE SIZE
SpriteSize = (64, 64)

#GAME screen
game_x = 768
game_y = 576

#GAME grid
grid_x = int(game_x / SpriteSize[0])
grid_y = int(game_y / SpriteSize[1])

#PLAYER SPRITE
player = {
    'colour' : grey,
    'pos'    : (5, 3),
    'rect'   : pygame.Rect(getPos((5,3), SpriteSize), SpriteSize),
    'health' : 100,
    'energy' : 100
}

#ENEMY SPRITE
enemy = {
    'colour' : grey,
    'pos'    : (5, 5),
    'rect'   : pygame.Rect(getPos((5, 5), SpriteSize), SpriteSize),
    'health' : 100,
    'energy' : 100
}


UI_rect = pygame.Rect(768, 0, 200, 576)

buttons = {
    0 : {
        'name'    : font.render('Attack' , True , white),
        'colour'  : grey, 
        'rect'    : pygame.Rect(798, 30,  140, 40)
    },

    1 : {
        'name'    : font.render('Supr Atk' , True , white),
        'colour'  : grey,
        'rect'    : pygame.Rect(798, 100, 140, 40)
    },

    2 : {
        'name'    : font.render('Option 3' , True , white),  
        'colour'  : grey, 
        'rect'    : pygame.Rect(798, 170, 140, 40)
    },

    3 : {
        'name'    : font.render('Option 4' , True , white), 
        'colour'  : grey, 
        'rect'    : pygame.Rect(798, 240, 140, 40)
    }
}


"""
Setup
"""
main_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pokemon ripoff")
clock = pygame.time.Clock()

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
    #print(mouse[0], mouse[1])

    """
    Add any functions or display code after this
    """

    #fill the screen with the colour white
    main_window.fill(white)

    #draw UI frame
    pygame.draw.rect(main_window, light_grey, UI_rect)

    #draw buttons
    for i in range(len(buttons)):
        #blitting the rectangle frames for the text
        if buttons[i]['rect'].collidepoint(mouse):
            pygame.draw.rect(main_window, black, buttons[i]['rect'])
        else:
            pygame.draw.rect(main_window, buttons[i]['colour'], buttons[i]['rect'])
        #blitting the text for the button
        main_window.blit(buttons[i]['name'], buttons[i]['rect'])

    #draw health bars
    pygame.draw.rect(main_window, white, [808, 310, 50, 210])
    pygame.draw.rect(main_window, white, [878, 310, 50, 210])
    pygame.draw.rect(main_window, green, [813, 515 - player['health']*2, 40, player['health']*2])
    pygame.draw.rect(main_window, green, [883, 515 - enemy['health']*2, 40, enemy['health']*2])

    #draw Sprites
    pygame.draw.rect(main_window, player['colour'], player['rect'])
    pygame.draw.rect(main_window, enemy['colour'], enemy['rect'])

    #draw game grid
    for x in range(grid_x + 1):
        pygame.draw.line(main_window, black, (x*SpriteSize[0], 0), (x*SpriteSize[0], game_y))
    for y in range(grid_y + 1):
        pygame.draw.line(main_window, black, (0, y*SpriteSize[1]), (game_x, y*SpriteSize[1]))

    # Update the screen
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(buttons)):
                if buttons[i]['rect'].collidepoint(mouse):
                    if i == 0:
                        damage(enemy)



"""            
        if (0 <= mouse[0] <= game_x and 0 <= mouse[1] < game_y) and (current_pressed > -1):
            square_pos = (mouse[0] - mouse[0] % SpriteSize[0], mouse[1] - mouse[1] % SpriteSize[1])
        else:
            square_pos = (-64, 0)"""


