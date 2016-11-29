import sys
#J. vehicles hier algemeen verklaard zodat we er gebruik van kunnen
#J. maken in get_moves, volgensm mij is dit nodig. maar correct me if im wrong
#vehicles = []
new_vehicles = []

# keeps track of the Position of a vehicle
class Position(object):
    def __init__(self, x, y):
        self.x = x
        #print "Position x: " + str(self.x)
        self.y = y
        #print "Position y: " + str(self.y)
    
    # to be able to use x and y in class 
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_new_position(self):
        old_x, old_y = self.get_x(), self.get_y()
        new_x = old_x + 1
        new_y = old_y + 0
        #print "Position new x: " + str(new_x)
        #print "Position new y: " + str(new_y)
        return Position(new_x, new_y)

class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation

        
        if self.id >= 'A' and self.id <= 'G':
            self.length = 2
        elif self.id >= 'O' and self.id <= 'Z':
            self.length = 3

        # self.position = position

        # self.board = board
        #self.pos = self.get_position(x, y)

#==============================================================================
#     def get_position(self, x, y):
#         # x = raw_input("Give me a X coordinate: ")
#         # y = raw_input("Give me an Y coordinate: ")
#         #print x
#         #print y
#         return Position(int(x), int(y))
#==============================================================================

#==============================================================================
#     # this method isn't used yet
#     def get_vehicle_position(self):
#         print "Position: " + self.pos
#         return self.pos
# 
#     def set_vehicle_position(self, position):
#         self.pos = position
#==============================================================================

#==============================================================================
#     def update_position(self):
#         new_position = self.pos.get_new_position()
#         if self.board.is_position_on_board(new_position) == True:
#             # self.set_vehicle_position(new_position)
#             self.pos = new_position
#             print "New vehicle position is on board."
#         else:
#             print "ERROR: new vehicle position is not on board."
#==============================================================================
    
    def get_moves(self):
        board = self.get_board()
        
        for v in self.vehicles:
            # indien horizontaal, kan de auto alleen naar links of rechts bewegen.
            if v.orientation == 'H':
                # Naar links beweeg functie
                # check of er een auto is die op x-1 staat of of het buiten de doos is.
                if v.x -1 >= 0 and board[v.y][v.x - 1] == '_':
                    # naar rechts gaan 
                    # Dit is gedaan door een nieuwe vehicle aan te maken met een andere x coordinaat
                    new_v = Vehicle(v.id, v.x -1, v.y, v.orientation)
                    # deze nieuwe vehicle vervolgens in nieuwe (gecloonde) array plaatsen en oude auto eruit halen.
                    new_vehicles = self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    # we hebben nu dus eigenlijk een kind gemaakt van de oude configuratie, deze kunnen we nu toevoegen aan de queue.
                    # dus wellicht hier dan deze functie oproepen
                    # enqueue.vehicles
                    # Alleen misschien moeten we het eerst nog terug converteren naar een string. misschien omkeren van de code in INIT
                    # Ik heb namelijk een print gemaakt van de vehicle[] array en deze ziet er dan zo uit:
                    # [<__main__.Vehicle object at 0x000000000AE51EB8>, 
                    #<__main__.Vehicle object at 0x000000000B3AA278>, 
                    #<__main__.Vehicle object at 0x000000000B1C8C50>, 
                    #<__main__.Vehicle object at 0x000000000B1C8EF0>]  
                    # Jij een idee Lisa?
                    
                    # is dit een geldige move dan moeten we hem returnen aan breadthfirst en opslaan als kind
                    # alleen wat returnen? Ik denk de nieuwe array new_vehicles
                    yield Vehicle(new_vehicles)
                
                # Naar Rechts beweeg functie
                if v.x + v.length >= 0 and board[v.y][v.x + v.length] == '_':
                    # Dit is gedaan door een nieuwe vehicle aan te maken met een andere x coordinaat
                    new_v = Vehicle(v.id, v.x +1, v.y, v.orientation)
                    # deze nieuwe vehicle vervolgens in nieuwe (gecloonde) array plaatsen en oude auto eruit halen.
                    new_vehicles == self.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.add(new_v)
                    yield Vehicle(new_vehicles)
                
                    
                #indien verticaal alleen omhoog en omlaag bewegen mogelijk.
                if v.orientation == 'V':
                    # omhoog beweeg functie
                    if v.y + v.length >= 0 and board[v.y + v.length][v.x] == '_':
                        # Dit is gedaan door een nieuwe vehicle aan te maken met een andere y coordinaat
                        new_v = Vehicle(v.id, v.x, v.y + 1, v.orientation)
                        # deze nieuwe vehicle vervolgens in nieuwe (gecloonde) array plaatsen en oude auto eruit halen.
                        new_vehicles == self.vehicles.copy()
                        new_vehicles.remove(v)
                        new_vehicles.add(new_v)
                        yield Vehicle(new_vehicles)
                    
                    # omlaag beweeg functie
                    if v.y - 1 >= 0 and board[v.y-1][v.x] == '_':
                    # Dit is gedaan door een nieuwe vehicle aan te maken met een andere y coordinaat
                        new_v = Vehicle(v.id, v.x, v.y - 1, v.orientation)
                        # deze nieuwe vehicle vervolgens in nieuwe (gecloonde) array plaatsen en oude auto eruit halen.
                        new_vehicles == self.vehicles.copy()
                        new_vehicles.remove(v)
                        new_vehicles.add(new_v)
                        yield Vehicle(new_vehicles)


