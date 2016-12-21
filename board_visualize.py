from BreadthFirst import Vehicle
from BreadthFirst import Board

from time import sleep

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
                        print "move", parent[i-1], "from", parent[i:i+2], "to", child[i:i+2], '\n'
                    else:
                        print "move", parent[i-2], "from", parent[i-1:i+1], "to", child[i-1:i+1], '\n'

                    print block

                    print "Aantal stappen gezet:", steps_taken
                    steps_taken += 1

                    sleep(1)

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
                        print "Aantal stappen gezet:", steps_taken

                        steps_taken += 1
                        sleep(1)

                    children -= 1

        last_child = child_array[len(child_array) - 1]
        first_child = parent_array[0]
        print "FIRST", first_child
        print "LAST", last_child
