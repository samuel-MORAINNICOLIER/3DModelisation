"""
Programme de test générale du projet.
Ici le test vise la bonne modélisation du cube 3D.
"""

import pygame
from _3D.Plan import Plan
from _3D.Point import Point
from _3D.Segment import Segment
from _3D.Square import Square
from _3D.Cube import Cube

# Initialisation des paramètres de la fenêtre ----------------
WIDTH = 800
HEIGHT = 800
DEPTH = 8000
background_color = "white"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = screen.fill(background_color)

clock = pygame.time.Clock()
FPS = 60
play = True

# Initialisation des objets 3D--------------------------------
plan1 = Plan(WIDTH, HEIGHT, DEPTH, 90, False)

cube1 = Cube(Point(plan1, 0,0,0),100)
pointCentre = Point(plan1, 0, 0, 10)

is1Pres = False # x
is2Pres = False # y
is3Pres = False # z
while play :
    clock.tick(FPS)

    # Gérer les événements ----------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                is1Pres = True
            if event.key == pygame.K_2:
                is2Pres = True
            if event.key == pygame.K_3:
                is3Pres = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                is1Pres = False
            if event.key == pygame.K_2:
                is2Pres = False
            if event.key == pygame.K_3:
                is3Pres = False

    # Contrôle des touches ---------------------------------
    if is1Pres :
        cube1.rotateSelf('x', 1)
    if is2Pres :
        cube1.rotateSelf('y', 1)
    if is3Pres :
        cube1.rotateSelf('z', 1)

    # Effacer la surface -----------------------------------
    screen.fill(background_color)

    # Afficher les objets ----------------------------------

    # Afficher les arêtes du cube
    cube1.pygameDrawEdges(screen, 'black')

    # Afficher le centre de l'écran
    # pointCentre.pygameDraw(screen)

    # Afficher le centre du cube
    # cube1.getCenter().pygameDraw(screen, 'purple')

    # Afficher les centres des faces
    #for face in cube1.getPolygons():
    #    face.getCenter().pygameDraw(screen)

    # Informations -----------------------------------------
    print(cube1.getRotation())

    # Basculer le buffer screen sur l'écran ----------------
    pygame.display.flip()