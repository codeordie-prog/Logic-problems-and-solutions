from typing import Any, Dict, List


class Recursion:
    """Fibonacci implementation using basic recursion.
    
    This approach has exponential time complexity O(2^n) as each call branches into two
    subcalls, leading to redundant calculations. Not recommended for large values of n.
    """

    def __init__(self, n: int) -> None:
        """Initialize the solution with input number.
        
        Args:
            n: The nth Fibonacci number to calculate
        """
        self.result: int = self.fibonacci(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: The nth Fibonacci number
        """
        return self.result
    
    def fibonacci(self, n: int) -> int:
        """Calculate the nth Fibonacci number using recursion.
        
        Args:
            n: The position in the Fibonacci sequence
            
        Returns:
            int: The nth Fibonacci number
        """
        def compute_n(n: int) -> int:
            """Helper function to compute Fibonacci number recursively.
            
            Args:
                n: Current position in sequence
                
            Returns:
                int: Fibonacci number at position n
            """
            if n == 0:
                return 0
            if n == 1:
                return 1
            return compute_n(n - 1) + compute_n(n - 2)
        
        return compute_n(n)


class RecursionPlusMemoization:
    """Fibonacci implementation using recursion with memoization.
    
    This approach has linear time complexity O(n) as each value is calculated exactly once
    and stored in a memoization dictionary for future use.
    """

    def __init__(self, n: int) -> None:
        """Initialize the solution with input number.
        
        Args:
            n: The nth Fibonacci number to calculate
        """
        self.result: int = self.fibonacci(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: The nth Fibonacci number
        """
        return self.result
    
    def fibonacci(self, n: int) -> int:
        """Calculate the nth Fibonacci number using memoized recursion.
        
        Args:
            n: The position in the Fibonacci sequence
            
        Returns:
            int: The nth Fibonacci number
        """
        memo: Dict[int, int] = {}
        
        def compute_n(n: int) -> int:
            """Helper function to compute Fibonacci number with memoization.
            
            Args:
                n: Current position in sequence
                
            Returns:
                int: Fibonacci number at position n
            """
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = compute_n(n - 1) + compute_n(n - 2)
            return memo[n]
        
        return compute_n(n)


class BottomUpTabulation:
    """Fibonacci implementation using bottom-up dynamic programming.
    
    This approach has linear time complexity O(n) and uses a table to store intermediate
    results. It avoids recursion stack overhead and is more space-efficient than
    memoization for this particular problem.
    """

    def __init__(self, n: int) -> None:
        """Initialize the solution with input number.
        
        Args:
            n: The nth Fibonacci number to calculate
        """
        self.result: int = self.fibonacci(n)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: The nth Fibonacci number
        """
        return self.result
    
    def fibonacci(self, n: int) -> int:
        """Calculate the nth Fibonacci number using bottom-up DP.
        
        Args:
            n: The position in the Fibonacci sequence
            
        Returns:
            int: The nth Fibonacci number
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        table: List[int] = [0] * (n + 1)
        table[0] = 0
        table[1] = 1

        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]

        return table[n]


def main() -> None:
    """Main function to demonstrate and compare different Fibonacci implementations."""
    n: int = 20

    # Create instances of each implementation
    result_0: Recursion = Recursion(n)
    result_1: RecursionPlusMemoization = RecursionPlusMemoization(n)
    result_2: BottomUpTabulation = BottomUpTabulation(n)

    # Verify all implementations give the same result
    assert result_0() == result_1() == result_2()

    # Print results
    print(f"Basic Recursion: {result_0()}")
    print(f"Memoized Recursion: {result_1()}")
    print(f"Bottom-up DP: {result_2()}")


if __name__ == "__main__":
    main()