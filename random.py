import random
from collections import deque

def Willekeur(board, configuration):
    #create archive & queue
    archive = {}
    short_memory_archive = {}
    counter = 0
    steps_taken = 0
    queue = deque([configuration])

    # create wincondition
    if board.width == 6:
        wincondition = "x42H"
    elif board.width == 9:
        wincondition == "x74H"
    elif board.width == 12:
        wincondition == "x105H"

    # create string of starting configuration for archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        if counter > 200:
            break
        current_configuration = queue.pop()
        counter += 1

        if short_memory_archive.items > 2:
            short_memory_archive.pop

        # create string of currently checked configuration
        stringCurrentConfiguration = board.get_string(current_configuration)
        if wincondition in stringCurrentConfiguration:
            parent = archive[stringCurrentConfiguration]

            # create solution
            while archive[parent] != None:
                parent = archive[parent]
                # if you want to check the board found, remove this hash:
                # print parent
                #update steps_taken
                steps_taken += 1
            print "Totaal aantal bezochte configuraties:", counter
            return counter

        a = 0
        b = 0
        while a != 1:
            if b > 5:
                break
            children = board.get_moves(current_configuration)
            willekeurigkind = random.choice(children)

            stringRandomChild = board.get_string(willekeurigkind)

            if stringRandomChild not in short_memory_archive and stringRandomChild != stringStartingConfiguration:
                queue.appendleft(willekeurigkind)
                archive[stringRandomChild] = stringCurrentConfiguration
                short_memory_archive[stringCurrentConfiguration] = None
                a = 1
                b = 0
            else:
                b += 1
