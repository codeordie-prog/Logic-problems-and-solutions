

from typing import Any


class Recursion:
    """
    Implements a recursive approach to check if a number is a power of two.
    """
    def __init__(self, n: int) -> None:
        """
        Initialize the class and compute the result.
        Args:
            n (int): The number to check.
        """
        self.result: bool = self.is_power_2(n)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """
        Callable interface to return the computed result.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        return self.result
    
    def is_power_2(self, n: int) -> bool:
        """
        Check if n is a power of two using recursion.
        Args:
            n (int): The number to check.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        
        def helper(x: int) -> bool:
            if x == n:
                return True
            if x > n:
                return False
            return helper(x * 2)
        
        return helper(1)
    

class Loop:
    """
    Implements an iterative (while loop) approach to check if a number is a power of two.
    """
    def __init__(self, n: int) -> None:
        """
        Initialize the class and compute the result.
        Args:
            n (int): The number to check.
        """
        self.result: bool = self.is_power_2(n)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """
        Callable interface to return the computed result.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        return self.result
    
    def is_power_2(self, n: int) -> bool:
        """
        Check if n is a power of two using an iterative approach.
        Args:
            n (int): The number to check.
        Returns:
            bool: True if n is a power of two, False otherwise.
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        x: int = 1
        while x < n:
            x *= 2
        return x == n

def main() -> None:
    """
    Run a set of test cases to validate both the recursive and iterative solutions.
    """
    test_cases: list[int] = [0, 2, 3, 67, 4, 8, 64, 32]
    for n in test_cases:
        result_1: bool = Recursion(n)()
        result_2: bool = Loop(n)()
        assert result_1 == result_2
        print(f"Test case: {n} result is {result_1}")
    print("All test cases passed!")

if __name__ == "__main__":
    main()
