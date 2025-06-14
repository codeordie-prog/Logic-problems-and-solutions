from typing import Any, Dict, List


class RecursionPlusMemoization:
    """Solution using recursion with memoization approach.
    
    Attributes:
        result (int): The number of distinct ways to climb n stairs.
    """
    
    def __init__(self, n: int) -> None:
        """Initialize the solution with the number of stairs.
        
        Args:
            n (int): The number of stairs to climb.
        """
        self.result: int = self.climb_stairs(n)

    def __call__(self, *args: Any, **kwargs: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: The number of distinct ways to climb n stairs.
        """
        return self.result
    
    def climb_stairs(self, n: int) -> int:
        """Calculate the number of distinct ways to climb n stairs using recursion with memoization.
        
        Args:
            n (int): The number of stairs to climb.
            
        Returns:
            int: The number of distinct ways to climb n stairs.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        memo: Dict[int, int] = {}
        
        def climb(idx: int) -> int:
            """Helper function to calculate paths recursively.
            
            Args:
                idx (int): Current position in the stairs.
                
            Returns:
                int: Number of ways to reach the top from current position.
            """
            if idx >= n - 1:
                return 1
            if idx in memo:
                return memo[idx]
            
            path1: int = climb(idx + 1)
            path2: int = climb(idx + 2)

            memo[idx] = path1 + path2
            return memo[idx]
        
        return climb(0)


class BottomUpSolution:
    """Solution using dynamic programming (bottom-up) approach.
    
    Attributes:
        result (int): The number of distinct ways to climb n stairs.
    """
    
    def __init__(self, n: int) -> None:
        """Initialize the solution with the number of stairs.
        
        Args:
            n (int): The number of stairs to climb.
        """
        self.result: int = self.climb_stairs(n)

    def __call__(self, *args: Any, **kwargs: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: The number of distinct ways to climb n stairs.
        """
        return self.result
        
    def climb_stairs(self, n: int) -> int:
        """Calculate the number of distinct ways to climb n stairs using bottom-up DP.
        
        Args:
            n (int): The number of stairs to climb.
            
        Returns:
            int: The number of distinct ways to climb n stairs.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        table: List[int] = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        table[2] = 2

        for i in range(3, n + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[n]


def test_solutions() -> None:
    """Test both solutions with various inputs and verify they produce the same results."""
    test_cases: List[int] = [0, 1, 2, 3, 4, 5, 10]
    
    for n in test_cases:
        result1: int = RecursionPlusMemoization(n)()
        result2: int = BottomUpSolution(n)()
        
        print(f"Testing n = {n}")
        print(f"Recursion with memoization: {result1}")
        print(f"Bottom-up DP: {result2}")
        print(f"Results match: {result1 == result2}\n")
        
        assert result1 == result2, f"Solutions don't match for n = {n}"


def main() -> None:
    """Main function to demonstrate and test the climbing stairs solutions."""
    print("Testing climbing stairs solutions...\n")
    test_solutions()
    print("All tests passed successfully!")


if __name__ == "__main__":
    main()