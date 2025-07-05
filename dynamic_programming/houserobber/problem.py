class ProblemStatement:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
    The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
    will automatically contact the police if two adjacent houses are broken into on the same night.

    Given an integer array 'nums' representing the amount of money in each house, return the maximum amount of money you
    can rob tonight without alerting the police.

    Example 1:
        Input: nums = [1, 2, 3, 1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

    Example 2:
        Input: nums = [2, 7, 9, 3, 1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.
    """

class Specifications:
    """
    1. Recognize the choices at each house - For a given house, you have two options: rob it or skip it.
        - If you rob the current house, you must skip the next house.
        - If you skip the current house, you can consider the next house.

    2. Use memoization to cache results for efficiency and avoid redundant calculations.

    3. Return the maximum amount between robbing and not robbing the current house.
    """

class EfficiencyHandling:
    """
    Time Complexity:
        - O(N), where N is the number of houses. Each house is processed once due to memoization.
    Space Complexity:
        - O(N), for the memoization cache and recursion stack.
    """

class Pseudocode:
    """
    FUNCTION rob(nums):
        memo = {}
        
        FUNCTION helper(idx):
            IF idx >= LENGTH(nums):
                RETURN 0
            
            IF idx IN memo:
                RETURN memo[idx]
            
            rob_current = nums[idx] + helper(idx + 2)
            skip_current = helper(idx + 1)
            
            result = MAX(rob_current, skip_current)
            memo[idx] = result
            RETURN memo[idx]
        
        RETURN helper(0)
    """