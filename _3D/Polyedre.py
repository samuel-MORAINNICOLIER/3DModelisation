import pygame
from _3D.Point import Point

class Polyedre :
    def __init__(self, polygons:list, center:Point):
        self.__polygons:list = polygons
        self.__rotation:dict = {'x':0.0,'y': 0.0,'z': 0.0}
        self.__center:Point = center


    # Gestion des coordonnées ---------------------------------

    def getPolygons(self)->list:
        """
        Renvoie les polygones qui constituent les faces du polyèdre.
        :return:
        """
        return self.__polygons

    def getCoord3D(self) -> tuple:
        return self.__center.getCoord3D()

    def getCenter(self)-> Point:
        return self.__center

    def isPolyedreInPlan(self)->bool:
        """
        Vérifie que le polyèdre se situe bien dans le plan 3D.
        :return: True si le polyèdre est dans le plan, False sinon.
        """
        rep = True
        i = 0
        while rep != False and i < len(self.__polygons):
            if not self.__polygons[i].isPolygonInPlan():
                rep = False
            else:
                i += 1
        return rep


    # gestion de la rotation ---------------------------------

    def getRotation(self)->dict:
        return self.__rotation

    def addRotation(self, axis:str, degree):
        self.__rotation[axis]+=degree
        if self.__rotation[axis] > 360 :
            self.__rotation[axis] -= 360


    def rotateSelf(self, axis: str, degree: float):
        self.addRotation(axis, degree)

        pointUsed = []
        for polygon in self.__polygons:
            pointsPoly = polygon.getPoints()
            for point in pointsPoly :
                if point not in pointUsed :
                    point.rotateTo(axis, degree, self.__center)
                    pointUsed.append(point)


    # Gestion de l'affichage ----------------------------------

    def getVisibilityFacesOrthopedic(self):
        """
        Indique si chaque face du polyèdre est visible ou non, dans le cadre du polyèdre uniquement.
        (Ne prends pas en charge les autres modèles du plan 3D)
        :return: Un dictionnaire avec les faces en attribut et un booléen en attribut.
        """
        for face in self.getPolygons():



    def pygameDrawEdges(self, screen, color:str="blue"):
        """
        Dessine avec pygame le polyèdre sur l'écran.
        :param screen:
        :param color:
        :return:
        """
        for polygon in self.__polygons:
            polygon.pygameDrawEdges(screen, color)
