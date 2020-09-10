from heapq import heappop, heappush
import random
import time
pop_size = 150
board_size = 8


# tests how close the current board is to being solved, with a lower fitness value
# meaning closer to a solved board
def fitness(state):
    fit = 0
    for a in range(0, len(state)):
        for b in range(a + 1, len(state)):
            if state[a] == state[b]:
                fit += 1
            if state[b] == state[a] + (b - a) or state[b] == state[a] - (b - a):
                fit += 1
    return fit


def generate():
    old_gen = list()
    gen = 0
    for a in range(0, pop_size):
        rand = []
        for b in range(0, board_size):
            rand.append(random.randint(0, board_size - 1))
        f = fitness(rand)
        if f == 0:
            return rand
        heappush(old_gen, (f * (random.uniform(0, 1) ** 5), rand, f))
    # starts off with a population size of pop_size and continues to
    # generate generations of parents and children until solved
    while True:
        new_gen = list()
        gen += 1
        while len(new_gen) < pop_size:
            parent_a = heappop(old_gen)
            parent_b = heappop(old_gen)
            # the parents will generate 2 children, 1 from the first half of parent a + second half of parent b
            # and the other from the first half of parent b + second half of parent a
            crossover = 3
            child_a = parent_a[1][0:crossover] + parent_b[1][crossover:]
            if fitness(child_a) == 0:
                print(gen)
                return child_a
            mutation_a = random.randint(1, 10)
            if mutation_a <= 8:  # mutates the child randomly
                child_a[random.randint(0, board_size - 1)] = random.randint(0, board_size - 1)
                # next is for double mutation, may not be necessary
                if mutation_a <= 4:
                    child_a[random.randint(0, board_size - 1)] = random.randint(0, board_size - 1)
            f_a = fitness(child_a)
            heappush(new_gen, (f_a * (random.uniform(0, 1) ** 5), child_a, f_a))
            child_b = parent_b[1][0:crossover] + parent_a[1][crossover:]
            if fitness(child_b) == 0:
                print(gen)
                return child_b
            mutation_b = random.randint(1, 10)
            if mutation_b <= 8:
                child_b[random.randint(0, board_size - 1)] = random.randint(0, board_size - 1)
                if mutation_b <= 4:
                    child_b[random.randint(0, board_size - 1)] = random.randint(0, board_size - 1)
            f_b = fitness(child_b)
            heappush(new_gen, (f_b * (random.uniform(0, 1) ** 5), child_b, f_b))
            heappush(old_gen, (parent_a[2] * (random.uniform(0, 1) ** 5), parent_a[1], parent_a[2]))
            heappush(old_gen, (parent_b[2] * (random.uniform(0, 1) ** 5), parent_b[1], parent_b[2]))
        old_gen = new_gen  # starts another generation


for a in range(0, 100):
    board_size = a + 8
    start = time.perf_counter()
    b = generate()
    end = time.perf_counter()
    print(str(a + 8) + " " + str(b) + " " + str(end - start))
