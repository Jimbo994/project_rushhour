class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        
        # we'll use length = 2 for now
        self.length = 2
        
        self.x = x
        self.y = y
        self.orientation = orientation

    def vehicleInfo(self):
        return "Vehicle({0}, {1}, {2}, {3})".format(self.id, self.x, self.y, self.orientation)

# een class 'move' en locatie op board
class Move(Vehicle):
    def __init__(id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
    # is de vehicle movable?
        # bij elke move wat toevoegen aan queue
        # BreadthFirst limiten tot hoe diep die gaat
    # gaan we het vanuit de muur of vanuit de auto doen?
    # houd rekening met dat 1 stap 4/3/2/1 blokken lang kan zijn
