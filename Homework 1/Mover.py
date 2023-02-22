# Jingbo Wang and Hengyi Li
# jw6347@truman.edu and hl3265@truman.edu
# Mover problem
from search import *


# It represents a state of the problem, and it provides methods for determining whether the state
# is illegal, whether it is a goal state, and for generating successor states
class MoverState(ProblemState):
    def __init__(self, itemA, itemB, itemC, mover):
        """
        The function takes in three items and a mover, and then sets the items to the items that were
        passed in, and sets the mover to the mover that was passed in

        :param itemA: The first item to be moved
        :param itemB: The item that will be moved
        :param itemC: The item that is being moved
        :param mover: The mover that will be used to move the items
        """
        self.itemA = itemA
        self.itemB = itemB
        self.itemC = itemC
        self.mover = mover

    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "(" + self.itemA + ", " + self.itemB + ", " + self.itemC + ", " + self.mover + ")"

    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if not isinstance(self.itemA, str) or not isinstance(self.itemB, str) or not isinstance(self.itemC, str) or not isinstance(self.mover, str):
            return 1
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.itemA == state.itemA and self.itemB == state.itemB and self.itemC == state.itemC and self.mover == state.mover

    def onlyItemACarried(self):
        """
        If the mover is carrying an item, and the other two items are the Big Mouse and the Cheese, then
        return the current state. Otherwise, return a state where the mover is not carrying anything
        :return: a new MoverState object.
        """
        if self.itemA != "" and self.mover != "":
            if self.itemB == "Big Mouse" and self.itemC == "Cheese":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState("", self.itemB, self.itemC, "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemBCarried(self):
        """
        If item B is being carried, then drop it
        :return: A new MoverState object with the same itemA and itemC, but with itemB and mover set to ""
        """
        if self.itemB != "" and self.mover != "":
            return MoverState(self.itemA, "", self.itemC, "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemCCarried(self):
        """
        If the mover is carrying the itemC and the itemB is a Big Mouse and the itemA is an Elephant, then
        return the current state. Otherwise, return a new state where the mover is not carrying the itemC.
        :return: a new MoverState object.
        """
        if self.itemC != "" and self.mover != "":
            if self.itemB == "Big Mouse" and self.itemA == "Elephant":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, "", "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyMoverCarried(self):
        """
        If the mover is carrying something, then return a new state with the mover carrying the same thing,
        otherwise return a new state with the mover not carrying anything
        :return: a new MoverState object.
        """
        if self.mover != "":
            if self.itemA == "Elephant" and self.itemB == "Big Mouse" and self.itemC == "":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            elif self.itemA == "" and self.itemB == "Big Mouse" and self.itemC == "Cheese":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, self.itemC, "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemABack(self):
        """
        If the mover is empty and itemA is empty, then if itemB is not empty and itemA is not empty, return
        a new MoverState with the mover as Elephant, itemB as the itemB, itemC as the itemC, and mover as
        Mover. Otherwise, return a new MoverState with itemA as the itemA, itemB as the itemB, itemC as the
        itemC, and mover as the mover. Otherwise, return a new MoverState with itemA as the itemA, itemB as
        the itemB, itemC as the itemC, and mover as the mover.
        :return: the state of the mover.
        """
        if self.mover == "" and self.itemA == "":
            if self.itemB != "" and self.itemA != "":
                return MoverState("Elephant", self.itemB, self.itemC, "Mover")
            else:
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemBBack(self):
        """
        If the mover is empty and itemB is empty, then return a new MoverState with itemA, "Big Mouse",
        itemC, and "Mover". Otherwise, return a new MoverState with itemA, itemB, itemC, and mover
        :return: The state of the mover and the items.
        """
        if self.mover == "" and self.itemB == "":
            return MoverState(self.itemA, "Big Mouse", self.itemC, "Mover")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemCBack(self):
        """
        If the mover is not on the boat, and the boat is not on the item C, then if the item A and item B
        are not on the boat, then return the current state, otherwise return the state with the mover on the
        boat and the cheese on the boat
        :return: The return statement is returning the current state of the mover and the items.
        """
        if self.mover == "" and self.itemC == "":
            if self.itemA == "" and self.itemB == "":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, "Cheese", "Mover")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlymoverBack(self):
        """
        If the mover is empty, then if the itemA and itemB are empty, return the same state, or if the itemB
        and itemC are empty, return the same state, otherwise return the state with the mover. If the mover
        is not empty, return the same state
        :return: a new MoverState object.
        """
        if self.mover == "":
            if self.itemA == "" and self.itemB == "":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            elif self.itemB == "" and self.itemC == "":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, self.itemC, "Mover")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """

        return ["onlyItemACarried", "onlyItemBCarried",
                "onlyItemCCarried", "onlyMoverCarried",
                "onlyItemABack", "onlyItemBBack",
                "onlyItemCBack", "onlymoverBack"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.onlyItemACarried(), self.onlyItemBCarried(),
                self.onlyItemCCarried(), self.onlyMoverCarried(),
                self.onlyItemABack(), self.onlyItemBBack(),
                self.onlyItemCBack(), self.onlymoverBack()]


# Using the search class to find the path from the initial state to the goal state.
Search(MoverState("Elephant", "Big Mouse", "Cheese",
       "Mover"), MoverState("", "", "", ""))
