import sys, copy, breadthfirst, depthfirst#, willekeur
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

    # visualisation
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
                    board[y][x + i] = id
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = id
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

if __name__ == '__main__':
    # input: rushhour.py [algorithmname] [problemfilename]

    # open problem on board
    filename = sys.argv[2]
    with open(filename) as file:
        # start timer
        begintime = datetime.now()
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

        #create board
        if "1" in sys.argv[2] or "2" in sys.argv[2] or "3" in sys.argv[2]:
            board = Board(6, 6, configuration)
        elif "4" in sys.argv[2] or "5" in sys.argv[2] or "6" in sys.argv[2]:
            board = Board(9, 9, configuration)
        elif "7" in sys.argv[2]:
            board = Board(12, 12, configuration)
        else:
            print "Sorry, that is not a valid board."

        print board
        # use correct algorithm
        if sys.argv[1] == "breadthfirst":
            steps_taken, counter = breadthfirst.BreadthFirst(board, configuration)

            # print results
            endtime = datetime.now()
            print "Totale runtijd:", endtime - begintime
            print "Aantal stappen gezet:", steps_taken
            print "Aantal bezochte configuraties:", counter

        elif sys.argv[1] == "depthfirst":
            steps_taken, counter = depthfirst.DepthFirst(board, configuration)

            # print results
            endtime = datetime.now()
            print "Totale runtijd:", endtime - begintime
            print "Aantal stappen gezet:", steps_taken
            print "Aantal bezochte configuraties:", counter

        elif sys.argv[1] == "random":
            results = []

            for i in range(0, 1000):
                print "Current iteration:", i
                result = (random.Willekeur(board, configuration))
                if result != None:
                    results.append(result)
                    print "Currently found solutions with these amount of moves:\n", sorted(results)
            print "These are the amount of moves of the solutions found:", sorted(results)

        else:
            print "Sorry, that is not a valid algorithm."
