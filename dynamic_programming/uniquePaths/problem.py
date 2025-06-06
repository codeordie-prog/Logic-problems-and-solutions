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
    """
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
    TABULATION
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
    