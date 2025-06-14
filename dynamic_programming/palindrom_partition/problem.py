class ProblemStatement:
    """Palindrome Partitioning Problem.
    
    Problem: Given a string s, partition s such that every substring of the partition
    is a palindrome. Return all possible palindrome partitioning of s.
    
    Examples:
        Input: s = "aab"
        Output: [["a","a","b"], ["aa","b"]]
        Explanation: The string "aab" can be partitioned in two ways:
            1. ["a","a","b"] - each substring is a palindrome
            2. ["aa","b"] - "aa" is a palindrome, "b" is a palindrome

        Input: s = "a"
        Output: [["a"]]
        Explanation: The string "a" is already a palindrome, so it forms a single partition.
    """


class Specifications:
    """Solution specifications for the palindrome partitioning problem.
    
    Approach: Depth-First Search (DFS) with Memoization
    
    Steps:
        1. For each position in the string:
           a. Check if the prefix from current position is a palindrome
           b. If it is a palindrome:
              - Recursively find all valid partitions for the remaining suffix
              - Combine the current palindrome with each valid suffix partition
           c. Continue until we reach the end of the string
        
        2. Memoization:
           - Cache results for each starting position to avoid redundant calculations
           - Store all valid partitions for each position
        
        3. Base Cases:
           - Empty string: return [[]] (empty partition)
           - Single character: return [[char]] (single partition)
    """


class EfficiencyAnalysis:
    """Time and space complexity analysis for the solution.
    
    Time Complexity: O(n * 2^n)
        - In worst case, we have 2^n possible partitions
        - For each partition, we need O(n) time to check if it's a palindrome
        - Memoization helps avoid redundant calculations but doesn't change the worst case
    
    Space Complexity: O(n * 2^n)
        - We need to store all possible partitions
        - Each partition can be up to n elements long
        - The memoization cache stores results for each position
    
    Where n is the length of the input string.
    """


class Pseudocode:
    """Pseudocode for the palindrome partitioning solution.
    
    FUNCTION partition(s: str) -> List[List[str]]:
        # Base case: single character
        IF len(s) == 1:
            RETURN [[s]]
        
        # Initialize memoization cache
        memo: Dict[int, List[List[str]]] = {}
        
        FUNCTION is_palindrome(s: str) -> bool:
            RETURN s == s[::-1]
        
        FUNCTION dfs(start: int) -> List[List[str]]:
            
            # Base case: reached end of string
            IF start >= len(s):
                RETURN [[]]
            
            # Return cached result if available
            IF start in memo:
                RETURN memo[start]
            
            results: List[List[str]] = []
            
            # Try all possible end positions
            FOR end IN RANGE(start + 1, len(s) + 1):
                prefix: str = s[start:end]
                
                # If prefix is a palindrome, recursively find partitions for suffix
                IF is_palindrome(prefix):
                    FOR suffix_partition IN dfs(end):
                        results.append([prefix] + suffix_partition)
            
            # Cache and return results
            memo[start] = results
            RETURN results
        
        RETURN dfs(0)
    """