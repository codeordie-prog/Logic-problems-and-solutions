class ProblemStatement:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

    Example 1:
        Input: nums = [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

    Example 2:
        Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        Output: 9

    Example 3:
        Input: nums = [1, 0, 1, 2]
        Output: 3
    """


class Specifications:
    """
    1. Initialize a set from nums to remove duplicates and allow O(1) lookups.
    2. Initialize a memoization dictionary to cache results for each number.
    3. Define a recursive count function:
        - Base case: If the number is not in the set, return 0.
        - If the number is already cached, return the cached result.
        - Otherwise, return 1 + count(num + 1) and cache the result.
    4. For each number in the set, compute the maximum count using the count function.
    5. Return the maximum length found.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        O(N), where N is the number of elements in nums, since each number is processed at most once.

    Space Complexity:
        O(N), for the set and memoization dictionary.
    """


class Pseudocode:
    """
    FUNCTION longest_sequence(nums):
        num_set = set(nums)
        memo = dict()

        FUNCTION count(num):
            IF num not in num_set:
                RETURN 0
            IF num in memo:
                RETURN memo[num]
            res = 1 + count(num + 1)
            memo[num] = res
            RETURN res

        max_len = float('-inf')
        FOR num in num_set:
            max_len = max(max_len, count(num))
        RETURN max_len
    """