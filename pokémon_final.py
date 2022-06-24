# Imports
import time, random
import pygame, math
from pygame.locals import *
import csv

# Initialisation
window_width = 960
window_height = 500

pygame.init()
clock = pygame.time.Clock()
main_window = pygame.display.set_mode((window_width,window_height))

# Variables
color = {
    'brown' : (148,109,32),
    'red' : (210,30,7),
    'grey' : (213,209,198),
    'white' : (255, 255, 255),
    'black' : (0,0,0),
    'green' : (30,210,7)
}
font = pygame.font.SysFont("Arial", 48)
click = False
x,y = 0,0

health1 = 10
health2 = 10
lost = 0

# Button click checks
fight_click = False
switch_click = False
option1_click = False
option2_click = False
option3_click = False
option4_click = False

# Load Pokémon information from file
with open("pokemon/pokemons.csv", "r", encoding="utf-8") as f:
    pokemons = list(csv.DictReader(f, delimiter=","))

# Set starting characters for each player
turn = 1            # Which player's turn is it?
player1 = 0         # Which pokemon is player 1?
player2 = 1         # Which pokemon is player 2?

# Load the images and sound effects
player1_sprite = pygame.image.load("pokemon/"+pokemons[player1]["image"])
player2_sprite = pygame.image.load("pokemon/"+pokemons[player2]["image"])
player1_sprite = pygame.transform.scale(player1_sprite, (192,192))
player2_sprite = pygame.transform.scale(player2_sprite, (192,192))
player1_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player1]["sfx"])
player2_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player2]["sfx"])

