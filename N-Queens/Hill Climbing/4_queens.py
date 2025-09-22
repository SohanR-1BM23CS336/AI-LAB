import itertools

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

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(tuple(new_state))
    return neighbors

def hill_climb(initial_state):
    current = initial_state
    current_attacks = calculate_attacks(current)

    print(f"\nStarting Hill Climb from: {current}, Attacks: {current_attacks}")
    while True:
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        neighbor = min(neighbors, key=lambda x: calculate_attacks(x))
        neighbor_attacks = calculate_attacks(neighbor)
        if neighbor_attacks >= current_attacks:
            break
        current, current_attacks = neighbor, neighbor_attacks
        print(f"Move to: {current}, Attacks: {current_attacks}")
    return current, current_attacks

if __name__ == "__main__":
    print("Name: Sohan R")
    print("USN: 1BM23CS336")
    print(f"\nTotal possible states: {4**4} ")

    all_states = itertools.product(range(4), repeat=4)
    for state in all_states:
        print(f"State: {state}, Attacks: {calculate_attacks(state)}")

    state_input = input("\nEnter initial state as 4 numbers separated by space (e.g. 0 1 2 3): ")
    initial_state = tuple(map(int, state_input.strip().split()))

    final_state, final_attacks = hill_climb(initial_state)

    print("\n=== Final Result ===")
    print(f"Final State: {final_state}, Attacks: {final_attacks}")
