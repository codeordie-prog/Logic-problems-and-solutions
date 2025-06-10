from typing import Any, Dict, List, Tuple, Optional


class RecursionPlusMemoizationSolution:
    """Solution using recursion with memoization to check if s3 is an interleaving of s1 and s2."""

    def __init__(self, s1: str, s2: str, s3: str) -> None:
        """Initialize the solution with input strings.
        
        Args:
            s1: First input string
            s2: Second input string
            s3: Target interleaved string
        """
        self.result: bool = self.interleave(s1, s2, s3)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """Return the result when the class instance is called.
        
        Returns:
            bool: True if s3 is an interleaving of s1 and s2, False otherwise
        """
        return self.result
    
    def interleave(self, s1: str, s2: str, s3: str) -> bool:
        """Check if s3 is an interleaving of s1 and s2.
        
        Args:
            s1: First input string
            s2: Second input string
            s3: Target interleaved string
            
        Returns:
            bool: True if s3 is an interleaving of s1 and s2, False otherwise
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo: Dict[Tuple[int, int], bool] = {}
        
        def dfs(i: int, j: int) -> bool:
            """Recursive helper function to check interleaving.
            
            Args:
                i: Current index in s1
                j: Current index in s2
                
            Returns:
                bool: True if valid interleaving found, False otherwise
            """
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            match1: bool = False
            if i < len(s1) and s1[i] == s3[i + j]:
                match1 = dfs(i + 1, j)

            match2: bool = False
            if j < len(s2) and s2[j] == s3[i + j]:
                match2 = dfs(i, j + 1)

            memo[(i, j)] = match1 or match2
            return memo[(i, j)]
    
        return dfs(0, 0)


def main() -> None:
    """Main function to demonstrate the solution."""
    s1: str = "aabcc"
    s2: str = "dbbca"
    s3: str = "aadbbcbcac"

    result: RecursionPlusMemoizationSolution = RecursionPlusMemoizationSolution(s1, s2, s3)
    print(result())


if __name__ == "__main__":
    main()
        
        