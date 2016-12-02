import sys
import copy

# array for vehiclestrings, nodig in class Vehicle
new_vehicles = []

# class for vehicles (/ moves?)
class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation



class Board(object):
    def __init__(self, width, height, vehicles):
        self.width = width
        self.height = height
        self.vehicles = vehicles

    #visualisation
    def __str__(self):
        block = ''
        for line in self.get_board(vehicles):
            block = block + '{0}\n'.format(''.join(line))
        return block

    def get_board(self, vehicles):
        board = [['_' for w in range(self.width)] for h in range(self.height)]

        # Voor de nieuwe coordinaten gaat dit dan als volgt worden:
        for vehicle in vehicles:
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

    def get_moves(self, vehicles):
        board = self.get_board(vehicles)

        for v in vehicles:
            # check voor horizontale orientatie
            if v.orientation == 'H':
                # check of auto naar links kan
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe x, die in array te zetten en oude weg te halen
                    new_vehicles = copy.copy(vehicles)
                    for nv in new_vehicles:
                        if nv.id == v.id:
                            nv.x -= 1

                    # print "test1"
                    yield new_vehicles

                # check of auto naar rechts kan
                if v.x + v.length < self.width and board[v.y][v.x + v.length] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe x, die in array te zetten en oude weg te halen
                    new_vehicles = copy.copy(vehicles)
                    for nv in new_vehicles:
                        if nv.id == v.id:
                            nv.x += 1
                    # print "test2"
                    yield new_vehicles

            #indien verticaal alleen omhoog en omlaag bewegen mogelijk.
            if v.orientation == 'V':
                # check of auto omhoog kan
                if v.y - 1 >= 0 and board[v.y - 1][v.x] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe y, die in array te zetten en oude weg te halen
                    new_vehicles = copy.copy(vehicles)
                    for nv in new_vehicles:
                        if nv.id == v.id:
                            nv.y -= 1
                    # print "test3"
                    # print new_v
                    yield new_vehicles

                # check of auto omlaag kan
                if v.y + v.length < self.height and board[v.y + v.length][v.x] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe y, die in array te zetten en oude weg te halen
                    new_vehicles = copy.copy(vehicles)
                    for nv in new_vehicles:
                        if nv.id == v.id:
                            nv.y += 1
                    # print "test4"
                    # print v.y, 'to', new_v.y
                    yield new_vehicles

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

def BreadthFirst(vehicles):
        # Eerst de benodigde dicts aanmaken en de queue
        old_boards = {}
        # De queue begint met de start configuratie, dan moeten hier alle kinderen van gemaakt worden (met get_board) en dan gepopt worden
        Q = Queue()
        #het standaard board toevoegen aan de Queue
        Q.enqueue(vehicles)
        # print "test1"

        # we moeten doorgaan met het algoritme totdat we een oplossing hebben, of tot de Queue leeg is.
        # in iedergeval deze loop dus
        while Q.size() != 0:
            # dan halen we het board uit de Queue
            new_vehicle = Q.dequeue()
            new_array=[]
            # print "test2"
            # als het bord al in de old_boards staat dan doen we er niks mee en gaan we door
            if str(new_array) in old_boards:
                # print "1"
                    continue
            # als we hem nog niet in de old_boards hadden dan moet ie er bij.
            else:
                for vehicle in new_vehicle:
                    new_array = vehicle.id + str(vehicle.y) + str(vehicle.x) + vehicle.orientation
                    print new_array
                    old_boards[new_array] = 0
                #print "New vehicle: " + new_vehicle

            for vehicle in new_vehicle:
                if vehicle.id == 'x' and vehicle.x == 3 and vehicle.y == 5 and vehicle.orientation == 'H':
                    break
                    print "we won!"

                else:
                    board = Board(6, 6, new_vehicle)
                    for new_moves in board.get_moves(new_vehicle):
                        Q.enqueue(new_moves)
                        # print Q.size()

if __name__ == '__main__':
    # filename is second argument given in command line
    filename = sys.argv[1]
    with open(filename) as file:
        # make a new array
        vehicles = []
        for line in file:
            # store a line in variable 'line' but leave the '\n' out
            line = line[:-1]
            # store every value that's in line in id - y - x - orientation
            id, x, y, orientation = line
            # y and x values are letters, convert these to their ascii values (ord) and convert to string (str)
            y = int(ord(y) - 65)
            x = int(ord(x) - 65)
            # send the values to class Vehicle and store this is vehicles
            vehicle = Vehicle(id, x, y, orientation)
            # store all the vehicle variables in the vehicles array that we just made
            vehicles.append(vehicle)

        # make a board of width = x and height = x
        board = Board(6, 6, vehicles)
        print board, '----'
        move = board.get_moves(vehicles)
        list1 =  list(move)
        # print list1[0]

        BreadthFirst(vehicles)
