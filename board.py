import sys
from vehicle import Vehicle

class RushHour(object):
    def __init__(self, vehicles, width = 6, height = 6):
        """
        Create a new Rush Hour board.

        Arguments:
            vehicles: a set of Vehicle objects.
        """
        self.vehicles = vehicles
        self.width = width
        self.height = height
    
    # make sure the board has an \n at the end of the line
    def __str__(self):
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        return s
    
    # make the board
    def get_board(self):
        # stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
        board = [['_' for x in range(self.width)] for y in range(self.height)]
        
        # if there is a car on the board, replace the '_' with the id of the vehicle
        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            # if the vehicle is placed horizontally
            # store the id of the vehicle on board[y][x]
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = vehicle.id
            # if the vehicle is placed vertically
            else:
                for i in range(vehicle.length):
                    board[y+i][x] = vehicle.id
        return board

def load_file(rushhour_file):
    vehicles = []
    for line in rushhour_file:
        line = line[:-1] if line.endswith('\n') else line
        id, x, y, orientation = line
        vehicles.append(Vehicle(id, int(x), int(y), orientation))
    print RushHour(set(vehicles))
    return RushHour(set(vehicles))

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as rushhour_file:
        rushhour = load_file(rushhour_file)

