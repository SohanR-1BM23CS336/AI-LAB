import collections

def get_actions(state):
    actions = []
    room_status = list(state[:4])
    location = state[4] - 1

    if room_status[location] == 1:
        actions.append("Suck")

    if location < 3:
        actions.append("Right")

    if location > 0:
        actions.append("Left")

    return actions

def apply_action(state, action):
    room_status = list(state[:4])
    location = state[4] - 1

    if action == "Suck":
        room_status[location] = 0
    elif action == "Right":
        location += 1
    elif action == "Left":
        location -= 1

    return tuple(room_status + [location + 1])

def solve_vacuum_problem(initial_state):
    queue = collections.deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        if all(room == 0 for room in current_state[:4]):
            print("Goal state reached:", current_state)
            print("Path taken:", path)
            return path

        actions = get_actions(current_state)

        for action in actions:
            next_state = apply_action(current_state, action)
            
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [action]
                queue.append((next_state, new_path))
    
    return None

if __name__ == "__main__":
    initial_state_1 = (1, 1, 1, 1, 1)
    print("Solving for initial state:", initial_state_1)
    solve_vacuum_problem(initial_state_1)

    print("\n" + "="*50 + "\n")

    initial_state_2 = (0, 1, 0, 1, 3)
    print("Solving for initial state:", initial_state_2)
    solve_vacuum_problem(initial_state_2)
