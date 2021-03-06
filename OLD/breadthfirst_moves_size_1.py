import sys, copy
from datetime import datetime
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
                # check if vehicle can move left & change x coordinate
                if vehicle.x - 1 >= 0 and board[vehicle.x - 1][vehicle.y] == '_':
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.x -=  1
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

                # check if vehicle can move right & change x coordinate
                if vehicle.x + vehicle.length < self.width and board[vehicle.x + vehicle.length][vehicle.y] == '_':
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.x +=  1
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

            # move vehicles vertically
            if vehicle.orientation == 'V':
                # check if vehicle can move up & change y coordinate
                if vehicle.y - 1 >= 0 and board[vehicle.x][vehicle.y - 1] == '_':
                    # copy configuration
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.y -=  1
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)

                # check if vehicle can move down & change y coordinate
                if vehicle.y + vehicle.length < self.height and board[vehicle.x][vehicle.y + vehicle.length] == '_':
                    new_configuration = configuration[:]
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            index = new_configuration.index(vehicle)
                            new_vehicle = copy.deepcopy(vehicle)
                            new_vehicle.y += 1
                            new_configuration[index] = new_vehicle
                            children.append(new_configuration)
        return children

# https://jeremykun.com/tag/breadth-first-search/

def BreadthFirst(configuration):
    #create archive & queue
    archive = {}
    counter = 0
    steps_taken = 0
    queue = deque([configuration])

    # create starting node in archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        current_configuration = queue.pop()
        counter += 1

        # keep counter for long runs :D
        if counter % 50000 == 0:
            print counter, "at:", datetime.now()

        # check win condition
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
            return steps_taken, counter

        # get moves of current configuration
        for children in board.get_moves(current_configuration):
            stringChildConfiguration = board.get_string(children)
            if stringChildConfiguration not in archive:
                queue.appendleft(children)
                archive[stringChildConfiguration] = stringCurrentConfiguration

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
        steps_taken, counter = BreadthFirst(configuration)

        # print results
        endtime = datetime.now()
        print "Eindtijd:", endtime
        print "Totale runtijd:", endtime - begintime
        print "Aantal stappen gezet:", steps_taken
        print "Aantal bezochte configuraties:", counter
