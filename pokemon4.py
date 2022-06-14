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

running_window = True

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


