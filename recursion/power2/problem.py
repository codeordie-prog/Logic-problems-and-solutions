
class ProblemStatement:
    """
    Given an integer n, return True if it is a power of two. Otherwise, return False.

    An integer n is a power of two if there exists an integer x such that n == 2 ** x.

    Example 1:
        Input: n = 1
        Output: True
        Explanation: 2 ** 0 = 1

    Example 2:
        Input: n = 16
        Output: True
        Explanation: 2 ** 4 = 16

    Example 3:
        Input: n = 3
        Output: False
    """

class Specifications:
    """
    1. Start with x = 1 (which is 2 ** 0).
    2. Repeatedly multiply x by 2 (or left shift by 1) until x >= n.
    3. If x == n at any point, return True. If x > n, return False.
    4. Alternatively, use recursion to perform the same check.
    """

class EfficiencyHandling:
    """
    Recursive Approach:
        Time Complexity: O(log N) - Each recursive call doubles x, so the number of calls is proportional to log N.
        Space Complexity: O(log N) - Due to the recursion stack.

    Iterative (While Loop) Approach:
        Time Complexity: O(log N) - Each iteration doubles x.
        Space Complexity: O(1) - Only a constant amount of extra space is used.
    """

class Pseudocode:
    """
    1. Recursive Approach
    FUNCTION is_power_of_two(n):
        IF n <= 0: RETURN False
        IF n == 1: RETURN True

        FUNCTION helper(x):
            IF x == n:
                RETURN True
            IF x > n:
                RETURN False
            RETURN helper(x * 2)

        RETURN helper(1)

    2. Iterative Approach (While Loop)
    FUNCTION is_power_of_two(n):
        IF n <= 0: RETURN False
        IF n == 1: RETURN True
        x = 1
        WHILE x < n:
            x *= 2
        RETURN x == n
    """