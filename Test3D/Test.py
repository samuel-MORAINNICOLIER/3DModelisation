import pygame
from _3D.Plan import Plan
from _3D.Point import Point
from _3D.Segment import Segment
from _3D.Square import Square
from _3D.Cube import Cube

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
plan1 = Plan(WIDTH, HEIGHT, DEPTH, 90, False)

pointCentre = Point(plan1, 0, 0, 10)
point2 = Point(plan1, 0, 0, 10)
temoin = Point(plan1, 200,0,10)

#square1 = Square(Point(plan1, 0,0,0), 200)
cube1 = Cube(Point(plan1, 0,0,0),100)

is1Pres = False # x
is2Pres = False # y
is3Pres = False # z
while play :
    clock.tick(FPS)

    # Gérer les événements :
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

    # Contrôle des touches
    if is1Pres :
        cube1.rotateSelf('x', 1)
    if is2Pres :
        cube1.rotateSelf('y', 1)
    if is3Pres :
        cube1.rotateSelf('z', 1)

    #print('p1 : ', point2.getCoord3D())
    #print('s1 : ', square1.getCoord3D(), '|----| p1 : ', point2.getCoord3D())

    # Effacer la surface
    screen.fill(background_color)

    # Afficher les objets
    #point2.pygameDraw(screen, "blue")
    #temoinS1.pygameDrawEdges(screen, "black")
    cube1.pygameDrawEdges(screen, 'black')
    pointCentre.pygameDraw(screen)

    cube1.getCenter().pygameDraw(screen, 'purple')
    #for face in cube1.getPolygons():
        #face.getCenter().pygameDraw(screen)

    print(cube1.getRotation())

    # Basculer le buffer screen sur l'écran
    pygame.display.flip()