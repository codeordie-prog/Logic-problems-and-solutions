from typing import Any, List, Dict, Set
from collections import defaultdict


class WordPattern:
    """
    Determines if a string follows a given pattern by establishing a bijection between pattern characters and words.
    """
    def __init__(self, pattern: str, s: str) -> None:
        self.result: bool = self.follows_pattern(pattern, s)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        return self.result

    def follows_pattern(self, pattern: str, s: str) -> bool:
        """
        Checks if the string s follows the given pattern.

        Args:
            pattern (str): The pattern string containing characters.
            s (str): The input string to check against the pattern.

        Returns:
            bool: True if s follows the pattern, False otherwise.
        """
        # Handle edge cases for empty pattern and string
        if not pattern and not s:
            return True
        if not pattern or not s:
            return False
            
        character_store: Dict[int, str] = defaultdict(str)
        patterns_map: Dict[str, str] = defaultdict(str)
        words: List[str] = s.split(" ")
        seen: Set[str] = set()

        for i, char in enumerate(pattern):
            character_store[i] = char

        for j, word in enumerate(words):
            # Case: unmapped unique words
            if j >= len(character_store):
                return False

            # Current pattern
            current_pattern: str = character_store[j]

            # Case: duplicate word
            if word in seen and patterns_map[current_pattern] != word:
                return False

            # Case: word violates pattern
            if current_pattern in patterns_map and patterns_map[current_pattern] != word.strip():
                return False

            # Case: no violations
            elif current_pattern in patterns_map and patterns_map[current_pattern] == word.strip():
                continue

            # Add word to seen and map its pattern
            seen.add(word)
            patterns_map[current_pattern] = word.strip()

        return j == len(character_store) - 1


def main() -> None:
    """
    Test cases for the WordPattern class.
    """
    # Test case 1: Valid pattern
    pattern = "abba"
    s = "dog cat cat dog"
    result = WordPattern(pattern, s)
    print(f"Test 1: {result()}")  # Expected: True

    # Test case 2: Invalid pattern
    pattern2 = "abba"
    s2 = "dog cat cat fish"
    result2 = WordPattern(pattern2, s2)
    print(f"Test 2: {result2()}")  # Expected: False

    # Test case 3: Pattern with repeated characters
    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    result3 = WordPattern(pattern3, s3)
    print(f"Test 3: {result3()}")  # Expected: False

    # Test case 4: Single character pattern
    pattern4 = "a"
    s4 = "hello"
    result4 = WordPattern(pattern4, s4)
    print(f"Test 4: {result4()}")  # Expected: True

    # Test case 5: Empty string
    pattern5 = ""
    s5 = ""
    result5 = WordPattern(pattern5, s5)
    print(f"Test 5: {result5()}")  # Expected: True

    # Test case 6: Different pattern lengths
    pattern6 = "abc"
    s6 = "dog cat"
    result6 = WordPattern(pattern6, s6)
    print(f"Test 6: {result6()}")  # Expected: False

    # Assertions for validation
    assert result() is True
    assert result2() is False
    assert result3() is False
    assert result4() is True
    assert result5() is True
    assert result6() is False


if __name__ == "__main__":
    main()
