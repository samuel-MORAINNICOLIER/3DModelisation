from _3D.Polygon import Polygon
from _3D.Segment import Segment
from _3D.Point import Point

def createSquare(center:Point, length: float)->list:
    """
    Fonction qui créé les segments et les points du carré.
    Les points du carré appartiendront au même plan que le centre.
    :param center: Centre du carré.
    :param length: Longueur du carré.
    :return: Liste de segments
    """
    plan = center.getPlan()
    p1 = Point(plan,
               center.getCoord3D()[0] - length // 2, # x
               center.getCoord3D()[1] + length // 2, # y
               center.getCoord3D()[2])               # z
    p2 = Point(plan,
               center.getCoord3D()[0] + length // 2, # x
               center.getCoord3D()[1] + length // 2, # y
               center.getCoord3D()[2])               # z
    p3 = Point(plan,
               center.getCoord3D()[0] + length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2])  # z
    p4 = Point(plan,
               center.getCoord3D()[0] - length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2])  # z
    return [Segment([p1, p2]),
            Segment([p2, p3]),
            Segment([p3, p4]),
            Segment([p4, p1])]

class Square(Polygon) :
    def __init__(self, center: Point, length: float):
        segments = createSquare(center, length)
        super().__init__(segments, center)
        self.__segments = segments

