from typing import Any, List


class Solution:
    """
    Solution class to count the number of index pairs (i, j) such that i < j and
    words[i] is both a prefix and a suffix of words[j].
    """
    def __init__(self, words: List[str]) -> None:
        """
        Initialize the Solution with the result of the prefix and suffix count.
        Args:
            words (List[str]): The list of words to process.
        """
        self.result: int = self.countprefixsuffixpairs(words)

    def __call__(self, *args: Any, **kwds: Any) -> int:
        """
        Callable interface to return the result.
        Returns:
            int: The number of valid (i, j) pairs.
        """
        return self.result
    
    def countprefixsuffixpairs(self, words: List[str]) -> int:
        """
        Count the number of index pairs (i, j) such that i < j and words[i] is both a prefix and a suffix of words[j].
        Args:
            words (List[str]): The list of words to process.
        Returns:
            int: The number of valid (i, j) pairs.
        """
        def is_both_pref_and_suff(str1: str, str2: str) -> bool:
            """
            Check if str1 is both a prefix and a suffix of str2.
            Args:
                str1 (str): The prefix/suffix candidate.
                str2 (str): The target string.
            Returns:
                bool: True if str1 is both a prefix and a suffix of str2, False otherwise.
            """
            return str2.startswith(str1) and str2.endswith(str1)
        
        count: int = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if is_both_pref_and_suff(words[i], words[j]):
                    count += 1
        return count
    
def main() -> None:
    """
    Main function to test the Solution class with example test cases.
    """
    # Test case 1
    words1: List[str] = ["a", "aba", "ababa", "aa"]
    result1: int = Solution(words1)()
    assert result1 == 4
    print(result1)

    # Test case 2
    words2: List[str] = ["pa", "papa", "ma", "mama"]
    result2: int = Solution(words2)()
    assert result2 == 2
    print(result2)

    # Test case 3
    words3: List[str] = ["abab", "ab"]
    result3: int = Solution(words3)()
    assert result3 == 0
    print(result3)

if __name__ == "__main__":
    main()