GOAL = "123804765"
MOVE_OFFSETS = {'U': -3, 'L': -1, 'R': 1, 'D': 3}

def is_valid_move(z, m):
    if m == 'L' and z % 3 == 0: return False
    if m == 'R' and z % 3 == 2: return False
    if m == 'U' and z < 3: return False
    if m == 'D' and z > 5: return False
    return True

def apply_move(state, m):
    z = state.index('0')
    s = z + MOVE_OFFSETS[m]
    a = list(state)
    a[z], a[s] = a[s], a[z]
    return "".join(a)

def misplaced_tiles(state):
    return sum(1 for i in range(9) if state[i] != '0' and state[i] != GOAL[i])

def ida_star(start):
    bound = misplaced_tiles(start)
    path = [(start, "")]
    visited = set([start])
    total_visited = set()

    def search(path, g, bound):
        state, moves = path[-1]
        f = g + misplaced_tiles(state)
        if f > bound: 
            return f, None
        if state == GOAL: 
            return True, moves
        min_bound = float("inf")
        z = state.index('0')
        for m in ['U','L','R','D']:
            if is_valid_move(z, m):
                new_state = apply_move(state, m)
                if new_state not in {s for s,_ in path}:
                    path.append((new_state, moves + m))
                    total_visited.add(new_state)
                    t, sol = search(path, g+1, bound)
                    if t == True: return True, sol
                    if isinstance(t, int) and t < min_bound: 
                        min_bound = t
                    path.pop()
        return min_bound, None

    while True:
        t, sol = search(path, 0, bound)
        if t == True: 
            return sol, len(sol), len(total_visited)
        if t == float("inf"): 
            return None, 0, len(total_visited)
        bound = t

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])

def replay_and_print(start_state, path):
    print("Steps:")
    print("Step 0:")
    print_board(start_state)
    cur = start_state
    for i, m in enumerate(path, 1):
        cur = apply_move(cur, m)
        print(f"Step {i} ({m}):")
        print_board(cur)

def is_solvable(state):
    s = [int(c) for c in state if c != '0']
    inv = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] > s[j]: inv += 1
    return inv % 2 == 0

if __name__ == "__main__":
    start_state = "283164705"
    path, steps, unique_states = ida_star(start_state)
    print("Moves to Goal:", path)
    print("Total Steps:", steps)
    print("Unique States Visited:", unique_states)
    replay_and_print(start_state, path)
