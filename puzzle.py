#9x9 puzzle problem

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve():
    for r in range(9):  #rows 
        for c in range(9): #column 

            if grid[r][c] == 0:  #finding zero if any

                for n in range(1, 10):

                    # Check row
                    if n in grid[r]:
                        continue

                    # Check column
                    found = False
                    for i in range(9):
                        if grid[i][c] == n:
                            found = True

                    if found:
                        continue

                    # Check 3x3 subgrid
                    sr = (r // 3) * 3
                    sc = (c // 3) * 3
                    found = False

                    for i in range(sr, sr + 3):
                        for j in range(sc, sc + 3):
                            if grid[i][j] == n:
                                found = True

                    if found:
                        continue

                    # Place digit
                    grid[r][c] = n

                    if solve():
                        return True

                    # Undo wrong choice
                    grid[r][c] = 0

                return False

    return True


if solve():
    for row in grid:
        print(row)
else:
    print("No solution exists")
