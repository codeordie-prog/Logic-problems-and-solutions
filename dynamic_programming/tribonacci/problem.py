class ProblemStatement:
    """The Tribonacci sequence Tn is defined as follows: 
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.

    Examples:
        Input: n = 4
        Output: 4
        Explanation:
            T_3 = 0 + 1 + 1 = 2
            T_4 = 1 + 1 + 2 = 4
        
        Input: n = 25
        Output: 1389537
    """


class Specifications:
    """Solution approaches and implementation details.
    
    Approach 1: Bottom-up Dynamic Programming (Tabulation)
    ----------------
    1. Handle base cases:
       - If n == 0: return 0
       - If n == 1 or n == 2: return 1
    
    2. Create a DP table:
       - Initialize an array of size n + 1
       - Set initial values: table[0] = 0, table[1] = 1, table[2] = 1
    
    3. Fill the table:
       - For each position i from 3 to n:
         table[i] = table[i-1] + table[i-2] + table[i-3]
    
    4. Return the final value:
       - Return table[n]

    Approach 2: Space-Optimized Solution
    ----------------
    1. Handle base cases (same as Approach 1)
    
    2. Use three variables to track the last three numbers:
       - a, b, c = 0, 1, 1
    
    3. Iterate n-2 times:
       - Calculate next number: next_num = a + b + c
       - Update variables: a, b, c = b, c, next_num
    
    4. Return the final value (c)
    """


class EfficiencyHandling:
    """Detailed analysis of time and space complexity.
    
    Approach 1 - Bottom-up DP (Tabulation):
    Time Complexity: O(n)
        - We compute each value in the sequence exactly once
        - Each computation takes O(1) time
        - Total operations: n + 1
    
    Space Complexity: O(n)
        - We store all values from 0 to n in the DP table
        - Space required: n + 1 elements
    
    Approach 2 - Space-Optimized:
    Time Complexity: O(n)
        - Same number of computations as Approach 1
        - Each iteration takes O(1) time
    
    Space Complexity: O(1)
        - We only store three variables regardless of input size
        - Constant extra space
    """


class Pseudocode:
    """Detailed implementation steps for the solution.
    
    Approach 1 - Bottom-up DP
    -------------------------
    FUNCTION tribonacci(n: int) -> int:
        # Handle base cases
        IF n == 0:
            RETURN 0
        IF n <= 2:
            RETURN 1
        
        # Initialize DP table
        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        table[2] = 1
        
        # Fill the table
        FOR i FROM 3 TO n:
            table[i] = table[i-1] + table[i-2] + table[i-3]
        
        RETURN table[n]


    Approach 2 - Space-Optimized
    ---------------------------
    FUNCTION tribonacci(n: int) -> int:
        # Handle base cases
        IF n == 0:
            RETURN 0
        IF n <= 2:
            RETURN 1
        
        # Initialize variables
        a, b, c = 0, 1, 1
        
        # Calculate sequence
        FOR i FROM 3 TO n:
            next_num = a + b + c
            a, b, c = b, c, next_num
        
        RETURN c
    """
    