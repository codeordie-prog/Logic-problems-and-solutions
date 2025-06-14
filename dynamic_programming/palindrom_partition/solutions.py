from typing import Any, Dict, List


class DFSWithMemoization:
    """Solution using DFS with memoization for palindrome partitioning.
    
    Attributes:
        result (List[List[str]]): All possible palindrome partitions of the input string.
    """
    
    def __init__(self, s: str) -> None:
        """Initialize the solution with the input string.
        
        Args:
            s (str): The input string to partition.
        """
        self.result: List[List[str]] = self.partition(s)

    def __call__(self, *args: Any, **kwargs: Any) -> List[List[str]]:
        """Return the result when the class instance is called.
        
        Returns:
            List[List[str]]: All possible palindrome partitions.
        """
        return self.result
    
    def partition(self, s: str) -> List[List[str]]:
        """Find all possible palindrome partitions of the input string.
        
        Args:
            s (str): The input string to partition.
            
        Returns:
            List[List[str]]: All possible palindrome partitions.
        """
        if len(s) == 1:
            return [[s]]

        memo: Dict[int, List[List[str]]] = {}
        
        def dfs(start: int) -> List[List[str]]:
            """Find all valid partitions starting from position 'start'.
            
            Args:
                start (int): The starting position in the string.
                
            Returns:
                List[List[str]]: All valid partitions from the starting position.
            """
            if start >= len(s):
                return [[]]
            
            if start in memo:
                return memo[start]
            
            result: List[List[str]] = []
            for end in range(start + 1, len(s) + 1):
                prefix: str = s[start:end]
                if prefix[::-1] == prefix:
                    for palindrome in dfs(end):
                        result.append([prefix] + palindrome)

            memo[start] = result
            return result
            
        return dfs(0)


def test_solutions() -> None:
    """Test the palindrome partitioning solution with various inputs."""
    test_cases: List[str] = ["aab", "a", "aa", "aba", "aaa"]
    expected_results: List[List[List[str]]] = [
        [["a", "a", "b"], ["aa", "b"]],
        [["a"]],
        [["a", "a"], ["aa"]],
        [["a", "b", "a"], ["aba"]],
        [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    ]
    
    for s, expected in zip(test_cases, expected_results):
        result: List[List[str]] = DFSWithMemoization(s)()
        print(f"\nTesting string: {s}")
        print(f"Expected partitions: {expected}")
        print(f"Actual partitions: {result}")
        print(f"Test passed: {sorted(result) == sorted(expected)}")


def main() -> None:
    """Main function to demonstrate and test the palindrome partitioning solution."""
    print("Testing palindrome partitioning solution...\n")
    test_solutions()
    print("\nAll tests completed!")


if __name__ == "__main__":
    main()

