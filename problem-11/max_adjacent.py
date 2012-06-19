"""Finds the maximum product of adjacent numbers."""

from operator import mul

def _load_grid(file_name):
    """Loads a grid of numbers from a file.

    Args:
        file_name - Name of the grid file.

    Returns:
        List of lists of ints.
    """
    grid = list()
    with open(file_name, 'r') as grid_file:
        for line in grid_file:
            gridLine = list()
            for n in line.split(' '):
                gridLine.append(int(n))
            grid.append(gridLine)
    return grid

def find_max_adjacent(grid, agg, num):
    """Finds the maximum set of adjacent (including diagonals) numbers
    determined by the aggregator function.

    Args:
        grid - List of lists of numbers
        agg - Aggregator function to maximize
        num - Number of sequential numbers to test.

    Returns:
        Maximum number.
    """
    dp_grid = [[0 for i in xrange(len(grid[0]))] 
               for j in xrange(len(grid))]

    for i in xrange(len(dp_grid)):
        for j in xrange(len(dp_grid[0])):
            max_up = 0 if i == 0 else dp_grid[i-1][j]
            max_left = 0 if j == 0 else dp_grid[i][j-1]
            if j <= len(grid[0]) - num:
                right = reduce(agg, grid[i][j:j+num])
            else:
                right = 0
            if i <= len(grid) - num:
                down_vector = [grid[i+k][j] for k in xrange(num)]
                down = reduce(agg, down_vector)
            else:
                down = 0
            if j <= len(grid[0]) - num and i <= len(grid) - num:
                diag_right_vector = [grid[i+k][j+k] for k in xrange(num)]
                diag_right = reduce(agg, diag_right_vector)
            else:
                diag_right = 0
            if j >= num and i <= len(grid) - num:
                diag_left_vector = [grid[i+k][j-k] for k in xrange(num)]
                diag_left = reduce(agg, diag_left_vector)
            else:
                diag_left = 0
            dp_grid[i][j] = max([max_up, max_left, right, down, diag_right, diag_left])
    for l in dp_grid:
        print l
    return dp_grid[-1][-1]


def main():
    grid = _load_grid('problem-11/grid.txt')
    # NOTE: We could use a lambda function combining sum and checking to see
    # that not all 4 are 0, but this way we can do it in 1 pass. This is far
    # slower than the alternative.
    print find_max_adjacent(grid, mul, 4)

if __name__ == '__main__':
    main()