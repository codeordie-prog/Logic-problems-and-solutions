from typing import List, Dict, Any, Optional


class RecursionPlusMemoization_Solution_For_WordBreak:
    """
    A solution class for the Word Break problem using recursion with memoization.
    
    This class implements a solution that determines if a string can be segmented
    into a sequence of words from a given dictionary using recursive approach
    with memoization for optimization.
    
    Attributes:
        result (bool): The result of the word break operation
    """

    def __init__(self, s: str, word_dict: List[str]) -> None:
        """
        Initialize the solution with input string and word dictionary.

        Args:
            s (str): The input string to be segmented
            word_dict (List[str]): List of valid words for segmentation
        """
        self.result: bool = self.process(s, word_dict)

    def __call__(self, *args: Any, **kwargs: Any) -> bool:
        """
        Make the class callable to get the result.

        Returns:
            bool: True if the string can be segmented, False otherwise
        """
        return self.result
    
    def process(self, s: str, word_dict: List[str]) -> bool:
        """
        Process the input string to check if it can be segmented.

        Args:
            s (str): The input string to be segmented
            word_dict (List[str]): List of valid words for segmentation

        Returns:
            bool: True if the string can be segmented, False otherwise
        """
        memo: Dict[str, bool] = {}

        def _break(suffix: str) -> bool:
            """
            Helper function to recursively check if a suffix can be segmented.

            Args:
                suffix (str): The remaining string to be checked

            Returns:
                bool: True if the suffix can be segmented, False otherwise
            """
            if not suffix:
                return True
            
            if suffix in memo:
                return memo[suffix]
            
            for word in word_dict:
                if suffix.startswith(word):
                    remaining: str = suffix[len(word):]
                    if _break(remaining):
                        memo[remaining] = True
                        return True
            
            memo[suffix] = False
            return False
        
        return _break(s)


def main() -> None:
    """
    Main function to demonstrate the Word Break solution.
    
    Creates example cases and prints the results in a readable format.
    """
    # Example 1
    s1: str = "leetcode"
    word_dict1: List[str] = ["leet", "code"]
    solution1 = RecursionPlusMemoization_Solution_For_WordBreak(s1, word_dict1)
    
    # Example 2
    s2: str = "applepenapple"
    word_dict2: List[str] = ["apple", "pen"]
    solution2 = RecursionPlusMemoization_Solution_For_WordBreak(s2, word_dict2)
    
    # Example 3
    s3: str = "catsandog"
    word_dict3: List[str] = ["cats", "dog", "sand", "and", "cat"]
    solution3 = RecursionPlusMemoization_Solution_For_WordBreak(s3, word_dict3)

    # Print results in a readable format
    print("\nWord Break Problem Results:")
    print("-" * 50)
    
    print(f"\nExample 1:")
    print(f"Input string: {s1}")
    print(f"Word dictionary: {word_dict1}")
    print(f"Can be segmented: {solution1()}")
    
    print(f"\nExample 2:")
    print(f"Input string: {s2}")
    print(f"Word dictionary: {word_dict2}")
    print(f"Can be segmented: {solution2()}")
    
    print(f"\nExample 3:")
    print(f"Input string: {s3}")
    print(f"Word dictionary: {word_dict3}")
    print(f"Can be segmented: {solution3()}")
    print("-" * 50)


if __name__ == "__main__":
    main()