class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        block = ''
        for line in self.get_board():
            block = block + '{0}\n'.format(''.join(line))
        #print block
        return block

#==============================================================================
#     def is_position_on_board(self, pos):
#         checkX = pos.get_x()
#         checkY = pos.get_y()
# 
#         if checkX < 0 or checkX > self.width:
#             return False
#         if checkY < 0 or checkY > self.height:
#             return False
#         else:
#             return True
#==============================================================================

    # we don't need this, just for visualisation
    # J. Ik denk dat we deze wel nodig hebben voor de get_moves om te checken of er een auto staat op de positie
    def get_board(self):
        board = [['_' for w in range(self.width)] for h in range(self.height)]
    
        
        #for vehicle in vehicles:
            #orientation = vehicle.orientation
            
            #if vehicle.id >= 'A' and vehicle.id <= 'G':
                #vehicle.length = 2
            #elif vehicle.id >= 'O' and vehicle.id <= 'Z':
                #vehicle.length = 3
                
        # Voor de nieuwe coordinaten gaat dit dan als volgt worden.
        for vehicle in vehicles:
             orientation = vehicle.orientation
             if vehicle.id >= 'A' and vehicle.id <= 'Z':
                vehicle.length = 2
             elif vehicle.id >= 'a' and vehicle.id <= 'z':
                vehicle.length = 3

             y = vehicle.y
             #print y
             x = vehicle.x
             #print x
             id = vehicle.id
            
            
             if orientation == 'H':
                 for i in range(vehicle.length):
                     board[y][x+i] = id
             else:
                 for i in range(vehicle.length):
                     board[y+i][x] = id
        #print board
        
        return board



#Voorbeeld van hoe een Queue opgezet kan worden in python. Deze link geeft chille voorbeelden van hoe je de functies kan oproepen
# http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# Bij een gevonden configuratie kan bijvoorbeeld gecalld worden configuratie.enqueue en dan zit hij in de queue op de 0 plek.
# bij dequeue wordt dan het laatste item uit de array gepopt, die is tenslotte als eerste toegevoegd. (First in First out)

class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

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
                old_boards[hash(str(new_vehicle))] =  new_vehicle
                
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
                for new_vehicles in Vehicle.get_moves(vehicles):
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
            #print y
            #print type(y)
            x = int(ord(x) - 65)
            # test test, we can leave this out later
            #print "ID: " + id
            #print y
            #print x
            # send the values to class Vehicle and store this is vehicles
            vehicle = Vehicle(id, x, y, orientation)
        
            # store all the vehicle variables in the vehicles array that we just made
            vehicles.append(vehicle)
            
        # make a board of width = 6 and height = 6
        board = Board(6, 6)
        print board
        BreadthFirst(vehicles)
            # pos = Position(x, y)
