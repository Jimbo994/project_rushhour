from collections import deque

# https://jeremykun.com/tag/breadth-first-search/
def BreadthFirst(board, configuration):
    # create archive, queue & counters
    archive = {}
    counter = 0
    steps_taken = 0
    solution = []
    queue = deque([configuration])

    # create wincondition
    if board.height == 6:
        wincondition = "x42H"
    elif board.height == 9:
        wincondition = "x74H"
    elif board.height == 12:
        wincondition = "x105H"

    # create starting node in archive
    stringStartingConfiguration = board.get_string(configuration)
    archive[stringStartingConfiguration] = None

    while len(queue) > 0:
        current_configuration = queue.pop()
        counter += 1

        # print if the program takes long
        if counter % 50000 == 0:
            print "Still running... Currently checked", counter, "configurations."

        # check win condition
        stringCurrentConfiguration = board.get_string(current_configuration)
        if wincondition in stringCurrentConfiguration:
            parent = archive[stringCurrentConfiguration]
            solution.append(stringCurrentConfiguration)

            # create solution
            while archive[parent] != None:
                child = parent
                # create solution
                solution.insert(0, parent)
                parent = archive[parent]
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
                            print "Move", solution[i + 1][j - 1], "from", solution[i + 1][j] +','+ solution[i + 1][j + 1], "to", solution[i][j] +','+ solution[i][j + 1]
                        else:
                            print "Move", solution[i + 1][j - 2], "from", solution[i + 1][j - 1] +','+ solution[i + 1][j], "to", solution[i][j - 1] +','+ solution[i][j]
            return steps_taken, counter

        # get moves of current configuration
        for children in board.get_moves(current_configuration):
            stringChildConfiguration = board.get_string(children)
            if stringChildConfiguration not in archive:
                queue.appendleft(children)
                archive[stringChildConfiguration] = stringCurrentConfiguration
