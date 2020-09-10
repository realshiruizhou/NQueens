import sys
import time
b = 0


def check_correct(state):
    for a in range(0, len(state)):
        for b in range(a + 1, len(state)):
            if state[a] == state[b]:
                return False
            if state[b] == state[a] + abs(b - a) or state[b] == state[a] - abs(b - a):
                return False
        for c in range(a - 1, 0, -1):
            if state[c] == state[a] + abs(c - a) or state[c] == state[a] - abs(c - a):
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
    return state.index(-1)


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


def csp(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = state[:]
        new_state[var] = val
        result = csp(new_state)
        if result is not None:
            return result
    global b
    b += 1
    return None


# sys.setrecursionlimit(50000)
# for a in range(8, 9):
#     start = time.perf_counter()
#     solved = csp(initial_state(a))
#     end = time.perf_counter()
#     print(str(a) + " " + str(end - start))
sys.setrecursionlimit(50000)
for a in range(21, 26):
    solved = csp(initial_state(a))
    print(str(b))
    b = 0
