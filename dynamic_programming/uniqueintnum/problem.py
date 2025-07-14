
class ProblemStatement:
    """
    Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.
    Example 1:

    Input: n = 2
    Output: 91
    Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
    excluding 11,22,33,44,55,66,77,88,99

    Example 2:
    Input: n = 0
    Output: 1
    """

class Specifications:
    """
    This is a combinatorics problem.
    1. Start with 1-digit numbers (k = 1) and proceed to higher digits. The goal is to find a repeating pattern that can be captured with an algorithm.

    2. When k = 1, the total unique numbers are 0-9, i.e., 10.
    3. For k = 2, the first digit can only be 1-9 (0 is not an option), so there are 9 possibilities. For the second digit, we have 0-9 possibilities, excluding the digit used for the first digit, resulting in 9 possibilities.

    4. For k = 3: the first digit has 9 options, the second digit has 9 options, and the third digit has 8 options (excluding the two digits already used).

    5. From k = 3 onwards, the number of available options reduces by 1, starting from 8. Thus:
        i = [9, 9, 8, 7, 6, 5, 4, 3, 2] (1-indexed array)

    6. To generalize, at any given k:
        unique_nums = available_options * current_i + previous_count
        For k = 2:
            current_i = 9
            previous_count = 10 (for k = 1, since [0-9] = 10 unique digits)
            So, 9 * 9 = 81, plus previous count: 10 + 81 = 91
        For k = 3:
            current_i = 8
            previous_count = 91
            So, (81 * 8) + 91 = 739
    """

class EfficiencyHandling:
    """
    Time Complexity:
        O(n), where n is the input value.

    Space Complexity:
        O(1), as only a constant amount of extra space is used.
    """

class Pseudocode:
    """
    FUNCTION count_unique(n):
        IF n == 0:
            RETURN 1

        count = 10
        options = 9
        current_i = 9

        FOR _ IN range(2, n + 1):
            current_i *= options
            count += current_i
            options -= 1

        RETURN count
    """