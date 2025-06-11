class ProblemStatement:
    """Calculate the nth Fibonacci number.
    
    The Fibonacci sequence is defined as:
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1
    
    Examples:
        Input: n = 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

        Input: n = 3
        Output: 2
        Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

        Input: n = 4
        Output: 3
        Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
    """


class Specifications:
    """Solution approaches and implementation details.
    
    Two main approaches are provided:

    1. Recursion with Memoization:
        a. Create a memoization dictionary to cache results
        b. Handle base cases: n == 0 returns 0, n == 1 returns 1
        c. Before computing, check if result exists in memo
        d. If not in memo, compute and store the result
        e. Return the computed value

    2. Bottom-up Dynamic Programming (Tabulation):
        a. Handle base cases: n == 0 returns 0, n == 1 returns 1
        b. Create a table of size n+1 to store intermediate results
        c. Initialize table[0] = 0 and table[1] = 1
        d. Iterate from 2 to n, filling each position
        e. Return the final value table[n]
    """


class EfficiencyHandling:
    """Detailed analysis of time and space complexity for each approach.
    
    Time Complexity:
        1. Recursion (without memoization): O(2^n)
           - Each call branches into two subcalls
           - Results in exponential growth of function calls
           - Many redundant calculations

        2. Recursion with Memoization: O(n)
           - Each value is calculated exactly once
           - Subsequent calls use cached results
           - Linear time due to memoization

        3. Bottom-up DP (Tabulation): O(n)
           - Single pass through the array
           - Each value calculated once
           - No redundant calculations

    Space Complexity:
        1. Recursion (without memoization): O(n)
           - Space used by recursion stack
           - Maximum depth of n levels

        2. Recursion with Memoization: O(n)
           - Space for memoization dictionary: O(n)
           - Space for recursion stack: O(n)
           - Total: O(n)

        3. Bottom-up DP (Tabulation): O(n)
           - Space for the table: O(n)
           - No recursion stack needed
           - Can be optimized to O(1) by keeping only last two values
    """


class Pseudocode:
    """Detailed implementation steps for both approaches.
    
    Approach 1: Recursion with Memoization
    -------------------------------------
    FUNCTION fibonacci(n: int) -> int:
        # Initialize memoization dictionary
        memo = {}
        
        FUNCTION fib_helper(n: int) -> int:
            # Base cases
            IF n == 0:
                RETURN 0
            IF n == 1:
                RETURN 1
            
            # Check memo before computing
            IF n in memo:
                RETURN memo[n]
            
            # Compute and store result
            memo[n] = fib_helper(n-1) + fib_helper(n-2)
            RETURN memo[n]
        
        RETURN fib_helper(n)

    Approach 2: Bottom-up Dynamic Programming
    ----------------------------------------
    FUNCTION fibonacci(n: int) -> int:
        # Handle base cases
        IF n == 0:
            RETURN 0
        IF n == 1:
            RETURN 1
        
        # Initialize table
        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        
        # Fill table iteratively
        FOR i IN RANGE(2, n + 1):
            table[i] = table[i-1] + table[i-2]
        
        RETURN table[n]
    """
    