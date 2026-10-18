import importlib
from math import *

import pygame
from _3D.Plan import Plan
importlib.import_module('_3D.Plan')

class Point :
    def __init__(self, plan, x:int, y:int, z:int):
        self.__plan:Plan = plan
        self.__x:int = x
        self.__y:int = y
        self.__z:int = z


    # Gestion des coordonnées ---------------------------------

    def getCoord2D(self)->tuple|None:
        """
        Si le point se situe dans le plan 3D,
        renvoie les coordonnées sur le plan projeté en 2dimensions du plan (l'écran).
        Sinon renvoie None.
        :return: Les coordonnées du point sur l'écran.
        """
        fovAngle = self.__plan.getFovAngle()*pi/180.0
        rep = None
        # Si le plan n'autorise pas la vérification ou s'il l'autorise et que le point est dans le plan :
        if not(self.__plan.getCheck()) or (self.__plan.getCheck() and self.isPointInPlan()):
            # nvelle coord = milieu plan +|- coord/(z/angle de vue)
            #x2D = self.__plan.getCenter2D()[0] + self.__x / (self.__z / tan(fovAngle / 2))
            #y2D = self.__plan.getCenter2D()[1] - self.__y / (self.__z / tan(fovAngle / 2))
            x2D = self.__plan.getCenter2D()[0] + self.__x #/ self.__z
            y2D = self.__plan.getCenter2D()[1] - self.__y #/ self.__z
            rep = x2D, y2D
        return rep

    def getCoord3D(self)->tuple:
        return self.__x, self.__y, self.__z

    def getPlan(self):
        return self.__plan

    def setCoord3DX(self, x:int)->None:
        self.__x = x

    def setCoord3DY(self, y:int)->None:
        self.__y = y

    def setCoord3DZ(self, z:int)->None:
        self.__z = z

    def isPointInPlan(self)->bool:
        """
        Vérifie que le point se situe bien dans le plan 3D.
        :return: True si le point est dans le plan, False sinon.
        """
        isPointInPlan = False
        if 1 <= self.__z <= 1 + self.__plan.getDimensions3D()[2]:
            # Ajouter les vérifications sur les axes x et y.
            isPointInPlan = True
        return isPointInPlan


    # gestion de la rotation ---------------------------------

    def rotateTo(self,axis:str, degree:float, center:'Point'):
        """
        Fait pivoter le point autour d'un centre de rotation sur l'axe et selon le degrée choisi
        :param axis: x, y ou z (une seule lettre, en minuscule)
        :param degree: De 0 à 360 ou plus
        :param center: Centre de rotation
        :return: None
        """
        x,y,z = self.getCoord3D()
        xCenter, yCenter, zCenter = center.getCoord3D()
        degreeRadian = degree*pi/180
        if axis == "x" :
            # Alors la rotation se passera sur le plan YZ
            newY = y*cos(degreeRadian) - z*sin(degreeRadian) #+ yCenter
            newZ = z*cos(degreeRadian) + y*sin(degreeRadian) #+ zCenter
            self.setCoord3DY(newY)
            self.setCoord3DZ(newZ)
        elif axis == "y" :
            # Alors la rotation se passera sur le plan XZ
            newX = x*cos(degreeRadian) + z*sin(degreeRadian) #+ xCenter
            newZ = z*cos(degreeRadian) - x*sin(degreeRadian) #+ zCenter
            self.setCoord3DX(newX)
            self.setCoord3DZ(newZ)
        elif axis == "z" :
            # Alors la rotation se passera sur le plan XY
            newX = x*cos(degreeRadian) - y*sin(degreeRadian) #+ xCenter
            newY = y*cos(degreeRadian) + x*sin(degreeRadian) #+ yCenter
            self.setCoord3DX(newX)
            self.setCoord3DY(newY)



    # Gestion de l'affichage ----------------------------------

    def pygameDraw(self, screen, color:str="red")->bool:
        """
        Dessine avec pygame le point sur l'écran.
        :param screen:
        :param color:
        :return: Si le point est en dehors du plan retourne False et True sinon.
        """
        rep = False
        if self.getCoord2D() is not None:
            rep = True
            pygame.draw.circle(screen, color, self.getCoord2D(), 7)
        return rep