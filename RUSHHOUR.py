import sys

# keeps track of the Position of a vehicle
class Position(object):
    def __init__(self, x, y):
        self.x = x
        print "Position x: " + str(self.x)
        self.y = y
        print "Position y: " + str(self.y)
    
    # to be able to use x and y in class 
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_new_position(self):
        old_x, old_y = self.get_x(), self.get_y()
        new_x = old_x + 1
        new_y = old_y + 0
        print "Position new x: " + str(new_x)
        print "Position new y: " + str(new_y)
        return Position(new_x, new_y)

class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation

        if self.id >= 'A' and self.id <= 'G':
            self.length = 2
        elif self.id >= 'O' and self.id <= 'Z':
            self.length = 3

        # self.position = position

        # self.board = board
        self.pos = self.get_position(x, y)

    def get_position(self, x, y):
        # x = raw_input("Give me a X coordinate: ")
        # y = raw_input("Give me an Y coordinate: ")
        print x
        print y
        return Position(int(x), int(y))

    # this method isn't used yet
    def get_vehicle_position(self):
        print "Position: " + self.pos
        return self.pos

    def set_vehicle_position(self, position):
        self.pos = position

    def update_position(self):
        new_position = self.pos.get_new_position()
        if self.board.is_position_on_board(new_position) == True:
            # self.set_vehicle_position(new_position)
            self.pos = new_position
            print "New vehicle position is on board."
        else:
            print "ERROR: new vehicle position is not on board."
    
    # def get_moves(self):
        # deze functie callen om in queue te stoppen?
            # als auto horizontaal is
                # naar links gaan
                    # check of er een auto is die op x-1 staat
                # naar rechts gaan
                    # check of auto op x+1+i staat
            # als auto verticaal is
                    # check of er een auto is die op x-1 staat
                # naar rechts gaan
                    # check of auto op x+1+i staat

    # algoritme
        # get_moves callen per auto
        # check for board state
        # alle mogelijke moves van een auto
        # moves hier maken 
        # opslaan welke moves er zijn gemaakt met welke auto
            # tuple aanmaken

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        block = ''
        for line in self.get_board():
            block = block + '{0}\n'.format(''.join(line))
        print block
        return block

    def is_position_on_board(self, pos):
        checkX = pos.get_x()
        checkY = pos.get_y()

        if checkX < 0 or checkX > self.width:
            return False
        if checkY < 0 or checkY > self.height:
            return False
        else:
            return True

    # we don't need this, just for visualisation
    def get_board(self):
        board = [['_' for x in range(self.width)] for y in range(self.height)]

        for vehicle in range(1):
            orientation = 'H'
            length = 3
            y = 0
            x = 2
            id = 'A'
            if orientation == 'H':
                for i in range(length):
                    board[y][x + i] = id
            else:
                for i in range(length):
                    board[y + i][x] = id
        print board
        return board

if __name__ == '__main__':
    # filename is second argument given in command line
    filename = sys.argv[1]
    with open(filename) as file:
        # make a new array
        vehicles = []
        for line in file:
            # store a line in variable 'line' but leave the '\n' out
            line = line[:-1]
            # store every value that's in line in id - y - x - orientation
            id, y, x, orientation = line
            # y and x values are letters, convert these to their ascii values (ord) and convert to string (str)
            y = str(ord(y) - 48)
            x = str(ord(x) - 48)
            # test test, we can leave this out later
            print "ID: " + id
            print "Y: " + y
            print "X: " + x
            # send the values to class Vehicle and store this is vehicles
            vehicle = Vehicle(id, x, y, orientation)
            # store all the vehicle variables in the vehicles array that we just made
            vehicles.append(vehicle)
        # make a board of width = 6 and height = 6
        board = Board(6, 6)
        print board
            # pos = Position(x, y)
