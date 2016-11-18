from vehicle import Vehicle
from board import Board
import sys

def load_file(rushhour_file)

# 
class Main(object):
    # make sure we can use the Vehicle class in Main class 
    # not sure if we'll use the Board class though
    def __init__(self, vehicles, board):
        self.vehicles = vehicles
        self.board = board
    
    # not going to use this, might be handy for now, just to figure out what the program does
    def print_vehicles(self):
        for vehicle in self.vehicles:
            print vehicle.id
    
    # not going to use this in the end, maar gewoon handig
    def clear_screen(self):
        print("\033[2J")
        print("\033[0;0H")

# this function gets called in the function below: board=load_file(rushhour_file)
# it reads all the values from the file
def load_file(rushhour_file):
    # makes an array to store the information about the vehicles
    vehicles = []
    # for every line in the file we'll make sure that
    for line in rushhour_file:
        # store all characters minus 1 because the line ends with ('\n') 
        line = line[:-1] 
        # store the values of one line in respectively the id, x, y and orientation
        id, x, y, orientation = line
        # add these nicely organized values to the Vehicle class
        vehicles.append(Vehicle(id, int(x), int(y), orientation))
    # give these values to the Board class and return
    # when returning it'll all be stored in 'board' (in the function below)
    return Board(set(vehicles))

# just opens the file that's given with userinput
# this function doesn't organize the values of the file on the board
# that's what will happen in the function above: load_file
if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as rushhour_file:
        board = load_file(rushhour_file)
        print board
