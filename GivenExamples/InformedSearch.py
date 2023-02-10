from PriorityQueue import *
from PythonSearches import *


class InformedNode(Node):
    # It's a Node that has a heuristic value
    def __init__(self, goal, state, parent, operator, depth):
        """
      It creates a new node with the given state, parent, operator, and depth, and sets the goal to
      the given goal

      :param goal: the goal state
      :param state: the current state of the problem
      :param parent: the node that generated this node
      :param operator: the operator that was applied to the parent node to get this node
      :param depth: the depth of the node in the search tree
      """

        Node.__init__(self, state, parent, operator, depth)
        self.goal = goal

    def priority(self):
        """
      It returns the sum of the depth of the current node and the heuristic value of the current
      state
      :return: The priority of the node.
    """
        return self.depth + self.state.heuristic(self.goal)


class InformedSearch(Search):
    # It's a subclass of Search that implements the A* algorithm
    def __init__(self, initialState, goalState):
        """
      The function takes in the initial state and the goal state and then creates a priority queue and
      adds the goal state to the queue. Then it calls the execute function and if the solution is
      None, it prints "Search failed" and if the solution is not None, it calls the showPath function
      and prints the number of expansions.

      :param initialState: The initial state of the puzzle
      :param goalState: The goal state of the puzzle
    """
        self.expansions = 0
        self.clearVisitedStates()
        self.q = PriorityQueue()
        self.goalState = goalState
        self.q.enqueue(InformedNode(goalState, initialState, None, None, 0))
        solution = self.execute()
        if solution == None:
            print("Search failed")
        else:
            self.showPath(solution)
            print("Expanded", self.expansions, "nodes during search")

    def execute(self):
        """
        While the queue is not empty, dequeue the current node, increment the number of
        expansions, check if the current node is the goal state, if not, apply the operators to the
        current node, and enqueue the new nodes
        :return: The goal node.
        """
        while not self.q.empty():
            current = self.q.dequeue()
            self.expansions += 1
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()
                operators = current.state.operatorNames()
                for i in range(len(successors)):
                    if not successors[i].illegal():
                        n = InformedNode(self.goalState,
                                         successors[i],
                                         current,
                                         operators[i],
                                         current.depth+1)
                        if n.repeatedState():
                            del (n)
                        else:
                            self.q.enqueue(n)
        return None


# It's a ProblemState that has a heuristic function
class InformedProblemState(ProblemState):
    """
    An interface class for problem domains used with informed search.
    """

    def heuristic(self, goal):
        """
        > The heuristic function should return an estimate of the cost of the cheapest path from the current
        state to the goal state

        :param goal: The goal node
        """
        abstract()
