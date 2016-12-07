import sys
import copy
from collections import deque

class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation

class Board(object):
    def __init__(self, width, height, configuration):
        self.width = width
        self.height = height
        self.configuration = configuration

    #visualisation
    def __str__(self):
        block = ''
        for line in self.get_board(configuration):
            block = block + '{0}\n'.format(''.join(line))
        return block

    def get_board(self, configuration):
        board = [['_' for w in range(self.width)] for h in range(self.height)]

        for vehicle in configuration:
            orientation = vehicle.orientation
            x = vehicle.x
            y = vehicle.y
            id = vehicle.id

            # check id for length (x = red car)
            if id >= 'A' and id <= 'Z' or id == '!' or id == 'x':
                vehicle.length = 2
            elif id >= 'a' and id <= 'w':
                vehicle.length = 3

            # put vehicles on board
            if orientation == 'H':
                for i in range(vehicle.length):
                    board[x+i][y] = id
            else:
                for i in range(vehicle.length):
                    board[x][y+i] = id
        return board

    def get_moves(self, configuration):
        board = self.get_board(configuration)

        # create list for new configurations
        children = []
        for vehicle in configuration:
            if vehicle.orientation == 'H':
                # check if vehicle can move left & change x coordinate
                if vehicle.x - 1 >= 0 and board[vehicle.x - 1][vehicle.y] == '_':
                    new_configuration = copy.deepcopy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.x -= 1
                            children.append(new_configuration)

                # check if vehicle can move right & change x coordinate
                if vehicle.x + vehicle.length < self.width and board[vehicle.x + vehicle.length][vehicle.y] == '_':
                    new_configuration = copy.deepcopy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.x += 1
                            children.append(new_configuration)

            # move vehicles vertically
            if vehicle.orientation == 'V':
                # check if vehicle can move up & change y coordinate
                if vehicle.y - 1 >= 0 and board[vehicle.x][vehicle.y - 1] == '_':
                    new_configuration = copy.deepcopy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.y -= 1
                            children.append(new_configuration)

                # check if vehicle can move down & change y coordinate
                if vehicle.y + vehicle.length < self.height and board[vehicle.x][vehicle.y + vehicle.length] == '_':
                    new_configuration = copy.deepcopy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.y += 1
                            children.append(new_configuration)
        return children

# https://jeremykun.com/tag/breadth-first-search/

def BreadthFirst(configuration):
    #create archive & queue
    archive = {}
    counter = 0
    queue = deque([configuration])
    stringStartingConfiguration = ""

    # create string of starting configuration for archive
    for vehicles in configuration:
        stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)
        stringStartingConfiguration += stringvehicle
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        current_configuration = queue.pop()
        counter += 1
        stringcars = ""

        # create string of currently checked configuration
        for vehicles in current_configuration:
            stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)
            stringcars += stringvehicle

        # check if current configuration is won
        for vehicle in current_configuration:
            if vehicle.id == 'x' and vehicle.x == 7 and vehicle.y == 4 and vehicle.orientation == 'H':
                print "Apparently we won! :D"
                print "Winning String:", stringcars

                i = 0
                parent = archive[stringcars]
                while archive[parent] != None:
                    parent = archive[parent]
                    print 'Parents:\n', parent
                    i = i + 1
                print "Totaal aantal gezette stappen:", i
                print "Totaal aantal bezochte configuraties:", counter
                return True

        # get_moves yields list of list of objects
        for children in board.get_moves(current_configuration):
            stringCurrentConfiguration = ""
            for cars in children:
                stringvehicles = str(cars.id) + str(cars.x) + str(cars.y) + str(cars.orientation)
                stringCurrentConfiguration += stringvehicles

            if (stringCurrentConfiguration not in archive):
                queue.appendleft(children)
                archive[stringCurrentConfiguration] = stringcars

if __name__ == '__main__':
    # open problem on board
    filename = sys.argv[1]
    with open(filename) as file:
        configuration = []

        # store cars with id, x, y (letters as coordinates) and orientation in Vehicle classes, then in array configuration
        for row in file:
            row = row[:-1]
            id, x, y, orientation = row
            # convert y & x to ascii (ord) and then to int
            y = int(ord(y) - 65)
            x = int(ord(x) - 65)
            vehicle = Vehicle(id, x, y, orientation)
            configuration.append(vehicle)

        # create board
        board = Board(9, 9, configuration)
        print board

        # run algorithme
        BreadthFirst(configuration)
