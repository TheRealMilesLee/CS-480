# Hengyi Li and Jingbo Wang
# jw6347@truman.edu and hl3265@truman.edu
# 8 Puzzle Problem
from informedSearch import *


class EightPuzzle(InformedProblemState):
    def __init__(self, state):
        """
        `__init__` is a special function that is called when an object is created

        :param state: The state of the game
        """
        self.state = state

    def __str__(self):
        """
        The function takes a state and returns a string representation of the state
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

    def illegal(self) -> int:
        """
        If the blank is in the first column, then the move is legal. Otherwise, it's illegal
        :return: the value of the variable move.
        """
        row, col = self.findBlank()
        if (col < 0 or row < 0):
            return 1
        return 0

    def equals(self, other):
        """
        > The function `equals` takes in a `State` object and returns `True` if the state of the current
        object is equal to the state of the `State` object passed in as an argument

        :param other: the other state to compare to
        :return: The state of the node.
        """
        return self.state == other.state

    def findBlank(self):
        """
        It returns the row and column of the blank tile
        :return: The row and column of the blank space.
        """
        blankRow = -1
        blankCol = -1
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state[row])):
                if (self.state[row][col] == 0):
                    blankRow = row
                    blankCol = col
        return blankRow, blankCol

    def moveLeft(self):
        """
        If the blank is not in the leftmost column, then move the blank one column to the left
        :return: The new state of the puzzle after the blank has been moved left.
        """
        row, col = self.findBlank()
        if col - 1 > -1:
            newState = [row[:] for row in self.state]
            blank = self.state[row][col]
            newState[row][col] = newState[row][col - 1]
            newState[row][col - 1] = blank
            return EightPuzzle(newState)
        else:
            return EightPuzzle(self.state)

    def moveRight(self):
        """
        It returns a new EightPuzzle object with the blank moved one space to the right
        :return: The new state of the puzzle after the blank has been moved.
        """
        row, col = self.findBlank()
        if col + 1 < len(self.state[row]):
            newState = [row[:] for row in self.state]
            blank = self.state[row][col]
            newState[row][col] = newState[row][col + 1]
            newState[row][col + 1] = blank
            return EightPuzzle(newState)
        else:
            return EightPuzzle(self.state)

    def moveUp(self):
        """
        If the blank is not in the top row, then move the blank up one row.
        :return: A new EightPuzzle object with the blank moved up one row.
        """
        row, col = self.findBlank()
        if row - 1 > -1:
            blank = self.state[row][col]
            newState = [row[:] for row in self.state]
            newState[row][col] = newState[row - 1][col]
            newState[row - 1][col] = blank
            return EightPuzzle(newState)
        else:
            return EightPuzzle(self.state)

    def moveDown(self):
        """
        It returns a new EightPuzzle object with the blank moved down one row
        :return: The new state of the puzzle.
        """
        row, col = self.findBlank()
        if row + 1 < len(self.state):
            blank = self.state[row][col]
            newState = [row[:] for row in self.state]
            newState[row][col] = newState[row + 1][col]
            newState[row + 1][col] = blank
            return EightPuzzle(newState)
        else:
            return EightPuzzle(self.state)

    def heuristic(self, goal):
        """
        For each tile in the current state, if the tile is not in the same position as the goal state, add 1
        to the count

        :param goal: The goal state of the puzzle
        :return: The number of tiles that are not in the correct position.
        """
        count = 0
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state[row])):
                if (self.state[row][col] != goal.state[row][col]):
                    count += 1
        return count

    def operatorNames(self):
        """
        It returns a list of the names of the operators that the agent can use
        :return: The names of the operators.
        """
        return ["moveDown", "moveUp", "moverLeft", "moveRight"]

    def applyOperators(self):
        """
        It returns a list of all possible states that can be reached from the current state
        :return: A list of the possible moves that can be made.
        """
        return [self.moveDown(), self.moveUp(), self.moveLeft(), self.moveRight()]


# A way to tell if the file is being run as a script or being imported as a module.
if __name__ == '__main__':
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

    for InformSearchIndex in range(0, len(initial_states)):
        print("Inform search Test case: ", chr(65 + InformSearchIndex))
        InformedSearch(EightPuzzle(
            initial_states[InformSearchIndex]), EightPuzzle(goal_state))
        print("##########################")

    for BFSIndex in range(0, len(initial_states)):
        print("BFS Test case: ", chr(65 + BFSIndex))
        Search(EightPuzzle(
            initial_states[BFSIndex]), EightPuzzle(goal_state))
        print("##########################")

#                                     Node Expansions
# Problem             BFS             A*(tiles)           A*(dist)
# A                           2                  2                          3
# B                           6                  6                         11
# C                           8                  8                        24
# D                           10                 10                     48
# E                           10                  10                    48
# F                           12                  12                    102
# G                           15                 15                    337
# H                           20                 20                   3508
