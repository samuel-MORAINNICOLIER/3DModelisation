import pygame
from _3D.Point import Point

class Segment :
    def __init__(self, points:list):
        self.__points:list[Point] = points
        self.__rotation:dict = {'x':0.0,'y': 0.0,'z': 0.0}


    # Gestion des coordonnées ---------------------------------

    def getPoints(self)->list:
        return self.__points

    def isSegmentInPlan(self)->bool:
        """
        Vérifie que le segment se situe bien dans le plan 3D.
        :return: True si le segment est dans le plan, False sinon.
        """
        rep = True
        i=0
        while rep!=False and i<len(self.__points):
            if not self.__points[i].isPointInPlan() :
                rep = False
            else :
                i+=1
        return rep


    # gestion de la rotation ---------------------------------

    def rotateTo(self, axis: str, degree: float, center: Point):
        """

        :param axis:
        :param degree:
        :param center:
        :return:
        """
        for point in self.__points :
            point.rotateTo(axis, degree, center)


    # Gestion de l'affichage ----------------------------------

    def pygameDraw(self,screen,  color:str="blue")->bool:
        """
        Dessine avec pygame le segment sur l'écran.
        Si l'option check du plan est True, le segment ne sera pas dessiné en dehors du plan 3D.
        Le plan du segment sera celui de son premier point.
        :param screen:
        :param color:
        :return: Si le segment est en dehors du plan retourne False et True sinon.
        """
        rep = False
        plan = self.__points[0].getPlan()
        if not(plan.getCheck()) or self.isSegmentInPlan() :
            pygame.draw.line(screen, color, self.__points[0].getCoord2D(), self.__points[1].getCoord2D())
            rep = True
        return rep
