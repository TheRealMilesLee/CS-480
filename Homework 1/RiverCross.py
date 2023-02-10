# JIngbo Wang
# jw6347

### File pitcher.py
### Implements the water pitcher puzzle for state space search

from search import *

class CrossState(ProblemState):
  def  __init__(self, a, b, c, d, timeA, timeB, timeC, timeD, light, totalTime):

    self.a = a
    self.b = b
    self.c = c
    self.d = d

    self.timeA = timeA
    self.timeB = timeB
    self.timeC = timeC
    self.timeD = timeD
    self.totalTime = totalTime

    self.light = light

  def __str__(self):
    """
    Required method for use with the Search class.
    Returns a string representation of the state.
    """
    if self.totalTime != 0:
      result =  "("+str(self.a)+", "+str(self.b)+", "+str(self.c)+", "+str(self.d)+")\nTotal time: " + str(self.totalTime)
    else:
      result =  "("+str(self.a)+", "+str(self.b)+", "+str(self.c)+", "+str(self.d)+")\nTotal time: " + str(self.totalTime)
    return  result

  def illegal(self):
    """
    Required method for use with the Search class.
    Tests whether the state is illegal.
    """
    if self.timeA <= 0 or self.timeB <= 0 or self.timeC <= 0 or self.timeD <= 0: return 1
    if len(self.a) > 1 or len(self.b) > 1 or len(self.c) > 1 or len(self.d) > 1: return 1
    return 0

  def equals(self, state):
    """
    Required method for use with the Search class.
    Determines whether the state instance and the given
    state are equal.
    """
    return self.a==state.a and self.b==state.b and self.c==state.c and self.d==state.d and self.timeA==state.timeA and self.timeB == state.timeB and self.timeC == state.timeC and self.timeD == state.timeD and self.light == state.light

  def onlyAcross(self):
    totalTime = self.totalTime
    if self.a != "" and self.light == 1:
      totalTime += self.timeA
      return CrossState("", self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def onlyBcross(self):
    totalTime = self.totalTime
    if self.b != "" and self.light == 1:
      totalTime += self.timeB
      return CrossState(self.a, "", self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def onlyCcross(self):
    totalTime = self.totalTime
    if self.c != "" and self.light == 1:
      totalTime += self.timeC
      return CrossState(self.a, self.b, "", self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def onlyDcross(self):
    totalTime = self.totalTime
    if self.d != "" and self.light == 1:
      totalTime += self.timeD
      return CrossState(self.a, self.b, self.c, "", self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)


  def onlyAback(self):
    totalTime = self.totalTime
    if self.a == "" and self.light == 0:
      totalTime += self.timeA
      return CrossState("A", self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def onlyBback(self):
    totalTime = self.totalTime
    if self.b == "" and self.light == 0:
      self.totalTime += self.timeB
      return CrossState(self.a, "B", self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def onlyCback(self):
    totalTime = self.totalTime
    if self.c == "" and self.light == 0:
      self.totalTime += self.timeC
      return CrossState(self.a, self.b, "C", self.d, self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def onlyDback(self):
    totalTime = self.totalTime
    if self.d == "" and self.light == 0:
      totalTime += self.timeD
      return CrossState(self.a, self.b, self.c, "D", self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def AandBcross(self):
    totalTime = self.totalTime
    if self.a != "" and self.b != "" and self.light == 1:
      if self.timeA > self.timeB:
        totalTime += self.timeA
      else:
        totalTime += self.timeB
      return CrossState("", "", self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def AandCcross(self):
    totalTime = self.totalTime
    if self.a != "" and self.c != "" and self.light == 1:
      if self.timeA > self.timeC:
        totalTime += self.timeA
      else:
        totalTime +=self.timeC
      return CrossState("", self.b, "", self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def AandDcross(self):
    totalTime = self.totalTime
    if self.a != "" and self.d != "" and self.light == 1:
      if self.timeA > self.timeD:
        totalTime += self.timeA
      else:
        totalTime +=self.timeD
      return CrossState("", self.b, self.c, "", self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def BandCcross(self):
    totalTime = self.totalTime
    if self.b != "" and self.c != "" and self.light == 1:
      if self.timeB > self.timeC:
        totalTime += self.timeB
      else:
        totalTime +=self.timeC
      return CrossState(self.a, "", "", self.d, self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def BandDcross(self):
    totalTime = self.totalTime
    if self.b !=  "" and self.d != "" and self.light == 1:
      if self.timeB > self.timeD:
        totalTime += self.timeB
      else:
        totalTime +=self.timeD
      return CrossState(self.a, "", self.c, "", self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def CandDcross(self):
    totalTime = self.totalTime
    if self.c != "" and self.d != "" and self.light == 1:
      if self.timeC > self.timeD:
        totalTime += self.timeC
      else:
        totalTime +=self.timeD
      return CrossState(self.a, self.b, "", "", self.timeA, self.timeB, self.timeC, self.timeD, 0, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light,  self.totalTime)

  def AandBback(self):
    totalTime = self.totalTime
    if self.a == "" and self.b == "" and self.light == 0:
      if self.timeA > self.timeB:
        totalTime += self.timeA
      else:
        totalTime +=self.timeB
      return CrossState("A", "B", self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def AandCback(self):
    totalTime = self.totalTime
    if self.a == "" and self.c == "" and self.light == 0:
      if self.timeA > self.timeC:
        totalTime += self.timeA
      else:
        totalTime +=self.timeC
      return CrossState("A", self.b, "C", self.d, self.timeA, self.timeB, self.timeC, self.timeD,1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def AandDback(self):
    totalTime = self.totalTime
    if self.a == "" and self.d == "" and self.light == 0:
      if self.timeA > self.timeD:
        totalTime += self.timeA
      else:
        totalTime +=self.timeD
      return CrossState("A", self.b, self.c, "D",  self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def BandCback(self):
    totalTime = self.totalTime
    if self.b == "" and self.c == "" and self.light == 0:
      if self.timeB > self.timeC:
        totalTime += self.timeB
      else:
        totalTime +=self.timeC
      return CrossState(self.a, "B", "C", self.d, self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def BandDback(self):
    totalTime = self.totalTime
    if self.b == "" and self.d == "" and self.light == 0:
      if self.timeB > self.timeD:
        totalTime += self.timeB
      else:
        totalTime +=self.timeD
      return CrossState(self.a, "B", self.c, "D", self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def CandDback(self):
    totalTime = self.totalTime
    if self.c == "" and self.d == "" and self.light == 0:
      if self.timeC > self.timeD:
        totalTime += self.timeC
      else:
        totalTime +=self.timeD
      return CrossState(self.a, self.b, "C", "D", self.timeA, self.timeB, self.timeC, self.timeD, 1, totalTime)
    else:
      return CrossState(self.a, self.b, self.c, self.d, self.timeA, self.timeB, self.timeC, self.timeD, self.light, self.totalTime)

  def operatorNames(self):
    """
    Required method for use with the Search class.
    Returns a list of the operator names in the
    same order as the applyOperators method.
    """

    return ["onlyAcross", "onlyBcross",
                "onlyCcross", "onlyDcross",
                "onlyAback", "onlyBback",
                "onlyCback", "onlyDback",
                "AandBcross", "AandCcross",
                "AandDcross" , "BandCcross",
                "BandDcross", "CandDcross",
                "AandBback", "AandCback",
                "AandDback", "BandCback",
                "BandDback", "CandDback"]


  def applyOperators(self):
    """
    Required method for use with the Search class.
    Returns a list of possible successors to the current
    state, some of which may be illegal.
    """
    return [self.onlyAcross(), self.onlyBcross(),
            self.onlyCcross(), self.onlyDcross(),
            self.onlyAback(), self.onlyBback(),
            self.onlyCback(), self.onlyDback(),
            self.AandBcross(), self.AandCcross(),
            self.AandDcross(), self.BandCcross(),
            self.BandDcross(),self.CandDcross(),
            self.AandBback(), self.AandCback(),
            self.AandDback(), self.BandCback(),
            self.BandDback(), self.CandDback()]

Search(CrossState("A", "B", "C","D", 1, 2, 5 , 8, 1, 0), CrossState("", "" ,"", "", 1, 2, 5 , 8, 0, 0))


