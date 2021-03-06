import sys, copy
import random
from collections import deque
import os.path
save_path = "C:\Users\Jim\Documents\GitHub\project_rushhour\oplossing_random"

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

def Willekeur(configuration):
    #create archive & queue
    archive = {}
    short_memory_archive = {}
    counter = 0
    steps_taken = 0
    queue = deque([configuration])

    # create string of starting configuration for archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        if counter > 500:
            break
        current_configuration = queue.pop()
        counter += 1

        if short_memory_archive.items > 2:
            short_memory_archive.pop

        # create string of currently checked configuration
        stringCurrentConfiguration = board.get_string(current_configuration)
        if 'x105H' in stringCurrentConfiguration:
            parent = archive[stringCurrentConfiguration]
            
            #als we netjes in een mapje solutions willen schrijven, zie helemaal bovenin voor definieren save_path
            filename = os.path.join(save_path, str(counter) + ".txt")
            f = open(filename, "w")
            f.write("start configuratie: " + stringStartingConfiguration + "\n")
           
            # als we direct in de map willen schrijven
            #f = open("%s.txt" %counter, "w")
            
            # create solution
            while archive[parent] != None:
                #child = parent
                parent = archive[parent]

                
                f.write(parent + "\n")
            

#                 # check string for different position of cars
#                for i in range(len(child)):
#                    if parent[i] != child[i] and str.isalpha(parent[i - 1]):
#                        print "from", child[i - 1:i + 3], "to", parent[i - 1:i + 3]
#                    elif parent[i] != child[i]:
#                        print "from", child[i - 2:i + 2], "to", parent[i - 2:i + 2]
                #update steps_taken
                steps_taken += 1
            print "Totaal aantal bezochte configuraties:", counter
            f.close()
            return counter

        a = 0
        b = 0
        while a != 1:
            if b > 5:
                break
            children = board.get_moves(current_configuration)
            willekeurigkind = random.choice(children)

            stringRandomChild = board.get_string(willekeurigkind)

            if stringRandomChild not in short_memory_archive and stringRandomChild != stringStartingConfiguration:
                queue.appendleft(willekeurigkind)
                archive[stringRandomChild] = stringCurrentConfiguration
                short_memory_archive[stringCurrentConfiguration] = None
                a = 1
                b = 0
            else:
                b += 1

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
        board = Board(12, 12, configuration)
        print board

        results = []
        # run algorithme
        for i in range(0,20000):
            print "Current iteration: ", i
            result = (Willekeur(configuration))
            if result != None:
                results.append(result)
                print sorted(results)
    print sorted(results)
