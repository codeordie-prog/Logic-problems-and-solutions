class ProblemStatement:
    """Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    
    An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
    substrings respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1

    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
    Note: a + b is the concatenation of strings a and b.
    """


class Specifications:
    """Recursion + memoization approach specifications.
    
    Steps:
    1. Assert Length s1 + s2 == s3 ELSE return False
    2. Order must be respected - use pointers i for s1 and j for s2
    3. At any given point, a decision has to be made - EITHER pick from s1 or s2
    4. Decision at any point relies on condition: 
       IF s1[i] == s3[i+j] OR IF s2[j] == s3[i+j]
    5. Store results in a memo to avoid repeated computations
    6. Base case - IF its possible to build s3 from s1 and s2 with respect to order, THEN 
       i == len(s1) and j == len(s2) at some point - This is the base case
    """


class EfficiencyHandling:
    """Efficiency analysis for the solution.
    
    Time Complexity:
        O(n * m) - where n is the length of s3 and m is the number of problems 
        generated from both s1 and s2 - matches found

    Space Complexity:
        O(m * n) - stack space required for recursion
    """


class Pseudocode:
    """Pseudocode for the interleaving string solution.
    
    FUNCTION INTERLEAVE(s1, s2, s3):
        # Check if lengths match
        IF len(s1) + len(s2) != len(s3):
            RETURN False
            
        # Initialize memoization dictionary
        memo = {}
        
        FUNCTION dfs(i, j):
            # Base case - both strings fully processed
            IF i == len(s1) AND j == len(s2):
                RETURN True
                
            # Check memo for existing result
            IF (i, j) in memo:
                RETURN memo[(i, j)]
            
            # Try matching with s1
            match1 = False
            IF i < len(s1) AND s1[i] == s3[i + j]:
                match1 = dfs(i + 1, j)
            
            # Try matching with s2
            match2 = False
            IF j < len(s2) AND s2[j] == s3[i + j]:
                match2 = dfs(i, j + 1)
            
            # Store and return result
            memo[(i, j)] = match1 OR match2
            RETURN memo[(i, j)]
        
        # Start recursion from beginning of both strings
        RETURN dfs(0, 0)
    """
    