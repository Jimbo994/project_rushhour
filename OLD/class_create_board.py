# LISA
import sys
from vehicle import Vehicle

class Board(object):
    def __init__(self, vehicles, width = 6, height = 6):
        # create new board with w = 6, h = 6 and set of vehicle objects.
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
        
        # if there is a car on the board, replace the original '_' with id of vehicle
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
