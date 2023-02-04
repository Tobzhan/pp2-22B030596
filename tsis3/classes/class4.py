"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""

import math
class Point:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def display( self ):
        print ("x = {0}, y = {1}".format( self.x, self.y ))

    def set( self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist( self, newPoint ):
        distance = float()
        distance = math.sqrt(abs(self.x - newPoint.x)**2 + abs( self.y - newPoint.y)**2)
        return distance

point1 = Point(0, 0)
point2 = Point(1, 1)
point1.display()
print("%.2f" %point1.dist(point2))
point2.set( 3, 4)
print( "%.2f" %point1.dist(point2))

