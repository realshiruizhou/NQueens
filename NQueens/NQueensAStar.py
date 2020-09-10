import sys
import time
import random
from heapq import heappush, heappop


# a simple check to see if the n-queens solution is valid
def check_correct(state):
    for a in range(0, len(state)):
        for b in range(a + 1, len(state)):
            if state[a] < 0 or state[a] >= len(state):
                return False
            if state[a] == state[b]:
                return False
            if state[b] == state[a] + abs(b - a) or state[b] == state[a] - abs(b - a):
                return False
    return True


# initializes a blank board of size n
def initial_state(n):
    state = []
    for a in range(0, n):
        state.append(-1)
    return state


# a check to see if the board has any blanks in it
def goal_test(state):
    for a in state:
        if a == -1:
            return False
    return True


# this is where the code does its heavy lifting, as it tries to
# predict the best queen placement for trial
def get_next_unassigned_var(state):
    most_constrained = -1
    amount = float("inf")
    for a in range(0, len(state)):
        if state[a] == -1:
            constraints = len(get_sorted_values(state, a))  # gives the # of other queens that constrain this column
            if constraints < amount:
                # a check to find the most constrained column
                amount = constraints
                most_constrained = a
    return most_constrained


# this method gives the number of available spaces in the column
def get_sorted_values(state, var):
    empty = []
    for a in range(0, len(state)):
        empty.append(a)
    for b in range(0, len(state)):
        if state[b] != -1:
            if state[b] in empty:
                empty.remove(state[b])
            if state[b] + abs(b - var) in empty:
                empty.remove(state[b] + abs(b - var))
            if state[b] - abs(b - var) in empty:
                empty.remove(state[b] - abs(b - var))
    return empty


# here is where the a star algorithm is implemented
def csp(state):
    if goal_test(state):  # checks to see whether current board state is solved
        return state
    var = get_next_unassigned_var(state)
    heap = list()
    for a in get_sorted_values(state, var):
        heappush(heap, (random.uniform(0, 1), a))  # adds a bit of randomness if heuristic ties with previous
    while len(heap) != 0:
        val = heappop(heap)
        new_state = state[:]
        new_state[var] = val[1]  # places the queen on the board
        result = csp(new_state)  # recurs to place more and returns None if no solution
        if result is not None:
            return result
    return None


# for testing the code. N increases by 1 until it takes more than 2 seconds to solve
def test_code():
    print(csp(initial_state(int(sys.argv[1]))))
    solve_time = 0
    size = 8
    while solve_time < 2:
        start = time.perf_counter()
        state = csp(initial_state(size))
        end = time.perf_counter()
        size += 1
        solve_time = end - start
    print("For size %s, the time was %s." % (size, solve_time))


test_code()
