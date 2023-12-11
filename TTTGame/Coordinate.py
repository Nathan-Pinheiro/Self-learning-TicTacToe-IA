class Coordinate :
    x : int
    y : int
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    def __str__(self): return f"({self.x}; {self.y})"

def CoordinateListToString(coordinate_list):
    return '[' + ', '.join(map(str, coordinate_list)) + ']'

def isCoordinateInList(x : int, y : int, listCoordinate : list[Coordinate]) :
    for c in listCoordinate:
        if(c.x == x and c.y == y): return True
    return False