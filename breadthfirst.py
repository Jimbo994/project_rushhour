from collections import deque
from datetime import datetime

# https://jeremykun.com/tag/breadth-first-search/
def BreadthFirst(board, configuration):
    #create archive & queue
    archive = {}
    counter = 0
    queue = deque([configuration])

    # create string of starting configuration for archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        current_configuration = queue.pop()
        counter += 1

        # keep counter for long runs :D
        if counter % 50000 == 0:
            print counter, "at:", datetime.now()

        # create string of currently checked configuration
        stringcars = board.get_string(current_configuration)
        if 'x42H' in stringcars:
            steps_taken = 0
            parent = archive[stringcars]

            while archive[parent] != None:
                child = parent
                parent = archive[parent]

                # check string for different position of cars
                for i in range(len(child)):
                    if parent[i] != child[i] and str.isalpha(parent[i - 1]):
                        print "from", child[i - 1:i + 3], "to", parent[i - 1:i + 3]
                    elif parent[i] != child[i]:
                        print "from", child[i - 2:i + 2], "to", parent[i - 2:i + 2]
                # update steps_taken
                steps_taken += 1
            return steps_taken, counter

        # get_moves yields list of list of objects
        for children in board.get_moves(current_configuration):
            stringCurrentConfiguration = board.get_string(children)

            if (stringCurrentConfiguration not in archive):
                queue.appendleft(children)
                archive[stringCurrentConfiguration] = stringcars
