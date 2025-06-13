from typing import Any, Callable


class BottomUpTabulation:
    """Solution using bottom-up dynamic programming approach.
    
    This approach uses a table to store all intermediate values,
    making it easier to understand but using O(n) space.
    """
    
    def __init__(self, n: int) -> None:
        """Initialize with input number and compute result.
        
        Args:
            n: The position in the Tribonacci sequence to calculate
        """
        self.result: int = self.tribonacci(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the computed result.
        
        Returns:
            int: The nth Tribonacci number
        """
        return self.result
    
    def tribonacci(self, n: int) -> int:
        """Calculate the nth Tribonacci number using bottom-up DP.
        
        Args:
            n: The position in the sequence to calculate
            
        Returns:
            int: The nth Tribonacci number
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        table: list[int] = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        table[2] = 1

        for i in range(3, n + 1):
            table[i] = table[i-1] + table[i-2] + table[i-3]

        return table[n]


class SpaceOptimization:
    """Solution using space-optimized approach.
    
    This approach uses only three variables to track the sequence,
    achieving O(1) space complexity while maintaining O(n) time complexity.
    """
    
    def __init__(self, n: int) -> None:
        """Initialize with input number and compute result.
        
        Args:
            n: The position in the Tribonacci sequence to calculate
        """
        self.result: int = self.tribonacci(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the computed result.
        
        Returns:
            int: The nth Tribonacci number
        """
        return self.result
    
    def tribonacci(self, n: int) -> int:
        """Calculate the nth Tribonacci number using space optimization.
        
        Args:
            n: The position in the sequence to calculate
            
        Returns:
            int: The nth Tribonacci number
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        a: int = 0
        b: int = 1
        c: int = 1
        
        for _ in range(3, n + 1):
            next_num: int = a + b + c
            a, b, c = b, c, next_num

        return c


def test_tribonacci(n: int, solution: Callable[[], int]) -> None:
    """Test a Tribonacci solution with given input.
    
    Args:
        n: The position in the sequence to test
        solution: The solution function to test
    """
    result: int = solution()
    print(f"Input: n = {n}")
    print(f"Result: {result}")
    print("-" * 30)


def main() -> None:
    """Main function to demonstrate and test Tribonacci solutions."""
    test_cases: list[int] = [0, 1, 2, 4, 25]
    
    for n in test_cases:
        print(f"\nTesting position: {n}")
        solution1 = BottomUpTabulation(n)
        solution2 = SpaceOptimization(n)
        
        # Verify both solutions give same result
        assert solution1() == solution2(), f"Solutions disagree for input {n}"
        
        print("Solution 1 (Bottom-up DP):")
        test_tribonacci(n, solution1)
        
        print("Solution 2 (Space-Optimized):")
        test_tribonacci(n, solution2)


if __name__ == "__main__":
    main()