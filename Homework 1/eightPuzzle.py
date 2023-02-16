from informedSearch import *
from pq import *

Goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
A = [1, 3, 0, 8, 2, 4, 7, 6, 5]
B = [1, 3, 4, 8, 6, 2, 0, 7, 5]
C = [0, 1, 3, 4, 2, 5, 8, 7, 6]
D = [7, 1, 2, 8, 0, 3, 6, 5, 4]
E = [8, 1, 2, 7, 0, 4, 6, 5, 3]
F = [2, 6, 3, 4, 0, 5, 1, 8, 7]
G = [7, 3, 4, 6, 1, 5, 8, 0, 2]
H = [7, 4, 5, 6, 0, 3, 8, 1, 2]


class EightPuzzle():
    def state(self, IncomingArray):
        for index in range(0..IncomingArray.length()):
            print(IncomingArray.at(index))


TestObj = EightPuzzle()
TestObj.state(A)
