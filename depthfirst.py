from collections import deque

def DepthFirst(board, configuration):
    #create archive, queue & counters
    archive = {}
    counter = 0
    steps_taken = 0
    max_depth = 50
    stack = deque([configuration])

    # create wincondition
    if board.width == 6:
        wincondition = "x42H"
    elif board.width == 9:
        wincondition == "x74H"
    else:
        wincondition == "x105H"

    # create string of starting configuration for archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None, 0

    while len(stack) > 0:
        current_configuration = stack.pop()
        counter += 1

        # print if the program takes long
        if counter % 50000 == 0:
            print "Still running... Currently checked", counter, "configurations."

        stringCurrentConfiguration = board.get_string(current_configuration)
        depthCurrentConfiguration = archive[stringCurrentConfiguration][1]

        # remove old, already checked boards from archive
        for k, v in archive.items():
            if v[1] > depthCurrentConfiguration:
                del archive[k]

        # check wincondition
        if wincondition in stringCurrentConfiguration:
            parent = archive[stringCurrentConfiguration][0]

            # create solution
            while archive[parent][0] != None:
                child = parent
                parent = archive[parent][0]

                # check string for different position of cars
                for i in range(len(child)):
                    if parent[i] != child[i] and str.isalpha(parent[i - 1]):
                        print "from", child[i - 1:i + 3], "to", parent[i - 1:i + 3]
                    elif parent[i] != child[i]:
                        print "from", child[i - 2:i + 2], "to", parent[i - 2:i + 2]
                # update steps_taken
                steps_taken += 1
            return steps_taken, counter

       # check if we have not exceeded depth yet.
        if depthCurrentConfiguration > max_depth:
            continue
        else:
            # get moves of current configuration
            for children in board.get_moves(current_configuration):
                stringChildConfiguration = board.get_string(children)

                if stringChildConfiguration not in archive:
                    stack.append(children)
                    archive[stringChildConfiguration] = stringCurrentConfiguration, depthCurrentConfiguration + 1
