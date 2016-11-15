from vehicle import Vehicle
from board import Board
import sys

class Main(object):
    def __init__(self, vehicles, board):
        self.vehicles = vehicles
        self.board = board

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print vehicle.id

    def clear_screen(self):
        print("\033[2J")
        print("\033[0;0H")

def load_file(rushhour_file):
    vehicles = []
    for line in rushhour_file:
        line = line[:-1] if line.endswith('\n') else line
        id, x, y, orientation = line
        vehicles.append(Vehicle(id, int(x), int(y), orientation))
    return Board(set(vehicles))

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as rushhour_file:
        board = load_file(rushhour_file)
        print board
