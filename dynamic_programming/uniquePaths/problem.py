class ProblemStatement:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
    The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
    bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

    Example 1:
    Input: m = 3, n = 7
    Output: 28

    Example 2:
    Input: m = 3, n = 2
    Output: 3

    Explanation: 
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
    """


class Specifications:
    METHOD_A = f"""
    1. Movement constraint: The robot can only move either right or down (2 possibilities).
    2. Pointers:
       - i: pointer for m (starts at 0, ends at m-1)
       - j: pointer for n (starts at 0, ends at n-1)
    3. Task: Count the number of unique paths from start (grid[0][0]) to target (grid[m-1][n-1])
    4. Valid path: A path that successfully reaches the target (grid[m-1][n-1])
    5. Invalid path: A path that does not reach the target
    6. Valid path result: Return 1
    7. Invalid path result: Return 0
    8. Valid path condition: Reaching grid[m-1][n-1]
    9. Invalid path condition: Not reaching grid[m-1][n-1]
    10. Target reached condition: Both pointers match target (i == m-1 AND j == n-1)
        Note: We use m-1 and n-1 because pointers are initialized at 0
    11. Out of bounds condition: Going past m-1 OR past n-1
    12. Implementation approach: Use recursion to try both possible movements
    """

    METHOD_B = f"""
    1. Initialize a 2D table of size m x n with all cells set to 0
    2. Base Cases:
       - First row: Set all cells to 1 (only one way to reach each cell - moving right)
       - First column: Set all cells to 1 (only one way to reach each cell - moving down)
    3. For each cell (i,j) where i > 0 and j > 0:
       - Number of paths = paths from top (i-1,j) + paths from left (i,j-1)
    4. Fill the table iteratively:
       - Start from (1,1)
       - Move row by row or column by column
       - Each cell's value depends on its top and left neighbors
    5. The final answer will be in table[m-1][n-1]
    6. Implementation approach: Use tabulation (bottom-up dynamic programming)
    """


class EfficiencyHandling:
    METHOD_A = """
    RECURSION WITH MEMOIZATION

    1. Using recursion to try both possible paths at every recursive call:
       - Worst case: Every point on the grid will be explored (m * n) for every recursive call
       - Time complexity: O(2^(m * n)) - Exponential

    2. With MEMOIZATION:
       - Each point is explored only once
       - Time complexity improves from O(2^(m * n)) to O(m * n)
       - Makes the algorithm significantly more efficient
    """

    METHOD_B = """
    TABULATION (BOTTOM-UP DYNAMIC PROGRAMMING)

    1. Time Complexity: O(m * n)
       - We visit each cell exactly once
       - For each cell, we perform O(1) operations
       - Total operations = m * n

    2. Space Complexity: O(m * n)
       - We maintain a 2D table of size m * n
       - Each cell stores the number of paths to reach it
       - No additional space is needed

    3. Advantages over Recursion with Memoization:
       - No recursion overhead
       - No stack space for recursive calls
       - More straightforward to implement
       - Better cache utilization due to sequential access
    """


class Pseudocode:
    METHOD_A = """
    RECURSION + MEMOIZATION
    
    FUNCTION uniquePaths(m, n):
        initialize memo

        FUNCTION findpaths(i, j):
            # Base case: Valid path
            IF i == m-1 AND j == n-1:
                RETURN 1

            # Invalid path: Out of bounds
            IF i > m-1 OR j > n-1:
                RETURN 0

            # Check if already explored
            IF (i,j) in memo:
                RETURN memo[(i,j)]

            # Explore both possible paths
            path_1 = findpaths(i+1, j)  # Move down
            path_2 = findpaths(i, j+1)  # Move right

            # Store result in memo
            memo[(i,j)] = path_1 + path_2

            RETURN memo[(i,j)]

        # Start exploration from origin
        RETURN findpaths(i=0, j=0)
    """

    METHOD_B = """
    TABULATION (BOTTOM-UP)
    
    FUNCTION uniquePaths(m, n):
        # Initialize table with zeros
        table = 2D array of size m x n filled with 0

        # Set base cases
        FOR i = 0 to m-1:
            table[i][0] = 1  # First column
        FOR j = 0 to n-1:
            table[0][j] = 1  # First row

        # Fill the table
        FOR i = 1 to m-1:
            FOR j = 1 to n-1:
                table[i][j] = table[i-1][j] + table[i][j-1]

        # Return the result
        RETURN table[m-1][n-1]
    """
    