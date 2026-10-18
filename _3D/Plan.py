
class Plan :
    def __init__(self,width:int, height:int, depth:int,fovAngle:int=90, check=True):
        """

        :param width:
        :param height:
        :param depth:
        :param fovAngle:
        :param check: Affiche ou n'affiche pas les objets en dehors du plan, n'affiche pas par défaut.
        """
        self.__width:int = width
        self.__height:int = height
        self.__depth:int = depth
        self.__fovAngle:int = fovAngle
        self.__check:bool = check

    def setCheck(self, check:bool):
        self.__check = check

    def getCheck(self):
        return self.__check

    def getFovAngle(self):
        return self.__fovAngle

    def getDimensions2D(self)->tuple:
        """
        :return: Les dimensions de l'écran.
        """
        return self.__width, self.__height

    def getDimensions3D(self)->tuple:
        """
        :return: Les dimensions du plan 3D.
        """
        return self.__width, self.__height, self.__depth

    def getCenter2D(self)->tuple:
        """
        :return: Les coordonnées au centre du plan projeté (l'écran).
        """
        return self.__width//2, self.__height//2

    def getCenter3D(self)->tuple:
        """
        :return: Le point au centre du plan 3D.
        """
        return  0, 0, 1+self.__depth//2
    