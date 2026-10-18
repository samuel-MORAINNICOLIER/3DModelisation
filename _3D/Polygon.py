import pygame
from _3D.Point import Point

class Polygon :
    def __init__(self, segments:list, center:Point):
        self.__segments:list = segments
        self.__rotation:dict = {'x':0.0,'y': 0.0,'z': 0.0}
        self.__center:Point = center


    # Gestion des coordonnées ---------------------------------

    def getSegment(self)->list:
        return self.__segments

    def getPoints(self)->list:
        """

        :return: La liste des points, le centre est le premier point.
        """
        points = [self.__center]
        for segment in self.__segments:
            for point in segment.getPoints() :
                if point not in points :
                    points.append(point)
        return points

    def getCoord3D(self)->tuple:
        return self.__center.getCoord3D()

    def getCenter(self)->Point:
        return self.__center

    def isPolygonInPlan(self)->bool:
        """
        Vérifie que le polygone se situe bien dans le plan 3D.
        :return: True si le polygone est dans le plan, False sinon.
        """
        rep = True
        i = 0
        while rep != False and i < len(self.__segments):
            if not self.__segments[i].isSegmentInPlan():
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

    def rotateTo(self, axis: str, degree: float, center: Point):
        """

        :param axis:
        :param degree: Axe de rotation (de 0 à 360°)
        :param center:
        :return:
        """
        self.addRotation(axis, degree)
        for point in self.getPoints():
            point.rotateTo(axis, degree, center)


    # Gestion de l'affichage ----------------------------------

    def pygameDrawEdges(self,screen, color:str="blue")->bool:
        """
        Dessine avec pygame le polygone sur l'écran.
        :param screen:
        :param color:
        :return: Si le polygone est en dehors du plan retourne False et True sinon.
        """
        rep = False
        plan = self.__center.getPlan()
        if not(plan.getCheck())or self.isPolygonInPlan():
            for segment in self.__segments :
               segment.pygameDraw(screen, color)
            rep = True
        return rep
