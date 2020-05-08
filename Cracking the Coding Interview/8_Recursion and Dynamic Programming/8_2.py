# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits"
# such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the bottom right.


def Path(grid, r, c):
    if grid is None or grid[0][0] == -1 or grid[-1][-1] == -1:
        print("It's not possible to find a path")
        return None
    if check_path_exist(grid, r, c):
        path = []
        get_path(grid, r-1, c-1, path)
        return path
    else:
        print('There is no path')
        return None


def check_path_exist(grid, r, c):
    grid[0][0] = 1
    # fill first column
    for i in range(1, r):
        if grid[i][0] == -1:
            break
        grid[i][0] = 1
    # fill first row
    for i in range(1, c):
        if grid[0][i] == -1:
            break
        grid[0][i] = 1
    for i in range(1, r):
        for j in range(1, c):
            if grid[i][j] != -1 and (grid[i-1][j] != -1 or grid[i][j-1] != -1):
                grid[i][j] = 1
    if grid[-1][-1] == 1:
        return True
    return False


def get_path(grid, r, c, path):
    if r == 0 and c == 0:
        path.append([0, 0])
        return
    if r == 0:
        path.append([0, c])
        get_path(grid, 0, c-1, path)
    elif c == 0:
        path.append([r, 0])
        get_path(grid, r-1, 0, path)
    else:
        path.append([r, c])
        if grid[r-1][c] == 1:
            get_path(grid, r-1, c, path)
        else:
            get_path(grid, r, c-1, path)


if __name__ == "__main__":
    r = 3
    c = 4
    grid = [[0 for _ in range(c)] for _ in range(r)]
    grid[1][0] = -1
    grid[1][2] = -1
    grid[0][3] = -1
    print(grid)
    path = Path(grid, r, c)
    if path:
        print('Path:', [[i+1, j+1] for [i, j] in path[::-1]])

