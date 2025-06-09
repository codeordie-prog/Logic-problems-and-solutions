from typing import List

class ProblemStatement:
    """
    Word Break Problem

    Given a string s and a dictionary of strings wordDict, determine if s can be segmented 
    into a space-separated sequence of one or more dictionary words.
    
    Note: The same word in the dictionary may be reused multiple times in the segmentation.

    Examples:
        Example 1:
            Input: s = "leetcode", wordDict = ["leet", "code"]
            Output: true
            Explanation: "leetcode" can be segmented as "leet code"

        Example 2:
            Input: s = "applepenapple", wordDict = ["apple", "pen"]
            Output: true
            Explanation: "applepenapple" can be segmented as "apple pen apple"
            Note: Dictionary words can be reused

        Example 3:
            Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
            Output: false
    """


class Specifications:
    METHOD_A = """
    Recursion with Memoization Approach

    Algorithm Steps:
    1. For each word in the dictionary:
        a. Check if the input string starts with the current word
        b. If yes, recursively process the remaining suffix
    2. Base case: Empty string returns True
    3. Use memoization to cache results of previously processed suffixes
    4. Return False if no valid segmentation is found

    Key Components:
    - Recursive function to process string segments
    - Memoization dictionary to store intermediate results
    - Word dictionary for valid word checking
    """


class EfficiencyHandling:
    METHOD_A = """
    Time Complexity:
        - Number of unique subproblems: O(m), where m is the length of input string
        - Work per subproblem: O(n), where n is the number of words in dictionary
        - Total time complexity: O(n * m)
        - Additional factor of O(k) for string prefix checking, where k is average word length
        - Final time complexity: O(n * m * k)

    Space Complexity:
        - Memoization storage: O(m) for storing results of unique substrings
        - Recursion stack: O(m) in worst case
        - Total space complexity: O(m)
    """


class Pseudocode:
    METHOD_A = """
    def word_break(s: str, word_dict: List[str]) -> bool:
        # Initialize memoization dictionary
        memo = {}
        
        def _break(suffix: str) -> bool:
            # Base case: empty string is valid
            if not suffix:
                return True
            
            # Return cached result if available
            if suffix in memo:
                return memo[suffix]
            
            # Try each word in dictionary
            for word in word_dict:
                if suffix.startswith(word):
                    # Process remaining suffix
                    remaining = suffix[len(word):]
                    if _break(remaining):
                        memo[suffix] = True
                        return True
            
            # No valid segmentation found
            memo[suffix] = False
            return False
        
        return _break(s)
    """
    