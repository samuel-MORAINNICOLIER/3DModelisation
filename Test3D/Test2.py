"""
Programme rapide et à part du projet
pour tester une formule de rotation en 2D
"""

import pygame
from math import *

# Initialisation des paramètres de la fenêtre
WIDTH = 800
HEIGHT = 800
DEPTH = 8000
background_color = "white"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = screen.fill(background_color)

clock = pygame.time.Clock()
FPS = 60
play = True

# Initialisation des objets 3D
center = [0, 0]
p1 = [200, 0]

isRPres = False
while play :
    clock.tick(FPS)

    # Gérer les événements :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                isRPres = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                isRPres = False

    # Contrôle des touches
    if isRPres :
        x, y = p1
        xCenter, yCenter = center
        degreeRadian = 0.1

        newX = x * cos(degreeRadian) - y * sin(degreeRadian) + xCenter
        newY = y * cos(degreeRadian) + x * sin(degreeRadian) + yCenter
        p1 = (newX, newY)

    # Effacer la surface
    screen.fill(background_color)

    # Témoin
    pygame.draw.circle(screen, 'yellow', (600, 400), 5.0)

    pygame.draw.circle(screen, 'blue', (p1[0]+400, p1[1]+400) ,5.0)
    pygame.draw.circle(screen, 'red', (center[0]+400, center[1]+400), 5.0)

    # Basculer le buffer screen sur l'écran
    pygame.display.flip()