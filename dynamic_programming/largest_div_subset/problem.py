
class ProblemStatement:
    """
    Given a set of distinct positive integers nums, return the largest subset such that every pair
    (answer[i], answer[j]) of elements in this subset satisfies:
        answer[i] % answer[j] == 0, or
        answer[j] % answer[i] == 0
    If there are multiple solutions, return any of them.

    Example 1:
        Input: nums = [1, 2, 3]
        Output: [1, 2]
        Explanation: [1, 3] is also accepted.

    Example 2:
        Input: nums = [1, 2, 4, 8]
        Output: [1, 2, 4, 8]
    """


class Specifications:
    """
    0. First, sort the numbers in ascending order.
    1. Constraint: Each pair in the subset must satisfy nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0.
    2. Note: If a % b == 0 and b % c == 0, then a % c == 0. This property allows us to build chains.
    3. The starting point can be any element in the array, so iterate through all possible starts.
    4. Add a number to the subset only if it satisfies the divisibility condition with the previous number.
    5. Return the largest subset found that meets the above conditions.
    """


class EfficiencyHandling:
    """
    Time Complexity: O(N^2), where N is the length of nums.
    Space Complexity: O(N), due to memoization and recursion stack.
    """


class Pseudocode:
    """
    FUNCTION largest_subset(nums):
        SORT nums in ascending order
        memo = {}

        FUNCTION helper(start, idx):
            IF (start, idx) in memo:
                RETURN memo[(start, idx)]

            subset = []
            FOR i FROM idx TO len(nums) - 1:
                IF nums[i] % start == 0:
                    candidate = helper(nums[i], i + 1)
                    IF len(candidate) > len(subset):
                        subset = candidate

            memo[(start, idx)] = [start] + subset
            RETURN memo[(start, idx)]

        max_subset = []
        FOR i FROM 0 TO len(nums) - 1:
            candidate = helper(nums[i], i + 1)
            IF len(candidate) > len(max_subset):
                max_subset = candidate

        RETURN max_subset
    """

