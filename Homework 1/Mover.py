# JIngbo Wang and Hengyi Li
# jw6347 and hl3265

###
###

from search import *


class MoverState(ProblemState):
    def __init__(self, itemA, itemB, itemC, mover):
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
        if self.itemA != "" and self.mover != "":
            if self.itemB == "Big Mouse" and self.itemC == "Cheese":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState("", self.itemB, self.itemC, "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemBCarried(self):
        if self.itemB != "" and self.mover != "":
            return MoverState(self.itemA, "", self.itemC, "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemCCarried(self):
        if self.itemC != "" and self.mover != "":
            if self.itemB == "Big Mouse" and self.itemA == "Elephant":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, "", "")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyMoverCarried(self):
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
        if self.mover == "" and self.itemA == "":
            if self.itemB != "" and self.itemA != "":
                return MoverState("Elephant", self.itemB, self.itemC, "Mover")
            else:
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemBBack(self):
        if self.mover == "" and self.itemB == "":
            return MoverState(self.itemA, "Big Mouse", self.itemC, "Mover")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlyItemCBack(self):
        if self.mover == "" and self.itemC == "":
            if self.itemA == "" and self.itemB == "":
                return MoverState(self.itemA, self.itemB, self.itemC, self.mover)
            else:
                return MoverState(self.itemA, self.itemB, "Cheese", "Mover")
        else:
            return MoverState(self.itemA, self.itemB, self.itemC, self.mover)

    def onlymoverBack(self):
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


Search(MoverState("Elephant", "Big Mouse", "Cheese",
       "Mover"), MoverState("", "", "", ""))
