from typing import Any, Final, List


class BottomUpNumberOfDecodings:
    """
    This class implements the solution for the Number of Decodings problem using bottom-up dynamic programming.
    It calculates the number of ways to decode a string of digits into letters using the mapping:
    1 -> 'A', 2 -> 'B', ..., 26 -> 'Z'

    Time Complexity: O(n)
        - We process each character in the string exactly once
        - Each operation at each step is O(1)
        - Where n is the length of the input string

    Space Complexity: O(n)
        - We maintain a 1D table of size n
        - Each cell stores the number of ways to decode up to that position
        - No additional space is needed

    Attributes:
        result (int): The number of ways to decode the input string.
    """

    def __init__(self, s: str) -> None:
        """
        Initialize the solution with the input string and calculate the result.

        Args:
            s (str): The input string containing only digits.
        """
        self.result: int = self.calculate_decodings(s)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Return the calculated result when the class instance is called.

        Returns:
            int: The number of ways to decode the input string.
        """
        return self.result

    def calculate_decodings(self, s: str) -> int:
        """
        Calculate the number of ways to decode the input string using bottom-up dynamic programming.

        Args:
            s (str): The input string containing only digits.

        Returns:
            int: The number of ways to decode the string. Returns 0 if the string cannot be decoded.
        """
        # Handle invalid cases
        if s == '' or s.startswith('0'):
            return 0

        length: int = len(s)
        # Handle single digit case
        if length == 1:
            return 1

        # Initialize table
        table: List[int] = [0 for _ in range(length)]
        table[0] = 1  # First position always has 1 way

        # Handle second position
        prev: str = s[0]
        if s[1] == '0':
            if prev == '1' or prev == '2':
                table[1] = 1
            else:
                return 0
        else:
            if prev == '1' or prev == '2':
                if int(s[1]) <= 6:
                    table[1] = 2  # Can be decoded as single or double digit
                else:
                    table[1] = 1  # Can only be decoded as single digit
            else:
                return 0  # Invalid encoding

        # Fill the table
        for i in range(2, length):
            prev = s[i-1]
            if s[i] == '0':
                if prev == '1' or prev == '2':
                    table[i] = table[i-2]  # Can only be decoded as part of previous digit
                else:
                    return 0  # Invalid encoding
            else:
                table[i] = table[i-1]  # Can be decoded as single digit
                if 10 <= int(s[i-1:i+1]) <= 26:
                    table[i] += table[i-2]  # Can also be decoded as double digit

        return table[-1]


def main() -> None:
    """
    Main function to demonstrate the solution with example inputs.
    """
    s: Final[str] = "2611055971756562"
    decoded = BottomUpNumberOfDecodings(s)
    print(f"Number of ways to decode '{s}': {decoded()}")


if __name__ == "__main__":
    main()