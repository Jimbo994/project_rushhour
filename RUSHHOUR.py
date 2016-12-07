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
            y = vehicle.y
            x = vehicle.x
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

    def get_moves(self, configuration):
        board = self.get_board(configuration)

        # create list for new configurations
        children = []
        for vehicle in configuration:
            for i in range (1, self.width - vehicle.length):
                # move vehicles horizontally
                if vehicle.orientation == 'H':
                    # check if vehicle can move left & change x coordinate
                    if vehicle.x - i >= 0 and board[vehicle.y][vehicle.x - i] == '_':
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.x -= i
                                children.append(new_configuration)

                    # check if vehicle can move right & change x coordinate
                    if vehicle.x + vehicle.length - 1 + i < self.width and board[vehicle.y][vehicle.x + vehicle.length - 1 + i] == '_':
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.x += i
                                children.append(new_configuration)

                # move vehicles vertically
                if vehicle.orientation == 'V':
                    # check if vehicle can move up & change y coordinate
                    if vehicle.y - i >= 0 and board[vehicle.y - i][vehicle.x] == '_':
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.y -= i
                                children.append(new_configuration)

                    # check if vehicle can move down & change y coordinate
                    if vehicle.y + vehicle.length - 1 + i < self.height and board[vehicle.y + vehicle.length + i - 1][vehicle.x] == '_':
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.y += i
                                children.append(new_configuration)
        #print "dit zijn moves:", children
        yield children

# http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
# https://jeremykun.com/tag/breadth-first-search/

def BreadthFirst(configuration):
    #create archive & queueue
    #archive = set()
    archive = dict()
    
    #create archive & queue
    archive = set()
    queue = deque([configuration])
    stringstart = ""
    for vehicles in configuration:
        stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)+"\n"
        stringstart += stringvehicle
    archive[stringstart] = None
    counter = 0
    
    while len(queue) > 0:
        current_configuration = queue.pop()
        counter += 1
        #print counter
        stringcars = ""
        for vehicles in current_configuration:
            stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)+"\n"
            stringcars += stringvehicle
            
        hashed = hash(stringcars)
        if hashed in archive:
            continue
        else:
             archive.add(hashed)

        # check if won
        for vehicle in current_configuration:
            if vehicle.id == 'x' and vehicle.x == 4 and vehicle.y == 2 and vehicle.orientation == 'H':
                string = ""
                print "We won! :D"
                for cars in current_configuration:
                    stringvehicles = str(cars.id) + str(cars.x) + str(cars.y) + str(cars.orientation) +"\n"
                    string += stringvehicles
                print string
                
                parent = archive[string]
                #print parent
                #print archive[parent]
                i = 0
                while archive[parent] != None:
                    parent = archive[parent]
                    print 'huidige \n', parent
                    i = i + 1
                print "aantal stappen", i
                
                    #for vehicle in current_configuration:
                    #print vehicle.id, vehicle.x, vehicle.y, vehicle.orientation
                print counter
                return True

        for children in board.get_moves(current_configuration):
            for configuration in children:
                string = ""
                for cars in configuration:
                    stringvehicles = str(cars.id) + str(cars.x) + str(cars.y) + str(cars.orientation)+"\n"
                    string += stringvehicles

                if string not in archive:
                    queue.appendleft(configuration)
                    archive[string] = stringcars

                    children_hashed = hash(string)
                    if children_hashed not in archive:
                        queue.appendleft(configuration)
#def solution:    

if __name__ == '__main__':
    # open problem on board
    filename = sys.argv[1]
    with open(filename) as file:
        configuration = []

        # store cars with id, y, x (letters as coordinates) and orientation in Vehicle classes, then in array configuration
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
        BreadthFirst(configuration)
        # run our awesome algorithm
        
        #newboard = Board(6, 6, BreadthFirst(configuration))
        #print newboard
