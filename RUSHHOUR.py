import sys
#J. vehicles hier algemeen verklaard zodat we er gebruik van kunnen
#J. maken in get_moves, volgensm mij is dit nodig. maar correct me if im wrong
#vehicles = []

# keeps track of the Position of a vehicle
class Position(object):
    def __init__(self, x, y):
        self.x = x
        print "Position x: " + str(self.x)
        self.y = y
        print "Position y: " + str(self.y)
    
    # to be able to use x and y in class 
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_new_position(self):
        old_x, old_y = self.get_x(), self.get_y()
        new_x = old_x + 1
        new_y = old_y + 0
        print "Position new x: " + str(new_x)
        print "Position new y: " + str(new_y)
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
        self.pos = self.get_position(x, y)

    def get_position(self, x, y):
        # x = raw_input("Give me a X coordinate: ")
        # y = raw_input("Give me an Y coordinate: ")
        print x
        print y
        return Position(int(x), int(y))

    # this method isn't used yet
    def get_vehicle_position(self):
        print "Position: " + self.pos
        return self.pos

    def set_vehicle_position(self, position):
        self.pos = position

    def update_position(self):
        new_position = self.pos.get_new_position()
        if self.board.is_position_on_board(new_position) == True:
            # self.set_vehicle_position(new_position)
            self.pos = new_position
            print "New vehicle position is on board."
        else:
            print "ERROR: new vehicle position is not on board."
    
    #def get_moves(self):
        # deze functie callen om in queue te stoppen?
        #for v in self.vehicles:
            # indien horizontaal, kan de auto alleen naar links of rechts bewegen.
            #if v.orientation == 'H':
                # Naar links beweeg functie
                # check of er een auto is die op x-1 staat of of het buiten de doos is.
                #if v.x -1 >= 0 and v.x - 1 = self.vehicles.x
                    # naar rechts gaan 
                    # Dit is gedaan door een nieuwe vehicle aan te maken met een andere x coordinaat
                    #new_v = Vehicle(v.id, v.x -1, v.y, v.orientation)
                    # deze nieuwe vehicle vervolgens in nieuwe (gecloonde) array plaatsen en oude auto eruit halen.
                    #new_vehicles == self.vehicles
                    #new_vehicles.remove(v)
                    #new_vehicles.add(new_v)
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
                    
                # check of auto op x+1+i staat

                    
            #3if v.orientation == 'V':
                    # check of er een auto is die op x-1 staat
                # naar rechts gaan
                    # check of auto op x+1+i staat

    # algoritme
        # get_moves callen per auto
        # check for board state
        # alle mogelijke moves van een auto
        # moves hier maken 
        # opslaan welke moves er zijn gemaakt met welke auto
            # tuple aanmaken

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

    def is_position_on_board(self, pos):
        checkX = pos.get_x()
        checkY = pos.get_y()

        if checkX < 0 or checkX > self.width:
            return False
        if checkY < 0 or checkY > self.height:
            return False
        else:
            return True

    # we don't need this, just for visualisation
    # J. Ik denk dat we deze wel nodig hebben voor de get_moves om te checken of er een auto staat op de positie
    def get_board(self):
        board = [['_' for x in range(self.width)] for y in range(self.height)]
        print board[1][1]
        
        for vehicle in vehicles:
            orientation = vehicle.orientation
            
            if vehicle.id >= 'A' and vehicle.id <= 'G':
                vehicle.length = 2
            elif vehicle.id >= 'O' and vehicle.id <= 'Z':
                vehicle.length = 3

            vehicle.y = y
            print y
            vehicle.x = x
            print x
            vehicle.id = id
            
            """
            if orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = vehicle.id
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = vehicle.id
        print board
        """
        
        
        return board

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
            print y
            print type(y)
            x = int(ord(x) - 65)
            # test test, we can leave this out later
            print "ID: " + id
            print y
            print x
            # send the values to class Vehicle and store this is vehicles
            vehicle = Vehicle(id, x, y, orientation)
        
            # store all the vehicle variables in the vehicles array that we just made
            vehicles.append(vehicle)
            print vehicles
            #print vehicles
        # make a board of width = 6 and height = 6
        board = Board(20, 20)
        print board
            # pos = Position(x, y)

#Voorbeeld van hoe een Queue opgezet kan worden in python. Deze link geeft chille voorbeelden van hoe je de functies kan oproepen
# http://ice-web.cc.gatech.edu/ce21/1/static/audio/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# Bij een gevonden configuratie kan bijvoorbeeld gecalld worden configuratie.enqueue en dan zit hij in de queue op de 0 plek.
# bij dequeue wordt dan het laatste item uit de array gepopt, die is tenslotte als eerste toegevoegd. (First in First out)

class Queue:
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
        

