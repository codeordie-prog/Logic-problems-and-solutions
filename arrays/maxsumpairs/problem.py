
class ProblemStatement:
    """
    You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, 
    such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
    Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j 
    that satisfy the conditions. If no such pair of indices exists, return -1.

    Example 1:
    Input: nums = [18,43,36,13,7]
    Output: 54
    Explanation: The pairs (i, j) that satisfy the conditions are:
    - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
    - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
    So the maximum sum that we can obtain is 54.

    Example 2:
    Input: nums = [10,12,19,14]
    Output: -1
    Explanation: There are no two numbers that satisfy the conditions, so we return -1.
    """


class Specifications:
    """
    Problem Specifications:

    - For each number in the input list, compute the sum of its digits.
    - Group numbers by their digit sum using a dictionary (key: digit sum, value: list of numbers).
    - For each group with at least two numbers, find the two largest numbers and compute their sum.
    - Return the maximum such sum across all groups. If no group has at least two numbers, return -1.

    Optimized Approach:
    - Instead of storing all numbers for each digit sum, keep only the two largest numbers per group.
    - This reduces space complexity and eliminates the need for sorting.
    """

class EfficiencyHandling:
    """
    Efficiency Analysis:

    1. Initial Approach:
        - Time Complexity: O(N log N), where N is the number of elements. This is due to sorting the groups of numbers.
        - Space Complexity: O(N), for storing all numbers in the groups.

    2. Optimized Approach:
        - Time Complexity: O(N), as each number is processed once and only the two largest numbers per group are tracked.
        - Space Complexity: O(K), where K is the number of unique digit sums (at most 81 for non-negative integers up to 999999999).
    """

class Pseudocode:
    """
    Initial Approach:

        FUNCTION max_sum_pairs(nums):
            store = defaultdict(list)

            FUNCTION digit_sum(num):
                total = 0
                WHILE num > 0:
                    total += num % 10
                    num //= 10
                RETURN total

            FOR num IN nums:
                s = digit_sum(num)
                store[s].append(num)

            max_sum = -1
            FOR group IN store.values():
                IF len(group) >= 2:
                    group.sort(reverse=True)
                    max_sum = max(max_sum, group[0] + group[1])
            RETURN max_sum

    Optimized Approach:

        FUNCTION max_sum_pairs_optimized(nums):
            store = {}
            max_sum = -1

            FUNCTION digit_sum(num):
                total = 0
                WHILE num > 0:
                    total += num % 10
                    num //= 10
                RETURN total

            FOR num IN nums:
                s = digit_sum(num)
                IF s IN store:
                    max_sum = max(max_sum, num + store[s])
                    store[s] = max(num, store[s])
                ELSE:
                    store[s] = num
            RETURN max_sum
    """