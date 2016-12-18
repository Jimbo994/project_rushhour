import sys
import copy
import breadthfirst
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
                n = 1
                a = 0
                while a < n:
                    # check if vehicle can move left & change x coordinate
                    a += 1
                    if vehicle.x - a >= 0 and board[vehicle.y][vehicle.x - a] == '_':
                        n += 1
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.x -=  a
                                children.append(new_configuration)

                n = 1
                a = 0
                # check if vehicle can move right & change x coordinate
                while a < n:
                    a += 1
                    if vehicle.x + a + vehicle.length - 1 < self.width and board[vehicle.y][vehicle.x + a + vehicle.length - 1] == '_':
                        n += 1
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.x +=  a
                                children.append(new_configuration)

            # move vehicles vertically
            if vehicle.orientation == 'V':
                n = 1
                a = 0
                while a < n:
                    a += 1
                    # check if vehicle can move up & change y coordinate
                    if vehicle.y - a  >= 0 and board[vehicle.y - a][vehicle.x] == '_':
                        n += 1
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.y -= a
                                children.append(new_configuration)

                # check if vehicle can move down & change y coordinate
                n = 1
                a = 0
                while a < n:
                    a += 1
                    if vehicle.y + a + vehicle.length - 1 < self.height and board[vehicle.y + a + vehicle.length - 1][vehicle.x] == '_':
                        n += 1
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.y += a
                                children.append(new_configuration)
        return children

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
        print "begintijd:", begintime

        # run algorithme
        steps_taken, counter = breadthfirst.BreadthFirst(board, configuration)

        endtime = datetime.now()
        print "Eindtijd:", endtime
        print "Totale runtijd:", endtime - begintime
        print "Aantal stappen gezet:", steps_taken
        print "Aantal bezochte configuraties:", counter
