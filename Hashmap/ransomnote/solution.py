from typing import Any
from collections import Counter

class Solution:
    """
    Determines if a ransom note can be constructed from the letters of a magazine.
    """
    def __init__(self, ransomNote: str, magazine: str) -> None:
        """
        Initialize the Solution and determine if ransomNote can be constructed from magazine.

        Args:
            ransomNote (str): The ransom note string to construct.
            magazine (str): The magazine string to use letters from.
        """
        self.result: bool = self.can_construct(ransomNote, magazine)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """
        Return the result of the construction check.

        Returns:
            bool: True if ransomNote can be constructed from magazine, False otherwise.
        """
        return self.result

    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransomNote can be constructed from magazine using each letter at most once.

        Args:
            ransomNote (str): The ransom note string to construct.
            magazine (str): The magazine string to use letters from.

        Returns:
            bool: True if possible, False otherwise.
        """
        counter = Counter(magazine)
        for char in ransomNote:
            if char in counter and counter[char] > 0:
                counter[char] -= 1
            else:
                return False
        return True


def main() -> None:
    """
    Runs several test cases to verify the Solution class for ransom note construction.
    """
    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("abc", "aabbcc", True),
        ("aabbc", "abcabc", True),
        ("aabbcc", "abc", False),
    ]
    for i, (ransomNote, magazine, expected) in enumerate(test_cases, 1):
        solution = Solution(ransomNote, magazine)
        result = solution()
        print(f"Test case {i}: ransomNote='{ransomNote}', magazine='{magazine}' => {result} (expected: {expected})")
        assert result == expected, f"Test case {i} failed!"
    print("All test cases passed.")


if __name__ == "__main__":
    main()
