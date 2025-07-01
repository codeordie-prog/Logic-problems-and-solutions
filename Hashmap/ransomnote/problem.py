class ProblemStatement:
    """
    Given two strings, ransomNote and magazine, return True if ransomNote can be constructed using the letters from magazine, and False otherwise.
    Each letter in magazine can only be used once in ransomNote.

    Example 1:
        Input: ransomNote = "a", magazine = "b"
        Output: False
    Example 2:
        Input: ransomNote = "aa", magazine = "ab"
        Output: False
    Example 3:
        Input: ransomNote = "aa", magazine = "aab"
        Output: True
    """


class Specifications:
    """
    1. Initialize a counter to count each character in magazine.
    2. Iterate through each character in ransomNote:
        - If the character exists in the counter and its count is greater than 0, decrement the count by 1.
        - Otherwise, return False immediately.
    3. If all characters are accounted for, return True at the end.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        O(N), where N is the length of magazine plus ransomNote.

    Space Complexity:
        O(1), since the alphabet size is fixed (assuming only lowercase English letters).
    """


class Pseudocode:
    """
    FUNCTION can_construct(ransomNote, magazine):
        counter = Counter(magazine)
        for char in ransomNote:
            if char in counter AND counter[char] > 0:
                counter[char] -= 1
            else:
                return False
        return True
    """