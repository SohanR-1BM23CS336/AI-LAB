def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def is_goal(state):
    return state == "123456780"

def manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != '0':
            goal_index = int(tile) - 1
            distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    moves = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}
    zero_index = state.index('0')
    for move, pos_change in moves.items():
        new_index = zero_index + pos_change
        if move == 'Left' and zero_index % 3 == 0:
            continue
        if move == 'Right' and zero_index % 3 == 2:
            continue
        if move == 'Up' and zero_index < 3:
            continue
        if move == 'Down' and zero_index > 5:
            continue
        state_list = list(state)
        state_list[zero_index], state_list[new_index] = state_list[new_index], state_list[zero_index]
        neighbors.append(("".join(state_list), move))
    return neighbors

def ida_star(start_state):
    bound = manhattan_distance(start_state)
    path = [start_state]
    moves = []

    while True:
        t = search(path, moves, 0, bound)
        if t == "FOUND":
            for i, step in enumerate(path):
                print(f"Step {i}:")
                print_state(step)
            print("Moves:", " -> ".join(moves))
            print("Total steps:", len(path) - 1)
            return
        if t == float("inf"):
            print("No solution found!")
            return
        bound = t

def search(path, moves, g, bound):
    state = path[-1]
    f = g + manhattan_distance(state)
    if f > bound:
        return f
    if is_goal(state):
        return "FOUND"
    min_threshold = float("inf")
    for neighbor, move in get_neighbors(state):
        if neighbor not in path:
            path.append(neighbor)
            moves.append(move)
            t = search(path, moves, g + 1, bound)
            if t == "FOUND":
                return "FOUND"
            if t < min_threshold:
                min_threshold = t
            path.pop()
            moves.pop()
    return min_threshold

start = "724506831"
ida_star(start)
