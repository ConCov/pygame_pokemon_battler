import time, random
import pygame, math
from pygame.locals import *
import csv

pygame.init()
clock = pygame.time.Clock()
main_window = pygame.display.set_mode((960,500))

color = {
    'brown' : (148,109,32),
    'red' : (210,30,7),
    'grey' : (213,209,198),
    'white' : (255, 255, 255),
    'black' : (0,0,0),
    'green' : (30,210,7)
}

font = pygame.font.SysFont("Arial", 48)

player1 = {
    'xpos' : 0,
    'ypos' : 0,
    'pokemon' : 0,
    'health' : 100,
}

player2 = {
    'xpos' : 0,
    'ypos' : 0,
    'pokemon' : 1,
    'health' : 100,
}

# Load Pokemon information from file
with open("./pokemon/pokemons.csv", "r", encoding="utf-8") as f:
    pokemons = list(csv.DictReader(f, delimiter=","))

turn = 1

running_window = True

while running_window:

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
    player_turn_text = font.render(f"PLAYER {turn} TURN", 1, color['black'])
    main_window.blit(player_turn_text, (410, 10))



    for event in pygame.event.get():
        if event.type == QUIT:
            running_window = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos

        if event.type == MOUSEMOTION:
            print(event.pos)
