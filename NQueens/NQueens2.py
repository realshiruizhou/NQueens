import time


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


def csp(state):
    n = len(state)
    odd = []
    even = []
    for a in range(0, n, 2):
        even.append(a)
    if n % 6 == 2:
        even = swap(even, 0, 1)
        even = swap(even, 2, len(even) - 1)
    for b in range(1, n, 2):
        odd.append(b)
    if n % 6 == 3:
        even = swap(even, 0, len(even) - 2)
        even = swap(even, 1, len(even) - 1)
        odd.remove(1)
        odd.append(1)
    return odd + even


def swap(s, a, b):
    temp = s[a]
    s[a] = s[b]
    s[b] = temp
    return s


a = 10000000
start = time.perf_counter()
solved = csp(initial_state(a))
end = time.perf_counter()
print(str(a) + " " + str(end - start))
a += 1
