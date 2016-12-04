import sys
import copy

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

        for vehicle in configuration:
            # move vehicles horizontally
            if vehicle.orientation == 'H':
                # check if vehicle can move left
                if vehicle.x - 1 >= 0 and board[vehicle.y][vehicle.x - 1] == '_':
                    # move vehicle by changing x
                    new_configuration = copy.copy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.x -= 1
                    yield new_configuration

                # check if vehicle can move right
                if vehicle.x + vehicle.length < self.width and board[vehicle.y][vehicle.x + vehicle.length] == '_':
                    # move vehicle by changing x
                    new_configuration = copy.copy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.x += 1
                    yield new_configuration

            # move vehicles vertically
            if vehicle.orientation == 'V':
                # check if vehicle can move up
                if vehicle.y - 1 >= 0 and board[vehicle.y - 1][vehicle.x] == '_':
                    # move vehicle by changing y
                    new_configuration = copy.copy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.y -= 1
                    yield new_configuration

                # check if vehicle can move down
                if vehicle.y + vehicle.length < self.height and board[vehicle.y + vehicle.length][vehicle.x] == '_':
                    # move vehicle by chaning y
                    new_configuration = copy.copy(configuration)
                    for copied_vehicle in new_configuration:
                        if copied_vehicle.id == vehicle.id:
                            copied_vehicle.y += 1
                    yield new_configuration

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# HIER MOET NAAR GEKEKEN WORDEN!!!
def BreadthFirst(configuration):
    # create archive & queue - put configuration in queue
    old_boards = {}
    Q = Queue()
    Q.enqueue(configuration)

    # find solution in queue, as long as there is a queue
    while Q.size() != 0:
        new_configuration = Q.dequeue()
        new_array = []

# >>>>>   NEW ARRAY IS HIER EMPTY!?!?!?!?!?!?!?!?!
        # als configuratie al in archief staat, skip.
        if str(new_array) in old_boards:
                continue

        # anders, opslaan
        else:
            for vehicle in new_vehicle:
                new_array = vehicle.id + str(vehicle.y) + str(vehicle.x) + vehicle.orientation
                print new_array
                old_boards[new_array] = 0

            # check if red car is at winning position, else enqueue children
            for vehicle in new_vehicle:
                if vehicle.id == 'x' and vehicle.x == 3 and vehicle.y == 5 and vehicle.orientation == 'H':
                    break
                    print "We won!"
                else:
                    board = Board(6, 6, new_vehicle)
                    for new_moves in board.get_moves(new_vehicle):
                        Q.enqueue(new_moves)

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

        # check if moves are working
        move = board.get_moves(configuration)
        list1 =  list(move)

        # run our awesome algorithm
#        BreadthFirst(configuration)
