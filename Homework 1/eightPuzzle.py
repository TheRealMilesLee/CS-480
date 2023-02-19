from queue import PriorityQueue
import copy


class InformedProblemState:
    def __init__(self, state, goal_state):
        self.state = state
        self.goal_state = goal_state

    def is_goal(self):
        return self.state == self.goal_state


class EightPuzzle(InformedProblemState):
    def __init__(self, state, goal_state):
        super().__init__(state, goal_state)
        self.blank_pos = self.find_blank_pos()

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def heuristic(self):
        """
        It counts the number of tiles that are not in their goal position
        :return: The number of tiles that are not in the correct position.
        """
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal_state[i][j]:
                    count += 1
        return count

    def successors(self):
        """
        It returns a list of all possible states that can be reached from the current state by moving
        the blank tile in any of the four directions
        :return: A list of successor states.
        """
        successors = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_state = copy.deepcopy(self.state)
            row, col = self.blank_pos
            new_row, new_col = row + i, col + j
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                successors.append(EightPuzzle(new_state, self.goal_state))
        return successors

    def find_blank_pos(self):
        """
        It returns the position of the blank tile in the puzzle
        :return: The position of the blank tile.
        """
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)


def a_star_search(initial_state, goal_state):
    """
    It takes an initial state and a goal state, and returns a solution state if one exists, or None if
    it doesn't

    :param initial_state: The initial state of the puzzle
    :param goal_state: The goal state of the puzzle
    :return: The goal state
    """
    start_state = EightPuzzle(initial_state, goal_state)
    queue = PriorityQueue()
    queue.put(start_state)
    visited = set()
    while not queue.empty():
        state = queue.get()
        if state.is_goal():
            return state
        visited.add(str(state.state))
        for successor in state.successors():
            if str(successor.state) not in visited:
                queue.put(successor)
    return None


# Testing the algorithm with different initial states
initial_states = [
    [[1, 3, 0], [8, 2, 4], [7, 6, 5]],  # A
    [[1, 3, 4], [8, 6, 2], [7, 5, 0]],  # B
    [[0, 1, 3], [4, 2, 5], [8, 7, 6]],  # C
    [[7, 1, 2], [8, 0, 3], [6, 5, 4]],  # D
    [[8, 1, 2], [7, 0, 4], [6, 5, 3]],  # E
    [[2, 6, 3], [4, 0, 5], [1, 8, 7]],  # F
    [[7, 3, 4], [6, 1, 5], [8, 0, 2]],  # G
    [[7, 4, 5], [6, 0, 3], [8, 1, 2]],  # H
]

goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

for i, initial_state in enumerate(initial_states):
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    solution = a_star_search(initial_state, goal_state)
    print(f"Initial State {chr(65+i)}: {initial_state}")
    if solution:
        print(f"Solution: {solution.state}")
        print(f"Number of steps: {solution.heuristic()}")
    else:
        print("No solution found!")
