import sys

"""
CLASS VEHICLE
op dit moment worden er vier values uit het problems document gehaald
(id, x, y, orientation)
we moeten nog even de id koppelen aan hoe lang een auto is
want op dit moment is de lengte alleen maar 2
of.. wat is een handige manier om te bepalen hoe lang een auto is?
we zouden dit ook kunnen meegeven in het bestand misschien?
dan wordt het id, x, y, orientation, length
"""

class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        # we'll only use length = 2 for now
        self.length = 2
        self.x = x
        self.y = y
        self.orientation = orientation

    # store all the values in Vehicle(id, x, y, orientation)
    def vehicleInfo(self):
        return "Vehicle({0}, {1}, {2}, {3})".format(self.id, self.x, self.y, self.orientation)

"""
CLASS MOVE
Things to keep in mind:
bij elke move wat toevoegen aan queue
BreadthFirst limiten tot hoe diep deze gaat
gaan we vanuit de muur of vanuit de auto checken of een auto kan bewegen?
houd rekening met dat 1 stap naar 1/2/3/4/5 blokken verder kan gaan
"""

# class move (Vehicle) en locatie op board
class Move(Vehicle):
    def __init__(id, x, y, orientation):
        self.x = x
        self.y = y
    # def isMovable?
        # check if horizontal or vertical
        # if horizontal
            # is vehicle movable to left
            # is vehicle movable to right
        # if vertical
            # can vehicle move downwards
            # can vehicle move upwards
