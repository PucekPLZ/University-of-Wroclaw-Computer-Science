N = 9

def printing(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end = " ")
        print()

def isSafe(grid, row, col, num):
    for x in range(N):
        if grid[row][x] == num:
            return False
 
    for x in range(N):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
            
    return True

def solveSudoku(grid, row, col):
    if (row == N - 1 and col == N):
        return True
       
    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    
    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num

            if solveSudoku(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False

def findEmpty(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return (i, j)
            
def solve(grid):
    find = findEmpty(grid)

    if not find:
        yield [row[:] for row in grid]  # Make a copy
        return
        
    row, col = find

    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num          
            yield from solve(grid)
            grid[row][col] = 0   

sudoku = [[0, 0, 0, 0, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 0, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 0, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
for solution in solve(sudoku):
        printing(solution)
        print("")