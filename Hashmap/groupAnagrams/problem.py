class ProblemStatement:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    Example 1:
        Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        Explanation:
        - There is no string in strs that can be rearranged to form "bat".
        - The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        - The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

    Example 2:
        Input: strs = [""]
        Output: [[""]]

    Example 3:
        Input: strs = ["a"]
        Output: [["a"]]
    """


class Specifications:
    """
    1. A word is an anagram of another if it can be rearranged to form the second word.
    2. This means sorted(word1) == sorted(word2) evaluates to True.
    3. Initialize a defaultdict with lists as values to group words by their sorted character key.
    4. For each word, sort its characters and use the sorted string as the key; append the word to the corresponding list.
    5. Return a list of all grouped anagrams (the values of the defaultdict).
    """


class EfficiencyHandling:
    """
    Time Complexity:
        O(N * K log K), where N is the number of words and K is the maximum length of a word (for sorting each word).

    Space Complexity:
        O(N * K), for storing the grouped anagrams.
    """


class Pseudocode:
    """
    FUNCTION group_anagrams(strs):
        anagrams = defaultdict(list)
        FOR each word in strs:
            sorted_chars = sorted(word)
            sorted_word = JOIN each char in sorted_chars
            anagrams[sorted_word].append(word)
        RETURN [values for each value in anagrams.values()]
    """