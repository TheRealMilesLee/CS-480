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
    def __init__(self, start_state, goal_state, move_step):
        self.state = start_state
        self.goal = goal_state
        self.move = move_step

    def illegal(self):
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        if (self.move > 1 or col < 0 or row < 0):
            return 1
        return 0

    def equals(self, state):
        return self.state == state.goal

    def findBlank(self):
        for row in range(0, len(self.state)):
            for col in range(0, len(self.state)):
                if (self.state[row][col] == 0):
                    return (row, col)

    def moveLeft(self):
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        self.state[row][col] = self.state[row][col - 1]
        self.state[row][col - 1] = temp

    def moveRight(self):
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        self.state[row][col] = self.state[row][col + 1]
        self.state[row][col + 1] = temp

    def moveUp(self):
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        self.state[row][col] = self.state[row - 1][col]
        self.state[row - 1][col] = temp

    def moveDown(self):
        blankPosition = self.findBlank()
        row = blankPosition[0]
        col = blankPosition[1]
        temp = self.state[row][col]
        self.state[row][col] = self.state[row + 1][col]
        self.state[row + 1][col] = temp

    def operatorNames(self):
        return ["moveDown", "moveUp", "moverLeft", "moveRight"]

    def applyOperators(self):
        return [self.moveDown(), self.moveUp(), self.moveLeft(), self.moveRight()]


Search(EightPuzzle(initial_states[0], goal_state, 1), EightPuzzle(
    goal_state, goal_state, 1))
