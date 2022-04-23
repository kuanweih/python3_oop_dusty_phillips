import math


class Point:
    """ Represent a point in 2D geometric coordinates.
    """    
    
    def __init__(self, x=0, y=0):
        """ Initialize the position of a new point at (x, y).
        """
        self.move(x, y)
        
    def move(self, x, y):
        """ Move the point to (x, y). """
        self.x = x
        self.y = y
        
    def reset(self):
        """ Reset the point back to (0, 0). """
        self.move(0, 0)
        
    def calc_distance(self, other_point):
        """ Calculate the distance between this point and another point """
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2)