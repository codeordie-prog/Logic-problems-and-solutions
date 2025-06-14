class ProblemStatement:
    """Climbing Stairs Problem.
    
    Problem: You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Examples:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top:
            1. 1 step + 1 step
            2. 2 steps

        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top:
            1. 1 step + 1 step + 1 step
            2. 1 step + 2 steps
            3. 2 steps + 1 step
    """


class Specifications:
    """Solution specifications for the climbing stairs problem.
    
    Approach 1: Recursion with Memoization
    Steps:
        1. Handle base cases: n = 0, 1, and 2
        2. Initialize a memo dictionary to cache results
        3. Define a helper method climb(idx) that:
           - Returns 1 if idx >= n-1 (reached or exceeded top)
           - Returns cached result if available
           - Recursively calculates paths by taking 1 or 2 steps
           - Caches and returns the sum of both paths

    Approach 2: Dynamic Programming (Bottom-up)
    Steps:
        1. Handle base cases: n = 0, 1, and 2
        2. Initialize a DP table of size n+1
        3. Set initial values for table[0], table[1], and table[2]
        4. For each step i from 3 to n:
           - Calculate table[i] = table[i-1] + table[i-2]
        5. Return the final value table[n]
    """


class EfficiencyAnalysis:
    """Time and space complexity analysis for both approaches.
    
    Recursion with Memoization:
        Time Complexity: O(n)
            - Each state is computed only once due to memoization
            - We have n possible states (0 to n-1)
        Space Complexity: O(n)
            - O(n) for the memo dictionary
            - O(n) for the recursion stack
            - Total: O(n)

    Dynamic Programming (Bottom-up):
        Time Complexity: O(n)
            - Single pass through the array
            - Each computation takes O(1) time
        Space Complexity: O(n)
            - O(n) for the DP table
            - No recursion stack needed
    """


class Pseudocode:
    """Pseudocode for both solution approaches.
    
    Recursion with Memoization:
    FUNCTION climbStairs(n):
        IF n == 0: RETURN 0
        IF n == 1: RETURN 1
        IF n == 2: RETURN 2

        memo = {}
        
        FUNCTION climb(idx):
            IF idx >= n-1:
                RETURN 1
            
            IF idx in memo:
                RETURN memo[idx]
            
            path1 = climb(idx + 1)
            path2 = climb(idx + 2)
            memo[idx] = path1 + path2
            RETURN memo[idx]
        
        RETURN climb(0)

    Dynamic Programming (Bottom-up):
    FUNCTION climbStairs(n):
        IF n == 0: RETURN 0
        IF n == 1: RETURN 1
        IF n == 2: RETURN 2

        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        table[2] = 2

        FOR i IN RANGE(3, n + 1):
            table[i] = table[i-1] + table[i-2]

        RETURN table[n]
    """