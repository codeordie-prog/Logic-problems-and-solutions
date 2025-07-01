from typing import Any
from collections import Counter

class Solution:
    def __init__(self, ransomNote: str, magazine: str) -> None:
        self.result: bool = self.can_construct(ransomNote, magazine)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        return self.result

    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for char in ransomNote:
            if char in counter and counter[char] > 0:
                counter[char] -= 1
            else:
                return False
        return True


def main() -> None:
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
