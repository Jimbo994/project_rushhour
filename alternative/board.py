import sys
import time
import rushhour_visualize
from vehicle import Vehicle

class RushHour(object):
    """A configuration of a single Rush Hour board."""

    def __init__(self, vehicles, width = 6, height = 6):
        """
        Create a new Rush Hour board.

        Arguments:
            vehicles: a set of Vehicle objects.
        """
        self.vehicles = vehicles
        self.width = width
        self.height = height

    def __str__(self):
        s = '_' * 8 + '\n'
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        s += '_' * 8 + '\n'
        print "Welcome to RUSH HOUR"
        time.sleep(2)
        # print s
        return s

    def get_board(self):
        """
        Representation of the Rush Hour board as a 2D list of strings
        """
        # stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
        board = [['_' for x in range(self.width)] for y in range(self.height)]

        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x+i] = vehicle.id
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

# def runSimulation(width, height):
#         anim = rushhour_visualize.BoardVisualization(width, height)
#         anim.done()
#
# runSimulation(6,6)
