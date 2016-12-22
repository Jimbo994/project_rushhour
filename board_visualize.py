from willekeur import Vehicle
from willekeur import Board

from time import sleep
import time

class BoardVisualization:
    """Visualisation for boards"""
    def __init__(self, stringChildConfiguration, archive, board):
        self.stringChildConfiguration = stringChildConfiguration
        self.archive = archive
        self.board = board

        parent = archive[self.stringChildConfiguration]

        child_array = []
        parent_array = []
        z = 0

        steps_taken = 0

        t0 = time.clock()
        print time.clock() - t0, "seconds"

        # create solution
        while archive[parent] != None:
            child = parent
            parent = archive[parent]
            child_array.insert(z, child)
            parent_array.insert(z, parent)
            z+=1

        # check string for different position of cars
        children = len(child_array)-1

        while children >= 0:
            parent = child_array[children]
            child = parent_array[children]

            for i in range(len(child)):
                if parent[i] != child[i]:
                    configuration = []
                    j = 0
                    for something in range(0, len(child), 4):
                        bla = child[j : j + 4]
                        j = j + 4
                        id, x, y, orientation = bla
                        vehicle = Vehicle(id, int(x), int(y), orientation)
                        configuration.append(vehicle)

                    block = ''

                    for line in self.board.get_board(configuration):
                        block = block + '{0}\n'.format(' '.join(line))

                    print("\033[2J")

                    if str.isalpha(parent[i - 1]):
                        print "move", child[i-1], "from", child[i]+','+child[i+1], "to", parent[i]+','+parent[i+1], '\n'
                    else:
                        print "move", child[i-2], "from", child[i-1]+','+child[i], "to", parent[i-1]+','+parent[i], '\n'

                    print block

                    print "Aantal stappen gezet:", steps_taken, '\n'
                    print "Aantal seconden:", time.clock() - t0, '\n'
                    steps_taken += 1

                    sleep(0.6)


                    if children == 0:
                        configuration = []
                        j = 0
                        for something in range(0, len(parent), 4):
                            bla = parent[j : j + 4]
                            j = j + 4
                            id, x, y, orientation = bla
                            vehicle = Vehicle(id, int(x), int(y), orientation)
                            configuration.append(vehicle)

                        block = ''

                        for line in board.get_board(configuration):
                            block = block + '{0}\n'.format(' '.join(line))

                        print("\033[2J")

                        print block
                        print "Aantal stappen gezet:", steps_taken, '\n'
                        print "Aantal seconden:", time.clock() - t0, '\n'

                        steps_taken += 1
                        sleep(0.6)

                    children -= 1
