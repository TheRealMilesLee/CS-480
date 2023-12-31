# Xian Wu, 02/22/2023
# Implements the eight puzzle. The node expansions table is at the end of the program.

from informedSearch import *


class EightPuzzle(InformedProblemState):

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __str__(self):
        return str(self.puzzle[0:3]) + "\n" + str(self.puzzle[3:6]) + "\n" + str(self.puzzle[6:9])

    def illegal(self):
        if self.puzzle == 1:
            return 1
        return 0

    def equals(self, state):
        return self.puzzle == state.puzzle

    def up(self):
        empty = self.puzzle.index(0)
        if empty in (0, 1, 2):
            return EightPuzzle(1)
        else:
            newpuzzle = self.puzzle[:]
            newpuzzle[empty] = newpuzzle[empty - 3]
            newpuzzle[empty - 3] = 0
        return EightPuzzle(newpuzzle)

    def down(self):
        empty = self.puzzle.index(0)
        if empty in (6, 7, 8):
            return EightPuzzle(1)
        else:
            newpuzzle = self.puzzle[:]
            newpuzzle[empty] = newpuzzle[empty + 3]
            newpuzzle[empty + 3] = 0
        return EightPuzzle(newpuzzle)

    def left(self):
        empty = self.puzzle.index(0)
        if empty in (0, 3, 6):
            return EightPuzzle(1)
        else:
            newpuzzle = self.puzzle[:]
            newpuzzle[empty] = newpuzzle[empty - 1]
            newpuzzle[empty - 1] = 0
        return EightPuzzle(newpuzzle)

    def right(self):
        empty = self.puzzle.index(0)
        if empty in (2, 5, 8):
            return EightPuzzle(1)
        else:
            newpuzzle = self.puzzle[:]
            newpuzzle[empty] = newpuzzle[empty + 1]
            newpuzzle[empty + 1] = 0
        return EightPuzzle(newpuzzle)

    def operatorNames(self):
        return ["up", "down", "left", "right"]

    def applyOperators(self):
        return [self.up(), self.down(), self.left(), self.right()]

    def manhattan(self, goal):
        distance = 0
        for i in goal.puzzle:
            distance += abs(self.puzzle.index(i) - goal.puzzle.index(i))
        return distance

    def tiles_out_of_place(self, goal):
        distance = 0
        for i in range(9):
            if self.puzzle[i] != goal.puzzle[i]:
                distance += 1
        return distance

    def heuristic(self, goal):
        distance = 0
        # distance = EightPuzzle.tiles_out_of_place(self, goal)
        # distance = EightPuzzle.manhattan(self, goal)
        return distance


goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
# InformedSearch(EightPuzzle([1, 3, 0, 8, 2, 4, 7, 6, 5]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([1, 3, 4, 8, 6, 2, 0, 7, 5]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([0, 1, 3, 4, 2, 5, 8, 7, 6]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([7, 1, 2, 8, 0, 3, 6, 5, 4]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([8, 1, 2, 7, 0, 4, 6, 5, 3]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([2, 6, 3, 4, 0, 5, 1, 8, 7]), EightPuzzle(goal))
# InformedSearch(EightPuzzle([7, 3, 4, 6, 1, 5, 8, 0, 2]), EightPuzzle(goal))
InformedSearch(EightPuzzle([7, 4, 5, 6, 0, 3, 8, 1, 2]), EightPuzzle(goal))
# Search(EightPuzzle([7, 4, 5, 6, 0, 3, 8, 1, 2]), EightPuzzle(goal))

"""
        Node Expansions
Problem   BFS       A*(tiles)   A*(dist)
A         7         3           3
B         91        8           7
C         156       19          10
D         690       48          20
E         856       48          20
F         1621      102         17
G         8361      337         38
H         50312     3529        185
"""
