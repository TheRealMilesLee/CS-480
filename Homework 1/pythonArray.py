from informedSearch import *
from pq import *
import copy

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


class EightPuzzle(InformedProblemState):
    def __init__(self, start_state, goal_state):
        """
        > The `__init__` function is called when you create a new instance of the class. It is used to
        initialize the class
        :param start_state: The starting state of the agent
        :param goal_state: The goal state of the agent
        """
        self.state = start_state
        self.goal = goal_state

    def __str__(self):
        """
        It returns a string representation of the state
        :return: The state of the board.
        """
        result = ""
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state[row])):
                if self.state[row][col] == 0:
                    result += " "
                else:
                    result += str(self.state[row][col])
                result += " "
            result += "\n"
        return result

    def illegal(self):
        """
        It checks if the current state is the goal state.
        :return: the number of illegal tiles in the current state.
        """
        BlankSpace = self.findBlank()
        if (BlankSpace == 1):
            return 1
        else:
            return 0

    def equals(self, state):
        # Checking if the current state is the goal state.
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state)):
                if (self.state[row][col] != self.goal[row][col]):
                    return False
        return True

    def findBlank(self):
        """
        It returns the row and column of the blank tile
        :return: The row and column of the blank space.
        """
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state)):
                if (self.state[row][col] == 0):
                    return (row, col)
        return 1

    def moveLeft(self):
        """
        The above function moves the blank tile to the left.
        """
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        if col - 1 > -1:
            self.state[row][col] = self.state[row][col - 1]
            self.state[row][col - 1] = temp
            return EightPuzzle(self.state, self.goal)
        else:
            return EightPuzzle(self.state, self.goal)

    def moveRight(self):
        """
        > The function `moveRight` takes a `Puzzle` object as input and returns a new `Puzzle` object with
        the blank moved one space to the right
        """
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        if col + 1 < self.state[row]:
            self.state[row][col] = self.state[row][col + 1]
            self.state[row][col + 1] = temp
            return EightPuzzle(self.state, self.goal)
        else:
            return EightPuzzle(self.state, self.goal)

    def moveUp(self):
        """
        It moves the blank up one row.
        """
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        if row - 1 > -1:
            self.state[row][col] = self.state[row - 1][col]
            self.state[row - 1][col] = temp
            return EightPuzzle(self.state, self.goal)
        else:
            return EightPuzzle(self.state, self.goal)

    def moveDown(self):
        """
        It moves the blank space down one row.
        """
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]

        if row + 1 < len(self.state):
            self.state[row][col] = self.state[row + 1][col]
            self.state[row + 1][col] = temp
            return EightPuzzle(self.state, self.goal)
        else:
            return EightPuzzle(self.state, self.goal)

    def operatorNames(self):
        """
        It returns a list of the names of the operators that the agent can use
        :return: The names of the operators.
        """
        return ["moveDown", "moveUp", "moverLeft", "moveRight"]

    def applyOperators(self):
        """
        It returns a list of all the possible states that can be reached from the current state
        :return: The return value is a list of the possible moves that can be made.
        """
        return [self.moveDown(), self.moveUp(), self.moveLeft(), self.moveRight()]


def Solver():
    solverObject = EightPuzzle(initial_states[0], goal_state)
    solverPtr = solverObject.state[0][0]
    for row in range(0, len(solverObject.state)):
        for col in range(0, len(solverObject.state)):
            if (solverObject.state[row][col + 1] == solverObject.goal[row][col]):
                solverObject.moveLeft()
            elif (solverObject.state[row][col - 1] == solverObject.goal[row][col]):
                solverObject.moveRight()
