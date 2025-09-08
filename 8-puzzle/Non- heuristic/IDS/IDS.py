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

def depth_limited_search(state, limit, visited, path):
    if state == GOAL: return path
    if limit == 0: return None
    visited.add(state)
    z = state.index('0')
    for m in ['U','L','R','D']:
        if is_valid_move(z, m):
            ns = apply_move(state, m)
            if ns not in visited:
                r = depth_limited_search(ns, limit - 1, visited, path + m)
                if r is not None: return r
    return None

def iterative_deepening_search(start_state):
    d = 0
    total_visited = set()
    while True:
        visited = set()
        r = depth_limited_search(start_state, d, visited, "")
        total_visited |= visited
        if r is not None:
            return r, len(r), len(total_visited)
        d += 1

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

if __name__ == "__main__":
    start_state = "283164705"
    path, steps, unique_states = iterative_deepening_search(start_state)
    print("Moves to Goal:", path)
    print("Total Steps:", steps)
    print("Unique States Visited:", unique_states)
    replay_and_print(start_state, path)
