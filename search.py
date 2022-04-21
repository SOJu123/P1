# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    startState = problem.getStartState()
    stack = Stack()
    stack.push((startState, [])) # push trang thai dau va list chua cac huong di
    visited = []    #list chua cac state can kiem tra
    while not stack.isEmpty():
        deepestState, listOfActions = stack.pop()
        visited.append(deepestState)
        if problem.isGoalState(deepestState):
            return listOfActions # Actions
        successors = problem.getSuccessors(deepestState) #push deepestState vao  successor 
        for nextState, nextAction, cost in successors:
            if nextState not in visited:
                #Dua cac action cu vao listActions
                nextActions = []
                for action in listOfActions:
                    nextActions.append(action) 

                nextActions.append(nextAction)    #Hanh dong toi trang thai moi

                stack.push((nextState, nextActions))

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    startState = problem.getStartState()
    queue = Queue()
    queue.push((startState, [])) # push trang thai dau va list chua cac huong di
    visited = []    #list chua cac state can kiem tra
    while not queue.isEmpty():
        breadthState, listOfActions = queue.pop()
        if breadthState in visited:
            continue
        visited.append(breadthState)
        if problem.isGoalState(breadthState):
            return listOfActions # Actions
        successors = problem.getSuccessors(breadthState) #push breadthState vao  successor 
        for nextState, nextAction, cost in successors:
            if nextState not in visited:
                #Dua cac action cu vao listActions
                nextActions = []
                for action in listOfActions:
                    nextActions.append(action) 

                nextActions.append(nextAction)    #Hanh dong toi trang thai moi

                queue.push((nextState, nextActions))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    startState = problem.getStartState()
    priorityQueue = PriorityQueue()
    priorityQueue.push((startState, [], 0), 0) # push trang thai dau va list chua cac huong di
    visited = []    #list chua cac state can kiem tra
    while not priorityQueue.isEmpty():
        uniformcostState, listOfActions, currentCost = priorityQueue.pop()
        if uniformcostState in visited:
            continue
        visited.append(uniformcostState)
        if problem.isGoalState(uniformcostState):
            return listOfActions # Actions
        successors = problem.getSuccessors(uniformcostState) #push uniformcostState vao  successor 
        for nextState, nextAction, cost in successors:
            if nextState not in visited:
                #Dua cac action cu vao listActions
                nextActions = []
                for action in listOfActions:
                    nextActions.append(action) 

                nextActions.append(nextAction)    #Hanh dong toi trang thai moi

                priorityQueue.push((nextState, nextActions, currentCost + cost), currentCost + cost)

    return []
    
   
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    startState = problem.getStartState()
    priorityQueue = PriorityQueue()
    priorityQueue.push((startState, [], 0), 0 + heuristic(startState, problem)) # push trang thai dau va list chua cac huong di
    visited = []    #list chua cac state can kiem tra
    while not priorityQueue.isEmpty():
        uniformcostState, listOfActions, currentCost = priorityQueue.pop()
        if uniformcostState in visited:
            continue
        visited.append(uniformcostState)
        if problem.isGoalState(uniformcostState):
            return listOfActions # Actions
        successors = problem.getSuccessors(uniformcostState) #push uniformcostState vao  successor 
        for nextState, nextAction, cost in successors:
            if nextState not in visited:
                #Dua cac action cu vao listActions
                nextActions = []
                for action in listOfActions:
                    nextActions.append(action) 

                nextActions.append(nextAction)    #Hanh dong toi trang thai moi

                priorityQueue.push((nextState, nextActions, currentCost + cost), currentCost + cost + heuristic(nextState, problem))

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
