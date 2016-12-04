import sys
import copy

class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation

# array for vehiclestrings, nodig nog ergens?
new_configuration = []
        
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

        # Voor de nieuwe coordinaten gaat dit dan als volgt worden:
        for vehicle in configuration:
            orientation = vehicle.orientation
            if vehicle.id >= 'A' and vehicle.id <= 'Z' or vehicle.id == '!' or vehicle.id == 'x':
                vehicle.length = 2
            elif vehicle.id >= 'a' and vehicle.id <= 'w':
                vehicle.length = 3

            y = vehicle.y
            x = vehicle.x
            id = vehicle.id

            if orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = id
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = id
        return board

    def get_moves(self, configuration):
        board = self.get_board(configuration)
        
        for v in configuration:
            # kijk of de auto horizontaal kan bewegen
            if v.orientation == 'H':
                # check of auto naar links kan
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == '_':
                    # move de vehicle, door x aan te passen
                    new_configuration = copy.copy(configuration)
                    for nv in new_configuration:
                        if nv.id == v.id:
                            nv.x -= 1
                    yield new_configuration

                # check of auto naar rechts kan
                if v.x + v.length < self.width and board[v.y][v.x + v.length] == '_':
                    # move de vehicle, door x aan te passen
                    new_configuration = copy.copy(configuration)
                    for nv in new_configuration:
                        if nv.id == v.id:
                            nv.x += 1
                    yield new_configuration

            # kijk of de auto verticaal kan bewegen
            if v.orientation == 'V':
                # check of auto omhoog kan
                if v.y - 1 >= 0 and board[v.y - 1][v.x] == '_':
                    # move de vehicle, door y aan te passen
                    new_configuration = copy.copy(configuration)
                    for nv in new_configuration:
                        if nv.id == v.id:
                            nv.y -= 1
                    yield new_configuration

                # check of auto omlaag kan
                if v.y + v.length < self.height and board[v.y + v.length][v.x] == '_':
                    # move de vehicle, door y aan te passen
                    new_configuration = copy.copy(configuration)
                    for nv in new_configuration:
                        if nv.id == v.id:
                            nv.y += 1
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
    # maak archief & queue aan, stop vervolgens startconfiguratie in queue.
    old_boards = {}
    Q = Queue()
    Q.enqueue(configuration)
    
    # zoek naar oplossing door queue, zolang er iets in de queue staat. 
    while Q.size() != 0:
        new_configuration = Q.dequeue()
        new_array = []

>>>>>   NEW ARRAY IS HIER EMPTY!?!?!?!?!?!?!?!?!
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
            id, x, y, orientation = line
            
            # convert y & x to ascii (ord) and then to int
            y = int(ord(y) - 65)
            x = int(ord(x) - 65)
            vehicle = Vehicle(id, x, y, orientation)
            configuration.append(vehicle)

        # make a board of width = x and height = x
        board = Board(6, 6, configuration)
        print board
        
        # start algorithm
        move = board.get_moves(configuration)
        list1 =  list(move)
        BreadthFirst(configuration)
