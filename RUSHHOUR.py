import sys

# class to keep track of the position of a vehicle
class position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_new_position(self):
        old_x, old_y = self.get_x(), self.get_y()
        new_x = old_x + 1
        new_y = old_y + 0
        return position(new_x, new_y)

# array for vehiclestrings, nodig in class Vehicle
new_vehicles = []

# class for vehicles (/ moves?)
class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation

    def get_moves(self, vehicles):
        board = self.get_board()

        for v in self.vehicles:
            # check voor horizontale orientatie
            if v.orientation == 'H':
                # check of auto naar links kan
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe x, die in array te zetten en oude weg te halen
                    new_v = Vehicle(v.id, v.x -1, v.y, v.orientation)
                    new_vehicles = vehicles.copy()
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield Vehicle(new_vehicles)

                # check of auto naar rechts kan
                if v.x + v.length >= 0 and board[v.y][v.x + v.length] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe x, die in array te zetten en oude weg te halen
                    new_v = Vehicle(v.id, v.x +1, v.y, v.orientation)
                    new_vehicles == vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield Vehicle(new_vehicles)
                
            #indien verticaal alleen omhoog en omlaag bewegen mogelijk.
            if v.orientation == 'V':
                # check of auto omhoog kan
                if v.y + v.length >= 0 and board[v.y + v.length][v.x] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe y, die in array te zetten en oude weg te halen
                    new_v = Vehicle(v.id, v.x, v.y + 1, v.orientation)
                    new_vehicles == self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield Vehicle(new_vehicles)

                # check of auto omlaag kan
                if v.y - 1 >= 0 and board[v.y-1][v.x] == '_':
                    # move de vehicle, door nieuwe vehicle te maken met nieuwe y, die in array te zetten en oude weg te halen
                    new_v = Vehicle(v.id, v.x, v.y - 1, v.orientation)
                    new_vehicles == self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield Vehicle(new_vehicles)

class Board(object):
    def __init__(self, width, height, vehicles):
        self.width = width
        self.height = height
        self.vehicles = vehicles
    
    #visualisation
    def __str__(self):
        block = ''
        for line in self.get_board():
            block = block + '{0}\n'.format(''.join(line))
        return block

    def get_board(self):
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

# Voorbeeld van hoe een queue opgezet kan worden in python. Deze link geeft chille voorbeelden van hoe je de functies kan oproepen
# http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pythonds/BasicDS/ImplementingaqueueinPython.html
# Bij een gevonden configuratie kan bijvoorbeeld gecalld worden configuratie.enqueue en dan zit hij in de queue op de 0 plek.
# bij dequeue wordt dan het laatste item uit de array gepopt, die is tenslotte als eerste toegevoegd. (First in First out)

class queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop() # KIJK OF WE DIT KUNNEN DEQUE IPV POP? (werkcollege)

    def size(self):
        return len(self.items)

def BreadthFirst(vehicles):
        # Eerst de benodigde dicts aanmaken en de queue
        # Hier wat info over dicts in python https://developmentality.wordpress.com/2012/03/30/three-ways-of-creating-dictionaries-in-python/
        # In ieder geval een dict waar we de gepopte configuraties in opslaan. Maar misschien nog andere, want we willen ook uiteindelijk de route weten.
        old_boards = {}
        # De queue begint met de start configuratie, dan moeten hier alle kinderen van gemaakt worden (met get_board) en dan gepopt worden
        Q = Queue()
        #het standaard board toevoegen aan de Queue
        Q.enqueue(vehicles)
        
        # we moeten doorgaan met het algoritme totdat we een oplossing hebben, of tot de Queue leeg is.
        # in iedergeval deze loop dus
        
        while Q.size != 0:
            # dan halen we het board uit de Queue 
            # maar ik weet dus niet zeker of het slim is om te zeggen dequeue(board) Misschien slimmer om gewoon het item dat het eerste erin is gestopt te poppen.
            # want later in de code enqueun we de moves uit vehicle.get_moves en dan heten ze dus ook move... toch?
            
            new_vehicle = Q.dequeue()
            
            # als het bord al in de old_boards staat dan doen we er niks mee en gaan we door
            if str(new_vehicle) in old_boards:
                continue
            # als we hem nog niet in de old_boards hadden dan moet ie er bij.
            else:
                old_boards[str(new_vehicle)] =  new_vehicle
                
            # Nu checken of het bord al een oplossing is
            # we moeten dus gaan kijken of auto met ID X dan op de juiste positie staat. 
            # alleen die array vehicles[] kunnen we dan niet gebruiken als geldige code.
            # ik zat te denken aan zoiets, maar weet dus niet of als we dat board noemen of dat werkt.
            # even uitzoeken wat de winnend coordinaten ook alweer precies zijn (ik ben lui, het is laat)
            #new_vehicleboard = Board.get_board(new_vehicle)
            #if new_vehicleboard[2][4] == 'X' and new_vehicleboard[2][5] == 'X':
                #print "we won"
                #print new_vehicleboard.__str__            
            # wat misschien ook kan is
            
            if Vehicle('X', 4, 2, 'H') in new_vehicle:
                print "we won"
                break
            
            # deze waardes gelden:
                #vehicle.id = X
                #vehicle.y = winnend y
                #vehicle.x = winnend x
                # dan weten we ook dat we gewonnen hebben.
                # dan hebben we gewonnen
            
            # zo ja zijn we klaar
            
            # zo nee, volgende move halen en daarmee weer dit proces doorlopen.
            # weet eigenlijk niet of dit zo kan
            else:
                for new_vehicles in vehicles.get_moves(vehicles):
                    Q.enqueue(new_vehicles)
            # en dan hier alles
            
            #queue.extendleft((move, new_path) for move in board.moves())
        
        # get_moves callen per auto
        # check for board state
        # alle mogelijke moves van een auto
        # moves hier maken 
        # opslaan welke moves er zijn gemaakt met welke auto
            # tuple aanmaken

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
        print board
        # breadthFirst(vehicles)
            # pos = position(x, y)
