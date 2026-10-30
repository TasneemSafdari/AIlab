# missioner and cannibals 
from collections import deque

def solve():

    M = int(input("Enter number of Missionaries: "))
    C = int(input("Enter number of Cannibals: "))
    capacity = int(input("Enter boat capacity: "))

    start = (M, C, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [start])])
    visited = []

    moves = []

    for x in range(capacity + 1):
        for y in range(capacity + 1):
            if 1 <= x + y <= capacity:
                moves.append((x, y))

    while queue:

        state, path = queue.popleft()

        m, c, boat = state

        if state == goal:
            print("\nSolution:")
            for step in path:
                print(step)

            print("\nGOAL ACCOMPLISHED!")
            return

        if state in visited:
            continue

        visited.append(state)

        for x, y in moves:

            if boat == 0:
                new_m = m - x
                new_c = c - y
                new_boat = 1
            else:
                new_m = m + x
                new_c = c + y
                new_boat = 0

            if 0 <= new_m <= M and 0 <= new_c <= C:

                right_m = M - new_m
                right_c = C - new_c

                if (new_m == 0 or new_m >= new_c) and \
                   (right_m == 0 or right_m >= right_c):

                    new_state = (new_m, new_c, new_boat)

                    if new_state not in visited:
                        queue.append((new_state, path + [new_state]))

    print("\nNo solution exists!")

solve()

