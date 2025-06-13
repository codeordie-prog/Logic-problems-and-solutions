from typing import Any, Callable


class ReverseInteger:
    """Solution using integer reversal approach."""
    
    def __init__(self, x: int) -> None:
        """Initialize with input number and compute result.
        
        Args:
            x: The number to check for palindrome
        """
        self.result: bool = self.is_palindrome(x)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """Return the computed result.
        
        Returns:
            bool: True if number is palindrome, False otherwise
        """
        return self.result
    
    def is_palindrome(self, x: int) -> bool:
        """Check if number is palindrome using integer reversal.
        
        Args:
            x: The number to check
            
        Returns:
            bool: True if number is palindrome, False otherwise
        """
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        reversed_num: int = 0
        num: int = x
        
        while num != 0:
            digit: int = num % 10
            reversed_num = (reversed_num * 10) + digit
            num //= 10

        return reversed_num == x


class StringComparison:
    """Solution using string comparison approach."""
    
    def __init__(self, x: int) -> None:
        """Initialize with input number and compute result.
        
        Args:
            x: The number to check for palindrome
        """
        self.result: bool = self.is_palindrome(x)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """Return the computed result.
        
        Returns:
            bool: True if number is palindrome, False otherwise
        """
        return self.result
    
    def is_palindrome(self, x: int) -> bool:
        """Check if number is palindrome using string comparison.
        
        Args:
            x: The number to check
            
        Returns:
            bool: True if number is palindrome, False otherwise
        """
        x_str: str = str(x)
        return x_str[::-1] == x_str


def test_palindrome(x: int, solution: Callable[[], bool]) -> None:
    """Test a palindrome solution with given input.
    
    Args:
        x: The number to test
        solution: The solution function to test
    """
    result: bool = solution()
    print(f"Input: {x}")
    print(f"Result: {result}")
    print("-" * 30)


def main() -> None:
    """Main function to demonstrate and test palindrome solutions."""
    test_cases: list[int] = [121, -121, 10, 0, 12321, 12345]
    
    for x in test_cases:
        print(f"\nTesting number: {x}")
        solution1 = ReverseInteger(x)
        solution2 = StringComparison(x)
        
        # Verify both solutions give same result
        assert solution1() == solution2(), f"Solutions disagree for input {x}"
        
        print("Solution 1 (Integer Reversal):")
        test_palindrome(x, solution1)
        
        print("Solution 2 (String Comparison):")
        test_palindrome(x, solution2)


if __name__ == "__main__":
    main()


