class CarHorizontal(object):
    def __init__(self, board, size):
        self.board = board
        self.position = position
        self.size = size

    def getCarPosition(self):
        return self.pos

    def setCarPosition(self, position):
        self.pos = position

class CarRed(object):
    def __init__(self, board, size):
        self.board = board
        self.position = position
        self.size = size

    def getCarPosition(self):
        return self.pos

    def setCarPosition(self, position):
        self.pos = position

def moveNorth(carID, steps):
    
    # check if car orientation is Vertical
    if self.Vehicle.length == 2:
        length = 2
    else:
        length = 3
        
    # get car position
    old_x = board.position.getX()
    old_y = board.position.getY()

    # check if new position is in room
    new_location = (old_x, (old_y + steps))
    if self.board.isPositionOnBoard(new_location) != True
        return False
    
    # check if column is empty for n steps
    else:
        for each i in range(0, steps):
            if (y + i) != '-':
                return False
            
    # move car steps op een manier?        
    for each i in range (0, steps):
        swap (x, y) met (x, y + 1)
        swap (x, y - 1) met (x, y)
        if length = 3:
            swap (x, y - 2) met (x, y - 1)
    
def moveEast(car, steps):

# get position car

# check if new position is in room

# check if row is empty for n steps

# move car n steps

# give error if movement is impossible

def moveSouth(car, steps):

# get position car

# check if new position is in room

# check if column is empty for n steps

# move car n steps

# give error if movement is impossible

def moveWest(car, steps):

# get position car

# check if new position is in room

# check if row is empty for n steps

# move car n steps

# give error if movement is impossible
