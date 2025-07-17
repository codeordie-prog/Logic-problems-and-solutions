
from typing import Any, List


class Solution:
    """
    Solution class to check if the usage of capitals in a word is correct.
    Usage is correct if:
        - All letters are uppercase.
        - All letters are lowercase.
        - Only the first letter is uppercase and the rest are lowercase.
    """
    def __init__(self, word: str) -> None:
        """
        Initialize the Solution with the result of the uppercase detection.
        Args:
            word (str): The word to check for correct capital usage.
        """
        self.result: bool = self.detect_uppercase(word)

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        """
        Callable interface to return the result.
        Returns:
            bool: True if the word uses capitals correctly, False otherwise.
        """
        return self.result
    
    def detect_uppercase(self, word: str) -> bool:
        """
        Check if the word uses capitals correctly.
        Args:
            word (str): The word to check.
        Returns:
            bool: True if the usage is correct, False otherwise.
        """
        if word.islower() or word.isupper():
            return True
        return word[0].isupper() and word[1:].islower()
    

def main() -> None:
    """
    Main function to test the Solution class with example words.
    """
    words: List[str] = ["Google", "leetcode", "USA"]

    for word in words:
        result: bool = Solution(word)()
        assert result is True
        print(result)


if __name__ == "__main__":
    main()