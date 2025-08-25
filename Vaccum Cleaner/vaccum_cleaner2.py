def vacuum_simulator():
    # Get initial status of rooms
    rooms = {}
    for room in ['A', 'B']:
        while True:
            status = input(f"Enter status of room {room} (C for clean, D for dirty): ").strip().upper()
            if status in ['C', 'D']:
                rooms[room] = status
                break
            else:
                print("Invalid input. Please enter 'C' or 'D'.")

    total_cost = 0

    while True:
        # Check if all rooms are clean
        if all(status == 'C' for status in rooms.values()):
            print("All rooms are clean. Exiting.")
            break

        move = input("Which room to move to? (A or B): ").strip().upper()
        if move not in rooms:
            print("Invalid room. Please enter 'A' or 'B'.")
            continue

        total_cost += 1

        if rooms[move] == 'C':
            print(f"Room {move} is clean. Continuing...")
        else:
            print(f"Room {move} is dirty. Cleaning now.")
            rooms[move] = 'C'

    print(f"Total cost of moves: {total_cost}")

vacuum_simulator()
