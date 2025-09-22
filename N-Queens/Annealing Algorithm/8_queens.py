# Name: Sohan R
# USN: 1BM23CS336

import random
import math

def calculate_attacks(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                attacks += 1
            if abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_random_neighbor(state):
    n = len(state)
    col = random.randint(0, n - 1)
    row = random.randint(0, n - 1)
    while row == state[col]:
        row = random.randint(0, n - 1)
    new_state = list(state)
    new_state[col] = row
    return tuple(new_state)

def simulated_annealing(n=8, max_iterations=10000, temperature=100.0, cooling_rate=0.99):
    current = tuple(random.randint(0, n - 1) for _ in range(n))
    current_attacks = calculate_attacks(current)
    best = current
    best_attacks = current_attacks

    for _ in range(max_iterations):
        if current_attacks == 0:
            break
        neighbor = get_random_neighbor(current)
        neighbor_attacks = calculate_attacks(neighbor)
        delta = current_attacks - neighbor_attacks
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current, current_attacks = neighbor, neighbor_attacks
            if current_attacks < best_attacks:
                best, best_attacks = current, current_attacks
        temperature *= cooling_rate

    return best, best_attacks

if __name__ == "__main__":
    print("Name: Sohan R")
    print("USN: 1BM23CS336")

    best_state, attacks = simulated_annealing()
    non_attacking = 8 - attacks

    print("Best State:", best_state)
    print("Number of Attacking Pairs:", attacks)
    print("Number of Non-Attacking Queens:", non_attacking)
    if attacks == 0:
        print("Status: Found an optimal solution!")
    else:
        print("Status: Local optimum reached.")