# Main game screen
running_window = True
while running_window:
    # Check for user clicks
    for event in pygame.event.get():
        if event.type == QUIT:
            running_window = False
        if event.type == MOUSEBUTTONDOWN:
            click = True
            x,y = event.pos

    # Draw arena
    pygame.draw.rect(main_window, color['brown'], (0,0,400,window_height))
    pygame.draw.ellipse(main_window, color['black'], (150,200,100,100))
    pygame.draw.ellipse(main_window, color['red'], (155,205,90,90))
    pygame.draw.arc(main_window, color['grey'], (155,205,90,90), 0, math.pi,40)
    pygame.draw.line(main_window, color['black'], (155,248),(245,248), 6)
    pygame.draw.ellipse(main_window, color['black'], (200-12,250-12,24,24))
    pygame.draw.ellipse(main_window, color['grey'], (200-7,250-7,14,14))

    # Draw button menu area
    pygame.draw.rect(main_window, color['grey'], (400,0,560,window_height))
    player_turn_text = font.render(f"PLAYER {turn} TURN", 1, color['black'])
    main_window.blit(player_turn_text, (410, 10))

    # Save the buttons to use later
    button1 = Rect(580,115,250,100)
    button2 = Rect(580,285,250,100)

    # Check for button clicks
    if fight_click == False and switch_click == False:
        # Draw the fight and switch text and buttons
        pygame.draw.rect(main_window, color['red'], button1)
        pygame.draw.rect(main_window, color['green'], button2)
        text1_render = font.render("FIGHT", 1, color['white'])
        text2_render = font.render("SWITCH", 1, color['white'])
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

    # Check if the fight button is clicked
    if fight_click == True:
        # Draw the new text and buttons
        pygame.draw.rect(main_window, color['red'], button1)
        pygame.draw.rect(main_window, color['white'], button2)
        text1_render = font.render("EMBER", 1, color['white'])
        text2_render = font.render("SCRATCH", 1, color['black'])
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

        # Check if the attack option 1 is clicked
        if option1_click == True:
            # Remove hit points
            hit_points = 3 + random.randint(-1, 1)
            if turn != 1:
                health1 -= hit_points
            else:
                health2 -= hit_points

            # Reset the screen
            fight_click = False
            option1_click = False
            time.sleep(0.25)

        # Check if the attack option 2 is clicked
        if option2_click == True:
            # Remove hit points
            hit_points = 3 + random.randint(-1, 1)
            if turn != 1:
                health1 -= hit_points
            else:
                health2 -= hit_points

            # Reset the screen
            fight_click = False
            option2_click = False
            time.sleep(0.25)

    # Check if the switch button is clicked
    if switch_click == True:
        # Draw the new text and buttons
        pygame.draw.rect(main_window, color['black'], button1)
        pygame.draw.rect(main_window, color['white'], button2)
        text1_render = font.render("Squirtle", 1, color['white'])
        text2_render = font.render("Bulbasaur", 1, color['black'])
        main_window.blit(text1_render, (600, 130))
        main_window.blit(text2_render, (600, 300))

        # Check if the switch option 1 is clicked and reset the screen
        if option3_click == True:
            switch_click = False
            option3_click = False
            time.sleep(0.25)

        # Check if the switch option 2 is clicked and reset the screen
        if option4_click == True:
            switch_click = False
            option4_click = False
            time.sleep(0.25)

    # Save some variables for drawing the health bars
    p1_width = player1_sprite.get_width()
    p1_height = player1_sprite.get_height()

    p2_width = player2_sprite.get_width()
    p2_height = player2_sprite.get_height()

    # Draw player 1
    main_window.blit(player1_sprite, (200 - p1_width // 2, 100 - p1_width // 2))

    # Draw player 1 health bar
    pygame.draw.rect(main_window, color['white'], (200 + p1_width // 2 - 40, 60, 20, 104))
    pygame.draw.rect(main_window, color['green'], (200 + p1_width // 2 - 38, 62 + 10 * (10 - health1), 16, 10 * health1))

    # Draw player 2
    main_window.blit(player2_sprite, (200 - p2_width // 2, 400 - p2_height // 2))

    # Draw player 2 health bar
    pygame.draw.rect(main_window, color['white'], (200 + p2_width // 2 - 40, 360, 20, 104))
    pygame.draw.rect(main_window, color['green'], (200 + p2_width // 2 - 38, 362 + 10 * (10 - health2), 16, 10 * health2))

    # If the user clicked the screen
    if click:
        # If the user clicked on the attack option 1 button
        if button1.collidepoint((x,y)) and option1_click == False and option2_click == False and fight_click == True:
            option1_click = True

            # Switch player turn
            if turn == 1:
                player1_sfx.play()
                turn = 2
            else:
                player2_sfx.play()
                turn = 1
        # If the user clicked on the attack option 2 button
        elif button2.collidepoint((x,y)) and option2_click == False and option1_click == False and fight_click == True:
            option2_click = True

            # Switch player turn
            if turn == 1:
                player1_sfx.play()
                turn = 2
            else:
                player2_sfx.play()
                turn = 1
        # If the user clicked on the switch option 1 button
        elif button1.collidepoint((x,y)) and option3_click == False and option4_click == False and switch_click == True:
            option3_click = True

            # Randomly pick new Pokemon for whoever's turn it is
            if turn == 1:
                player1 = random.randint(0, len(pokemons)-1)
            else:
                player2 = random.randint(0, len(pokemons)-1)

            # Reload the sprites and sounds
            player1_sprite = pygame.image.load("pokemon/"+pokemons[player1]["image"])
            player2_sprite = pygame.image.load("pokemon/"+pokemons[player2]["image"])
            player1_sprite = pygame.transform.scale(player1_sprite, (192,192))
            player2_sprite = pygame.transform.scale(player2_sprite, (192,192))
            player1_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player1]["sfx"])
            player2_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player2]["sfx"])
        # If the user clicked on the switch option
        elif button2.collidepoint((x,y)) and option3_click == False and option4_click == False and switch_click == True:
            option4_click = True

            # Randomly pick new Pokemon for whoever's turn it is
            if turn == 1:
                player1 = random.randint(0, len(pokemons)-1)
                turn = 2
            else:
                player2 = random.randint(0, len(pokemons)-1)
                turn = 1

            # Reload the sprites and sounds
            player1_sprite = pygame.image.load("pokemon/"+pokemons[player1]["image"])
            player2_sprite = pygame.image.load("pokemon/"+pokemons[player2]["image"])
            player1_sprite = pygame.transform.scale(player1_sprite, (192,192))
            player2_sprite = pygame.transform.scale(player2_sprite, (192,192))
            player1_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player1]["sfx"])
            player2_sfx = pygame.mixer.Sound("pokemon/"+pokemons[player2]["sfx"])

        # If the user clicked on the fight button
        if button1.collidepoint((x,y)) and fight_click == False and switch_click == False:
            fight_click = True
        # If the user clicked on the switch button
        elif button2.collidepoint((x,y)) and switch_click == False and fight_click == False:
            switch_click = True

        # Reset the click
        click = False

    # Check whether the health of one of the Pokemon is 0
    if health1 <= 0:
        running_window = False
        lost = 2
    elif health2 <= 0:
        running_window = False
        lost = 1

    # Update the screen
    pygame.display.update()
    clock.tick(30)

# Game over screen
running_window = True
while running_window and lost != 0:
    # Check for user clicks
    for event in pygame.event.get():
        if event.type == QUIT:
            running_window = False

    # Draw the text for which player lost
    pygame.draw.rect(main_window, color['black'], (0,0,window_width,window_height))
    player_lose_text = font.render(f"PLAYER {lost} LOST", 1, color['white'])
    main_window.blit(player_lose_text, (100, 100))

    # Update the screen
    pygame.display.update()
    clock.tick(30)

# Close the window
pygame.quit()
