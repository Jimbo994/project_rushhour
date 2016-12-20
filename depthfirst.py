import sys, copy
from collections import deque
from datetime import datetime

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
                    board[y][x+i] = id
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = id
        return board

    def get_string(self, configuration):
        stringconfiguration = ""
        for vehicles in configuration:
            stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)
            stringconfiguration += stringvehicle
        return stringconfiguration

    def get_moves(self, configuration):
        board = self.get_board(configuration)

        # create list for new configurations
        children = []

        for vehicle in configuration:
            if vehicle.orientation == 'H':
                a = 1
                # check for left
                if vehicle.x - a >= 0 and board[vehicle.y][vehicle.x - a] == '_':
                    while vehicle.x - a >= 0 and board[vehicle.y][vehicle.x - a] == '_':
                        maximum = a
                        a += 1
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.x -=  maximum
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

                # check for right
                b = 1
                if vehicle.x + b + vehicle.length - 1 < self.width and board[vehicle.y][vehicle.x + b + vehicle.length - 1] == '_':
                    while vehicle.x + b + vehicle.length - 1 < self.width and board[vehicle.y][vehicle.x + b + vehicle.length - 1] == '_':
                        maximum = b
                        b += 1
                    # copy configuration
                    new_configuration = configuration[:]
                    # find movable car
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.x +=  maximum
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

            # move vehicles vertically
            if vehicle.orientation == 'V':
                c = 1
                if vehicle.y - c  >= 0 and board[vehicle.y - c][vehicle.x] == '_':
                    while vehicle.y - c >= 0 and board[vehicle.y - c][vehicle.x] == '_':
                        maximum = c
                        c += 1
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.y -= maximum
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

                # check if vehicle can move down & change y coordinate
                d = 1
                if vehicle.y + d + vehicle.length - 1 < self.height and board[vehicle.y + d + vehicle.length - 1][vehicle.x] == '_':
                    while vehicle.y + d + vehicle.length - 1 < self.height and board[vehicle.y + d + vehicle.length - 1][vehicle.x] == '_':
                        maximum = d
                        d += 1
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.y += maximum
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)
        return children

# https://jeremykun.com/tag/breadth-first-search/
def DepthFirst(configuration):
    #create archive & queue
    archive = {}
    counter = 0
    depth = 0
    steps_taken = 0
    stack = deque([configuration])

    # create string of starting configuration for archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(stack) > 0:
        
        depth += 1
        current_configuration = stack.pop()
        counter += 1

        # keep counter for long runs :D
        if counter % 50000 == 0:
            print counter, "at:", datetime.now()

        # create string of currently checked configuration
        stringCurrentConfiguration = board.get_string(current_configuration)
        if 'x42H' in stringCurrentConfiguration:
            parent = archive[stringCurrentConfiguration]

            # create solution
            while archive[parent] != None:
                child = parent
                parent = archive[parent]

                # check string for different position of cars
                for i in range(len(child)):
                    if parent[i] != child[i] and str.isalpha(parent[i - 1]):
                        print "from", child[i - 1:i + 3], "to", parent[i - 1:i + 3]
                    elif parent[i] != child[i]:
                        print "from", child[i - 2:i + 2], "to", parent[i - 2:i + 2]
                # update steps_taken
                steps_taken += 1
            print "stappen",steps_taken, "configuraties", counter
            return True

        # get_moves yields list of list of objects
        for children in board.get_moves(current_configuration):
            stringChildConfiguration = board.get_string(children)

            if (stringChildConfiguration not in archive):
                stack.append(children)
                archive[stringChildConfiguration] = stringCurrentConfiguration, i

    return False

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
        board = Board(6, 6, configuration)
        print board
        begintime = datetime.now()
        print "Begintijd:", begintime

        # run algorithme
        DepthFirst(configuration)

        endtime = datetime.now()
        print "Eindtijd:", endtime
        print "Totale runtijd:", endtime - begintime
        #print "Totaal aantal gezette stappen:", steps_taken
        #print "Totaal aantal bezochte configuraties:", counter
