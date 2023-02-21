import heapq

# Define the goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Define the heuristic function


def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j]-1, 3)
                distance += abs(row-i) + abs(col-j)
    return distance

# Define the A* search algorithm
def a_star(initial_state):
    # Define the initial state
    start_node = (heuristic(initial_state), initial_state, 0, None)

    # Define the priority queue
    frontier = []
    heapq.heappush(frontier, start_node)

    # Define the explored set
    explored = set()

    while frontier:
        # Get the node with the smallest f value
        f, state, g, parent = heapq.heappop(frontier)

        # Check if the goal state has been reached
        if state == goal_state:
            path = []
            node = (f, state, g, parent)
            while node:
                path.append(node[1])
                node = node[3]
            return path[::-1]

        # Add the state to the explored set
        explored.add(tuple(map(tuple, state)))

        # Generate the children of the node
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < 3 and 0 <= y < 3:
                            child_state = [row[:] for row in state]
                            child_state[i][j], child_state[x][y] = child_state[x][y], child_state[i][j]
                            if tuple(map(tuple, child_state)) not in explored:
                                child_node = (
                                    heuristic(child_state)+g+1, child_state, g+1, (f, state, g, parent))
                                heapq.heappush(frontier, child_node)

    # If no solution is found, return None
    return None

# Define the informed search algorithm


def informed_search(initial_state, heuristic_func):
    # Define the initial state
    start_node = (heuristic_func(initial_state), initial_state, None)

    # Define the priority queue
    frontier = []
    heapq.heappush(frontier, start_node)

    # Define the explored set
    explored = set()

    while frontier:
        # Get the node with the smallest h value
        h, state, parent = heapq.heappop(frontier)

        # Check if the goal state has been reached
        if state == goal_state:
            path = []
            node = (h, state, parent)
            while node:
                path.append(node[1])
                node = node[2]
            return path[::-1]

        # Add the state to the explored set
        explored.add(tuple(map(tuple, state)))

        # Generate the children of the node
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < 3 and 0 <= y < 3:
                            child_state = [row[:] for row in state]
                            child_state[i][j], child_state[x][y] = child_state[x][y], child_state[i][j]
                            if tuple(map(tuple, child_state)) not in explored:
                                child_node = (heuristic_func(
                                    child_state), child_state, (h, state, parent))
                                heapq.heappush(frontier, child_node)
# If no solution is found, return None
    return None


# Define the initial state
initial_state = [[1, 3, 0], [8, 2, 4], [7, 6, 5]]

# Solve the puzzle using A * search
print("Solution using A* search:")
path = a_star(initial_state)
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")
