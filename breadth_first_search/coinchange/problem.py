
class ProblemStatement:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.

    Example 1:
        Input: coins = [1, 2, 5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Example 2:
        Input: coins = [2], amount = 3
        Output: -1

    Example 3:
        Input: coins = [1], amount = 0
        Output: 0
    """


class Specifications:
    """
    Approach 1 - Recursion with Memoization

    1. If amount == 0, return 0.
    2. Since each coin can be used infinitely, we cannot use a greedy approach. Instead, try each coin in every recursive call.
    3. Use memoization to avoid redundant calculations.
    4. Base cases:
        - If remainder == 0, return 0 (no coins needed).
        - If remainder < minimum coin value, return infinity (not possible).
    5. For each coin, recursively compute the minimum coins needed for (remainder - coin).
    6. Among all possible coins, select the minimum count.
    7. If no combination is possible, return -1.
    """


class EfficiencyHandling:
    """
    Time Complexity:
        O(N * M), where N is the number of coins and M is the amount.

    Space Complexity:
        O(M), due to memoization storage for each sub-amount.
    """


class Pseudocode:
    """
    FUNCTION coin_change(coins, amount):
        IF amount == 0:
            RETURN 0

        min_value = MIN(coins)
        memo = {}

        FUNCTION helper(remainder):
            IF remainder == 0:
                RETURN 0
            IF remainder IN memo:
                RETURN memo[remainder]
            IF remainder < min_value:
                RETURN infinity

            min_count = infinity
            FOR coin IN coins:
                rem = remainder - coin
                count = 1 + helper(rem)
                min_count = MIN(min_count, count)
            memo[remainder] = min_count
            RETURN min_count

        min_count = helper(amount)
        IF min_count == infinity:
            RETURN -1
        RETURN min_count
    """