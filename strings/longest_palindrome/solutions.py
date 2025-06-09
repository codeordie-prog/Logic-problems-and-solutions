from typing import Any, Dict, List
from collections import Counter


class LongestPalindromeSolution:
    """
    A solution class for finding the length of the longest palindrome that can be built
    from a given string of characters.
    
    This class implements a solution that counts character frequencies and determines
    the maximum possible palindrome length by considering even and odd character counts.
    
    Attributes:
        result (int): The length of the longest possible palindrome
    """

    def __init__(self, s: str) -> None:
        """
        Initialize the solution with input string.

        Args:
            s (str): The input string to process
        """
        self.result: int = self.process(s)

    def __call__(self, *args: Any, **kwargs: Any) -> int:
        """
        Make the class callable to get the result.

        Returns:
            int: The length of the longest possible palindrome
        """
        return self.result
    
    def process(self, s: str) -> int:
        """
        Process the input string to find the length of the longest possible palindrome.

        Args:
            s (str): The input string to process

        Returns:
            int: The length of the longest possible palindrome
        """
        # Handle edge cases
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        length: int = 0
        remainder_flag: bool = False

        # Count character frequencies
        counter: Counter = Counter(s)

        # Sort characters by frequency in descending order
        sorted_chars: List[str] = sorted(
            counter.keys(),
            key=lambda x: counter[x],
            reverse=True
        )

        # Process each character
        for char in sorted_chars:
            value: int = counter[char]
            
            # Check for odd frequency
            if value % 2 > 0:
                remainder_flag = True

            # Add even pairs to length
            length += value - (value % 2)

        # Add center character if needed
        if remainder_flag:
            length += 1

        return length


def main() -> None:
    """
    Main function to demonstrate the Longest Palindrome solution.
    
    Creates example cases and prints the results in a readable format.
    """
    # Example cases
    test_cases: List[str] = [
        "abccccdd",  # Should return 7
        "a",         # Should return 1
        "ccc",       # Should return 3
        "bb",        # Should return 2
        "aabbcc"     # Should return 6
    ]

    # Print results in a readable format
    print("\nLongest Palindrome Problem Results:")
    print("-" * 50)
    
    for i, test_string in enumerate(test_cases, 1):
        solution = LongestPalindromeSolution(test_string)
        print(f"\nExample {i}:")
        print(f"Input string: {test_string}")
        print(f"Longest palindrome length: {solution()}")
    
    print("-" * 50)


if __name__ == "__main__":
    main()
        
        
        