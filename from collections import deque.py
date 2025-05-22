from collections import deque

def show(state):
    for row in state:
        print(row)
    print()

def find_zero(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def h(state):
    goal = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    dist = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                dist += 1
    return dist

def solve(start):
    queue = deque()
    queue.append((start, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        goal = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        
        if state == goal:
            return path + [state]

        x, y = find_zero(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                queue.append((new_state, path + [state]))

        queue = deque(sorted(queue, key=lambda x: len(x[1]) + h(x[0])))

    return None

def check_win(state):
    return state == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

def menu(start):
    while True:
        print("\nmenu")
        print("1-move manually")
        print("2-solve automatically using A* ")
        print("3-exit")
        choice = input("enter your choice:  ")

        if choice == "1":
            show(start)
            if check_win(start):
                print("congrats You have solved the puzzle")
                break

            move = input("enter the move (w == up, s == down, a ==left, d == right): ")
            x, y = find_zero(start)
            dx, dy = 0, 0
            if move == "w":
                dx, dy = -1, 0
            elif move == "s":
                dx, dy = 1, 0
            elif move == "a":
                dx, dy = 0, -1
            elif move == "d":
                dx, dy = 0, 1
            else:
                print("invalid move")
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                start[x][y], start[nx][ny] = start[nx][ny], start[x][y]
                print("move done")
                show(start)

                if check_win(start):
                    print("congrats You've solved the game")
                    break
            else:
                print("can't move in that direction")

        elif choice == "2":
            print("running A* to solve")
            result = solve(start)
            if result:
                print("solved in", len(result) - 1, "steps")
                for i, s in enumerate(result[1:]):
                    print("Step", i+1)
                    show(s)
                if check_win(result[-1]):
                    print("puzzle solved successfully")
            else:
                print("no solution found")
            break

        elif choice == "3":
            print("exiting the game")
            break

        else:
            print("Invalid choice")

start = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 0],
    [13, 14, 15, 12]
]
menu(start)