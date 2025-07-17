
class ProblemStatement:
    """
    We define the usage of capitals in a word to be right when one of the following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

    Example 1:
    Input: word = "USA"
    Output: true

    Example 2:
    Input: word = "FlaG"
    Output: false
    """

class Specifications:
    """
    Specifications:
    1. A valid uppercase word is one of the following:
        a. All letters are uppercase (e.g., "USA").
        b. All letters are lowercase (e.g., "leetcode").
        c. Only the first letter is uppercase and the rest are lowercase (e.g., "Google").
    2. Any other combination is considered invalid.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(1).
    Space Complexity:
        - O(1), as no extra space is used beyond variables.
    """

class Pseudocode:
    """
    FUNCTION uppercase_detector(word):
        IF word.islower() OR word.isupper():
            RETURN True
        RETURN word[0].isupper() AND word[1:].islower()
    """
