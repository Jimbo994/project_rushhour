import sys
import copy
from collections import deque
import random
import numpy

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
                n = 1
                a= 0
                while a < n:
                    # check if vehicle can move left & change x coordinate
                    a += 1
                    if vehicle.x - a >= 0 and board[vehicle.x - a][vehicle.y] == '_':
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
                    if vehicle.x+a + vehicle.length-1 < self.width and board[vehicle.x+a + vehicle.length-1][vehicle.y] == '_':
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
                    if vehicle.y -a  >= 0 and board[vehicle.x][vehicle.y - a] == '_':
                        n +=1
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
                    if vehicle.y + a + vehicle.length-1 < self.height and board[vehicle.x][vehicle.y + a + vehicle.length-1] == '_':
                        n += 1
                        new_configuration = copy.deepcopy(configuration)
                        for copied_vehicle in new_configuration:
                            if copied_vehicle.id == vehicle.id:
                                copied_vehicle.y += a 
                                children.append(new_configuration)
        
        #randomvehiclearray = random.choice(children) 
        return children

# https://jeremykun.com/tag/breadth-first-search/

def Random(configuration):
    #create archive & queue
    archive = {}
    short_memory_archive = {}
    counter = 0
    queue = deque([configuration])
    stringStartingConfiguration = ""

    # create string of starting configuration for archive
    for vehicles in configuration:
        stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)
        stringStartingConfiguration += stringvehicle
   
    #print stringStartingConfiguration
        
    archive[stringStartingConfiguration] = None
    #short_memory_archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        if counter > 500:
            break
        #print counter
        current_configuration = queue.pop()
        counter += 1
        stringcars = ""
        winning_state = 0
        
        if short_memory_archive.items > 1:
            short_memory_archive.pop
            

        # create string of currently checked configuration
        for vehicles in current_configuration:
            stringvehicle = str(vehicles.id) + str(vehicles.x) + str(vehicles.y) + str(vehicles.orientation)
            if stringvehicle == 'x105H':
                winning_state = 1
            stringcars += stringvehicle
        if winning_state == 1:
            steps_taken = 0
            parent = archive[stringcars]
            while archive[parent] != None:
                i = 0
                child = parent
                parent = archive[parent]
                for bla in child:
                    if parent[i] != child[i] and str.isalpha(parent[i-1]):
                        print "from", child[i-1]+child[i]+child[i+1]+child[i+2], "to", parent[i-1]+parent[i]+parent[i+1]+parent[i+2]
                    elif parent[i] != child[i]:
                        print "from", child[i-2]+child[i-1]+child[i]+child[i+1], "to", parent[i-2]+parent[i-1]+parent[i]+parent[i+1]
                    # update the index
                    i += 1
                # update steps_taken
                steps_taken += 1
            #print "Totaal aantal gezette stappen:", steps_taken
            print "Totaal aantal bezochte configuraties:", counter
            return counter

        # get_moves yields list of list of objects
        #randomvehiclearray = board.get_moves(current_configuration):
        a = 0
        b = 0
        while a != 1:
            if b > 5:
                break
            children = []
            stringCurrentConfiguration = ""
            children = board.get_moves(current_configuration)
            randomchoice = random.choice(children)
        
            #randomvehiclearray = numpy.random.choice(children)
            for cars in randomchoice:
                stringvehicles = str(cars.id) + str(cars.x) + str(cars.y) + str(cars.orientation)
                stringCurrentConfiguration += stringvehicles

            if (stringCurrentConfiguration not in short_memory_archive):
                queue.appendleft(randomchoice)
                archive[stringCurrentConfiguration] = stringcars
                short_memory_archive[stringCurrentConfiguration] = None
                a = 1
                b = 0
            else:
                #randomchoice = random.choice(children)
                #short_memory_archive[stringCurrentConfiguration] = None
                b += 1
            
                #print stringCurrentConfiguration
        
                    
                
                
            
            

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
        board = Board(12,12, configuration)
        print board
        
        results = []
        # run algorithme
        for i in range(0, 1000):
            print "iteration: ", i
            results.append(Random(configuration))
            print sorted(results)
        
