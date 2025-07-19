class ProblemStatement:
    """
    You are given a 0-indexed string array words.
    Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
    isPrefixAndSuffix(str1, str2) returns True if str1 is both a prefix and a suffix of str2, and False otherwise.
    For example, isPrefixAndSuffix("aba", "ababa") is True because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is False.
    Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is True.

    Example 1:
    Input: words = ["a", "aba", "ababa", "aa"]
    Output: 4
    Explanation: In this example, the counted index pairs are:
    i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is True.
    i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is True.
    i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is True.
    i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is True.
    Therefore, the answer is 4.

    Example 2:
    Input: words = ["pa", "papa", "ma", "mama"]
    Output: 2
    Explanation: In this example, the counted index pairs are:
    i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is True.
    i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is True.
    Therefore, the answer is 2.

    Example 3:
    Input: words = ["abab", "ab"]
    Output: 0
    Explanation: In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is False.
    Therefore, the answer is 0.
    """

class Specifications:
    """
    1. For each pair of indices (i, j) with i < j, check if words[i] is both a prefix and a suffix of words[j].
    2. Define a helper function is_prefix_and_suffix(word1, word2) that returns True if word2 starts and ends with word1.
    3. Iterate through all valid pairs and count those that satisfy the condition.
    4. Return the total count.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(N^2 * L), where N is the number of words and L is the average length of the words (due to prefix/suffix checks).
    Space Complexity:
        - O(1), as only a constant amount of extra space is used.
    """

class Pseudocode:
    """
    FUNCTION count_pairs(words: list of str) -> int:
        count = 0

        FUNCTION is_prefix_and_suffix(word1: str, word2: str) -> bool:
            RETURN word2.startswith(word1) AND word2.endswith(word1)

        FOR i FROM 0 TO LENGTH(words) - 2:
            FOR j FROM i + 1 TO LENGTH(words) - 1:
                IF is_prefix_and_suffix(words[i], words[j]):
                    count += 1

        RETURN count
    """