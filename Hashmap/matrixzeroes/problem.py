class ProblemStatement:
    """
    Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.
    
    Example:

    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    """


class Specifications:
    """
    Approach 1: Using Additional Storage

    1. Initialize a dictionary to store coordinates of cells to be marked as 0.
    2. Define a flag marker function that stores each cell in the row and column to be marked with 0.
    3. Visit each cell in the grid. If the value is 0, call the flag marker function on it.
    4. Visit all stored cells and set them to 0.

    Approach 2: In-Place Optimization

    This approach avoids using additional storage and is optimized for space:
    1. Use the first column and row as flag markers.
    2. First, record whether the first row and first column have zeros.
    3. Start from column 1, row 1 and hunt for 0. If found, set the first row cell and first column cell to 0.
    4. Revisit cells from column 1 and row 1. If the first cell on that row OR first column is 0, set that cell to 0.
    5. Revisit the first column and first row, handling them with respect to their original states.
    """

class EfficiencyHandling:
    """
    Approach 1:
        - Time Complexity: O(N * M)
        - Space Complexity: O(N + M)

    Approach 2:
        - Time Complexity: O(N * M)
        - Space Complexity: O(1)

    where N is the row count and M is the column count.
    """

class Pseudocode:
    """
    Approach 1: Using Additional Storage

    FUNCTION set_zeroes(grid):
        rows = len(grid)
        cols = len(grid[0])
        store = dict()

        DEF flag(i, j):
            temp_i = 0
            temp_j = 0
            WHILE temp_i < rows:
                store[(temp_i, j)] = 0
                temp_i += 1
            WHILE temp_j < cols:
                store[(i, temp_j)] = 0
                temp_j += 1
            RETURN

        FOR i IN RANGE(rows):
            FOR j IN RANGE(cols):
                IF grid[i][j] == 0:
                    flag(i, j)

        FOR key IN store:
            i = key[0]
            j = key[1]
            grid[i][j] = 0

        RETURN

    Approach 2: In-Place Optimization

    FUNCTION set_zeroes(grid):
        rows = len(grid)
        cols = len(grid[0])

        first_row_has_zeros = ANY(grid[0][j] == 0 FOR j IN RANGE(cols))
        first_col_has_zeros = ANY(grid[i][0] == 0 FOR i IN RANGE(rows))

        FOR i IN RANGE(1, rows):
            FOR j IN RANGE(1, cols):
                IF grid[i][j] == 0:
                    grid[i][0] = 0
                    grid[0][j] = 0

        FOR i IN RANGE(1, rows):
            FOR j IN RANGE(1, cols):
                IF grid[i][0] == 0 OR grid[0][j] == 0:
                    grid[i][j] = 0

        IF first_row_has_zeros:
            FOR j IN RANGE(cols):
                grid[0][j] = 0

        IF first_col_has_zeros:
            FOR i IN RANGE(rows):
                grid[i][0] = 0

        RETURN
    """