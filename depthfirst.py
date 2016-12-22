from collections import deque

def DepthFirst(board, configuration):
    #create archive, queue & counters
    archive = {}
    counter = 0
    steps_taken = 0
    max_depth = 50
    solution = []
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
            solution.append(stringCurrentConfiguration)

            # create solution
            while archive[parent][0] != None:
                child = parent
                # create solution
                solution.insert(0, parent)
                parent = archive[parent][0]
                steps_taken += 1

            # add first step
            solution.insert(0, parent)
            steps_taken += 1

            # print solution
            for i in range(0, len(solution) - 1):
                string = solution[i]
                for j in range(0, len(string)):
                    if solution[i][j] != solution[i + 1][j]:
                        if str.isalpha(solution[i][j - 1]):
                            print "Move", solution[i + 1][j - 1], "from", solution[i][j] +','+ solution[i][j + 1], "to", solution[i + 1][j] +','+ solution[i + 1][j + 1]
                        else:
                            print "Move", solution[i + 1][j - 2], "from", solution[i][j - 1] +','+ solution[i][j], "to", solution[i + 1][j - 1] +','+ solution[i + 1][j]
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
