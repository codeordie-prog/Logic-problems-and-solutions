class ProblemStatement:
    """You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
    right at any point in time.

    An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square 
    that is an obstacle.

    Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

    Examples:
        Input: grid = [[0,0,0],[0,1,0],[0,0,0]]
        Output: 2
        Explanation: There is one obstacle in the middle of the 3x3 grid above.
        There are two paths to the bottom-right corner:
        1. Right -> Right -> Down -> Down
        2. Down -> Down -> Right -> Right

        Input: grid = [[0,1],[0,0]]
        Output: 1
    """


class Specifications:
    """Solution approaches and implementation details.
    
    Approach 1: Recursion with Memoization
    ----------------
    1. Edge Cases:
       - If the target cell (bottom-right) is an obstacle, return 0
       - If the starting cell is an obstacle, return 0
    
    2. Base Cases:
       - If we reach the target cell (i == rows-1 and j == cols-1), return 1
       - If we go out of bounds (i >= rows or j >= cols), return 0
       - If we hit an obstacle (grid[i][j] == 1), return 0
    
    3. Recursive Cases:
       - Try moving right: move(i, j+1)
       - Try moving down: move(i+1, j)
       - Sum the results from both paths
    
    4. Memoization:
       - Cache results for each cell (i,j) to avoid recalculating
       - Use a dictionary to store computed paths for each position
    """


class EfficiencyHandling:
    """Detailed analysis of time and space complexity.
    
    Approach 1 - Recursion with Memoization:
    Time Complexity: O(m * n)
        - Each cell in the grid is visited exactly once
        - With memoization, we avoid recalculating paths
        - Total number of unique states: m * n
        - Each state calculation takes O(1) time
    
    Space Complexity: O(m * n)
        - Memoization cache stores results for each cell
        - Maximum number of entries in cache: m * n
        - Recursion stack depth: O(m + n) in worst case
        - Total space: O(m * n) for cache + O(m + n) for stack
    
    Without Memoization:
    Time Complexity: O(2^(m+n))
        - Each cell has two choices (right or down)
        - Without caching, we recalculate paths multiple times
        - Leads to exponential growth in calculations
    """


class Pseudocode:
    """Detailed implementation steps for the solution.
    
    Approach 1 - Recursion with Memoization
    --------------------------------------
    FUNCTION unique_paths(grid: list[list[int]]) -> int:
        # Check if target is reachable
        IF grid[-1][-1] == 1:
            RETURN 0
        
        # Initialize dimensions and memoization cache
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}
        
        FUNCTION move(i: int, j: int) -> int:
            # Base cases
            IF i == ROWS-1 AND j == COLS-1:
                RETURN 1  # Reached target
            
            IF i >= ROWS OR j >= COLS:
                RETURN 0  # Out of bounds
            
            IF grid[i][j] == 1:
                RETURN 0  # Hit obstacle
            
            # Check memoization cache
            IF (i,j) IN memo:
                RETURN memo[(i,j)]
            
            # Try both directions and cache result
            right_paths = move(i, j+1)
            down_paths = move(i+1, j)
            
            memo[(i,j)] = right_paths + down_paths
            RETURN memo[(i,j)]
        
        RETURN move(0, 0)
    """

  
    