import sys
import time
import random
from heapq import heappush, heappop
b = 0


def check_correct(state):
    for a in range(0, len(state)):
        for b in range(a + 1, len(state)):
            if state[a] == state[b]:
                return False
            if state[b] == state[a] + abs(b - a) or state[b] == state[a] - abs(b - a):
                return False
    return True


def initial_state(n):
    state = []
    for a in range(0, n):
        state.append(-1)
    return state


def goal_test(state):
    for a in state:
        if a == -1:
            return False
    return True


def get_next_unassigned_var(state):
    for i in range(0, len(state)):
        if state[i] == -1:
            return i


# def get_next_unassigned_var(state):
#     temp = []
#     for i in range(0, len(state)):
#         if state[i] == -1:
#             temp.append(i)
#     return temp[random.randint(0, len(temp) - 1)]


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


def csp(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    heap = list()
    for a in get_sorted_values(state, var):
        heappush(heap, ((random.uniform(0, 1) ** 5) * (abs(a - (len(state) / 2))), a))
    while len(heap) != 0:
        val = heappop(heap)
        new_state = state[:]
        new_state[var] = val[1]
        result = csp(new_state)
        if result is not None:
            return result
    global b
    b += 1
    return None


# def csp(state):
#     if goal_test(state):
#         return state
#     var = get_next_unassigned_var(state)
#     for val in get_sorted_values(state, var):
#         new_state = state[:]
#         new_state[var] = val
#         result = csp(new_state)
#         if result is not None:
#             return result
#     return None


sys.setrecursionlimit(50000)
for a in range(8, 110):
    start = time.perf_counter()
    solved = csp(initial_state(a))
    end = time.perf_counter()
    print(str(a) + " " + str(end - start))
    b = 0
