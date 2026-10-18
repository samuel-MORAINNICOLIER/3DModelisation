from _3D.Polyedre import Polyedre
from _3D.Polygon import Polygon
from _3D.Segment import Segment
from _3D.Point import Point

def createCube(center:Point, length:float)->list[Polygon]:
    """
    Fonction qui créé les polygones, segments et points du cube
    Les points du cube appartiendront au même plan 3D que le centre.
    :param center: Centre du cube
    :param length: Longueur des arêtes du cube
    :return: liste de polygones
    """
    plan = center.getPlan()

    # Points
    p1 = Point(plan,
               center.getCoord3D()[0] - length // 2,  # x
               center.getCoord3D()[1] + length // 2,  # y
               center.getCoord3D()[2] - length // 2)  # z
    p2 = Point(plan,
               center.getCoord3D()[0] + length // 2,  # x
               center.getCoord3D()[1] + length // 2,  # y
               center.getCoord3D()[2] - length // 2)  # z
    p3 = Point(plan,
               center.getCoord3D()[0] + length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2] - length // 2)  # z
    p4 = Point(plan,
               center.getCoord3D()[0] - length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2] - length // 2)  # z

    p5 = Point(plan,
               center.getCoord3D()[0] - length // 2,  # x
               center.getCoord3D()[1] + length // 2,  # y
               center.getCoord3D()[2] + length // 2)  # z
    p6 = Point(plan,
               center.getCoord3D()[0] + length // 2,  # x
               center.getCoord3D()[1] + length // 2,  # y
               center.getCoord3D()[2] + length // 2)  # z
    p7 = Point(plan,
               center.getCoord3D()[0] + length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2] + length // 2)  # z
    p8 = Point(plan,
               center.getCoord3D()[0] - length // 2,  # x
               center.getCoord3D()[1] - length // 2,  # y
               center.getCoord3D()[2] + length // 2)  # z

    # Centres
    center1 = Point(plan,
                    center.getCoord3D()[0],  # x
                    center.getCoord3D()[1],  # y
                    center.getCoord3D()[2] - length // 2)  # z)
    center2 = Point(plan,
                    center.getCoord3D()[0] + length // 2,  # x
                    center.getCoord3D()[1],  # y
                    center.getCoord3D()[2])  # z)
    center3 = Point(plan,
                    center.getCoord3D()[0],  # x
                    center.getCoord3D()[1],  # y
                    center.getCoord3D()[2] + length // 2)  # z)
    center4 = Point(plan,
                    center.getCoord3D()[0] - length // 2,  # x
                    center.getCoord3D()[1],  # y
                    center.getCoord3D()[2])  # z)
    center5 = Point(plan,
                    center.getCoord3D()[0],  # x
                    center.getCoord3D()[1] + length // 2,  # y
                    center.getCoord3D()[2])  # z)
    center6 = Point(plan,
                    center.getCoord3D()[0],  # x
                    center.getCoord3D()[1] - length // 2,  # y
                    center.getCoord3D()[2])  # z)
    
    face1 = Polygon([Segment([p1, p2]),
                                Segment([p2, p3]),
                                Segment([p3, p4]),
                                Segment([p4, p1])], center1)
    face2 = Polygon([Segment([p2, p6]),
                                Segment([p6, p7]),
                                Segment([p7, p3]),
                                Segment([p3, p2])], center2)
    face3 = Polygon([Segment([p5, p6]),
                                Segment([p6, p7]),
                                Segment([p7, p8]),
                                Segment([p8, p5])], center3)
    face4 = Polygon([Segment([p5, p1]),
                                Segment([p1, p4]),
                                Segment([p4, p8]),
                                Segment([p8, p5])], center4)
    face5 = Polygon([Segment([p5, p6]),
                                Segment([p6, p2]),
                                Segment([p2, p1]),
                                Segment([p1, p5])], center5)
    face6 = Polygon([Segment([p8, p7]),
                                Segment([p7, p3]),
                                Segment([p3, p4]),
                                Segment([p4, p8])], center6)

    return [face1, face2, face3, face4, face5, face6]


class Cube(Polyedre) :
    def __init__(self, center: Point, length: float):
        polygons = createCube(center, length)
        super().__init__(polygons, center)
