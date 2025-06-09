class ProblemStatement:
    """
    Longest Palindrome Length Problem

    Given a string s which consists of lowercase or uppercase letters, return the length
    of the longest palindrome that can be built with those letters.
    
    Note: Letters are case sensitive, for example, "Aa" is not considered a palindrome.

    Examples:
        Example 1:
            Input: s = "abccccdd"
            Output: 7
            Explanation: One longest palindrome that can be built is "dccaccd",
                        whose length is 7.

        Example 2:
            Input: s = "a"
            Output: 1
            Explanation: The longest palindrome that can be built is "a",
                        whose length is 1.
    """


class Specifications:
    METHOD_A = """
    Character Frequency Counter Approach

    Algorithm Steps:
    1. Count the frequency of each character in the input string
    2. For each character:
        a. If frequency is even, use all occurrences
        b. If frequency is odd, use (frequency - 1) occurrences
        c. Keep track if we have any odd frequencies
    3. If we found any odd frequencies, we can use one character as the center
    4. Sum up all even pairs and add 1 for the center if needed

    Key Points:
    - Even frequencies contribute fully to the palindrome length
    - Odd frequencies contribute (frequency - 1) to the length
    - One odd frequency can be used as the center
    - Case sensitivity matters in character matching
    """


class EfficiencyHandling:
    METHOD_A = """
    Time Complexity:
        - Counting character frequencies: O(n), where n is the length of input string
        - Sorting frequencies: O(k log k), where k is the number of unique characters
        - Processing frequencies: O(k)
        - Overall time complexity: O(n + k log k)
        - Since k (unique characters) is bounded by the alphabet size,
          the time complexity simplifies to O(n)

    Space Complexity:
        - Character frequency counter: O(k), where k is the number of unique characters
        - Since k is bounded by the alphabet size (52 for a-z and A-Z),
          the space complexity is O(1)
    """


class Pseudocode:
    METHOD_A = """
    def longest_palindrome(s: str) -> int:
        # Handle edge cases
        if not s:
            return 0
        if len(s) == 1:
            return 1

        # Initialize variables
        length = 0
        has_odd_frequency = False

        # Count character frequencies
        char_count = Counter(s)

        # Process each character's frequency
        for char, frequency in char_count.items():
            if frequency % 2 == 1:
                has_odd_frequency = True
            
            # Add even pairs to length
            length += frequency - (frequency % 2)

        # Add center character if needed
        if has_odd_frequency:
            length += 1

        return length
    """
    