from typing import Any, Dict, Tuple
from collections import Counter


class MaxDifference:
    """Class to compute maximum difference between odd and even character frequencies."""

    def __init__(self, s: str) -> None:
        """Initialize the solution with input string.
        
        Args:
            s: Input string to analyze
        """
        self.result: int = self.compute_diff(s)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """Return the result when the class instance is called.
        
        Returns:
            int: Maximum difference between odd and even frequencies
        """
        return self.result
    
    def compute_diff(self, s: str) -> int:
        """Compute the maximum difference between odd and even character frequencies.
        
        Args:
            s: Input string to analyze
            
        Returns:
            int: Maximum difference between odd and even frequencies
        """
        if not s:
            return 0
        
        frequencies: Counter = Counter(s)

        max_odd_frequency: float = float("-inf")
        min_even_frequency: float = float("inf")

        for _, value in frequencies.items():
            if value % 2 > 0:
                max_odd_frequency = max(max_odd_frequency, value)
            elif value % 2 == 0:
                min_even_frequency = min(min_even_frequency, value)

        if isinstance(max_odd_frequency, float):
            max_odd_frequency = 0

        if isinstance(min_even_frequency, float):
            min_even_frequency = 0

        return max_odd_frequency - min_even_frequency


def main() -> None:
    """Main function to demonstrate the solution with example cases."""
    # Example test cases
    test_cases: Dict[str, int] = {
        "aaaaabbd": 3,  # 'a' (5) - 'b' (2) = 3
        "abcabcab": 1,  # 'a' (3) - 'c' (2) = 1
        "": 0,          # Empty string
        "a": 1,         # Single character
    }
    
    # Run all test cases
    for test_string, expected in test_cases.items():
        result: MaxDifference = MaxDifference(test_string)
        actual: int = result()
        print(f"Input: {test_string}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print(f"Test {'PASSED' if actual == expected else 'FAILED'}")
        print("-" * 40)


if __name__ == "__main__":
    main()
        
